"""
This modules extends the base_tasks modules by providing task logic around the Choice World protocol
"""
from abc import abstractmethod
import json
import math
import random
import logging

import numpy as np
import pandas as pd

from iblutil.util import Bunch

import iblrig.base_tasks
from iblrig.path_helper import SessionPathCreator
import iblrig.iotasks as iotasks
import iblrig.user_input as user
import iblrig.misc as misc
from iblrig.check_sync_pulses import sync_check

log = logging.getLogger(__name__)

NTRIALS_INIT = 1000

# todo sess update plots
# todo camera mixin: choose modality


class OnlineGraphsMixin(object):

    def update_plots(self):
        pass
        # stop_crit = self.check_stop_criterions()
        # # clean this up and remove display from logic
        # if stop_crit and self.task_params.USE_AUTOMATIC_STOPPING_CRITERIONS:
        #     if stop_crit == 1:
        #         msg = "STOPPING CRITERIA Nº1: PLEASE STOP TASK AND REMOVE MOUSE\
        #         \n < 400 trials in 45min"
        #         f.patch.set_facecolor("xkcd:mint green")
        #     elif stop_crit == 2:
        #         msg = "STOPPING CRITERIA Nº2: PLEASE STOP TASK AND REMOVE MOUSE\
        #         \nMouse seems to be inactive"
        #         f.patch.set_facecolor("xkcd:yellow")
        #     elif stop_crit == 3:
        #         msg = "STOPPING CRITERIA Nº3: PLEASE STOP TASK AND REMOVE MOUSE\
        #         \n> 90 minutes have passed since session start"
        #         f.patch.set_facecolor("xkcd:red")
        #
        #     if not self.task_params.SUBJECT_DISENGAGED_TRIGGERED and stop_crit:
        #         patch = {
        #             "SUBJECT_DISENGAGED_TRIGGERED": stop_crit,
        #             "SUBJECT_DISENGAGED_TRIALNUM": i + 1,
        #         }
        #         self.paths.patch_settings_file(patch)
        #     [log.warning(msg) for x in range(5)]


class ChoiceWorldSession(
    iblrig.base_tasks.BaseSession,
    iblrig.base_tasks.BonsaiRecordingMixin,
    iblrig.base_tasks.BonsaiVisualStimulusMixin,
    iblrig.base_tasks.BpodMixin,
    iblrig.base_tasks.Frame2TTLMixin,
    iblrig.base_tasks.RotaryEncoderMixin,
    iblrig.base_tasks.SoundMixin,
    iblrig.base_tasks.ValveMixin,
):

    def __init__(self, fmake=True, interactive=False, *args,  **kwargs):
        super(ChoiceWorldSession, self).__init__(*args, **kwargs)
        self.interactive = interactive
        # Create the folder architecture and get the paths property updated
        if not fmake:
            make = False
        elif fmake and "ephys" in self.pybpod_settings.PYBPOD_BOARD:
            make = True  # True makes only raw_behavior_data folder
        else:
            make = ["video"]  # besides behavior which folders to creae
            # todo move the paths creation to the abstract class so mixins can be instantiated
        spc = SessionPathCreator(
            self.pybpod_settings.PYBPOD_SUBJECTS[0],  #
            # fixme subject needed here
            protocol=self.pybpod_settings.PYBPOD_PROTOCOL,
            make=make)
        self.paths = Bunch(spc.__dict__)
        # Session data
        if self.interactive:
            self.SUBJECT_WEIGHT = user.ask_subject_weight(self.pybpod_settings.PYBPOD_SUBJECTS[0])
            self.task_params.SESSION_START_DELAY_SEC = user.ask_session_delay(self.paths.SETTINGS_FILE_PATH)
        else:
            self.SUBJECT_WEIGHT = np.NaN
        self.display_logs()
        # init the trials table
        self.trial_num = -1
        self.block_trial_num = -1
        self.block_num = -1
        self.block_len = -1
        self.ntrials_correct = 0
        self.water_delivered = 0
        self.behavior_data = []
        self.movement_left = self.device_rotary_encoder.THRESHOLD_EVENTS[
            self.task_params.QUIESCENCE_THRESHOLDS[0]]
        self.movement_right = self.device_rotary_encoder.THRESHOLD_EVENTS[
            self.task_params.QUIESCENCE_THRESHOLDS[1]]

        self.trials_table = pd.DataFrame({
            'block_num': np.zeros(NTRIALS_INIT, dtype=np.int16),
            'block_trial_num': np.zeros(NTRIALS_INIT, dtype=np.int16),
            'contrast': np.zeros(NTRIALS_INIT) * np.NaN,
            'position': np.zeros(NTRIALS_INIT) * np.NaN,
            'quiescent_period': np.zeros(NTRIALS_INIT) * np.NaN,
            'response_side': np.zeros(NTRIALS_INIT, dtype=np.int8),
            'response_time': np.zeros(NTRIALS_INIT) * np.NaN,
            'reward_amount': np.zeros(NTRIALS_INIT) * np.NaN,
            'reward_valve_time': np.zeros(NTRIALS_INIT) * np.NaN,
            'stim_angle': np.zeros(NTRIALS_INIT) * np.NaN,
            'stim_freq': np.zeros(NTRIALS_INIT) * np.NaN,
            'stim_gain': np.zeros(NTRIALS_INIT) * np.NaN,
            'stim_phase': np.zeros(NTRIALS_INIT) * np.NaN,
            'stim_probability_left': np.zeros(NTRIALS_INIT),
            'stim_reverse': np.zeros(NTRIALS_INIT) * np.NaN,
            'stim_sigma': np.zeros(NTRIALS_INIT) * np.NaN,
            'trial_correct': np.zeros(NTRIALS_INIT, dtype=bool),
            'trial_num': np.zeros(NTRIALS_INIT, dtype=np.int16),
        })

        self.as_data = {
            "Temperature_C": -1,
            "AirPressure_mb": -1,
            "RelativeHumidity": -1,
        }

    def start(self):
        """
        In this step we explicitely run the start methods of the various mixins.
        The super class start method is overloaded because we need to start the different hardware pieces in order
        """
        self.start_mixin_frame2ttl()
        self.start_mixin_bpod()
        self.start_mixin_valve()
        self.start_mixin_sound()
        self.start_mixin_rotary_encoder()
        self.start_mixin_bonsai_cameras()
        self.start_mixin_bonsai_microphone()
        self.start_mixin_bonsai_visual_stimulus()

    """
    Those are the methods that need to be implemented for a new task
    """
    @abstractmethod
    def new_block(self):
        pass

    @abstractmethod
    def next_trial(self):
        pass

    """
    Those are the properties that are used in the state machine code
    """
    @property
    def reward_time(self):
        return self.valve.reward_time

    @property
    def quiescent_period(self):
        return self.trials_table.at[self.trial_num, 'quiescent_period']

    @property
    def position(self):
        return self.trials_table.at[self.trial_num, 'position']

    @property
    def event_error(self):
        return self.device_rotary_encoder.THRESHOLD_EVENTS[self.position]

    @property
    def event_reward(self):
        return self.device_rotary_encoder.THRESHOLD_EVENTS[-self.position]

    def send_trial_info_to_bonsai(self):
        """
        This sends the trial information to the Bonsai UDP port for the stimulus
        The OSC protocol is documented in iblrig.base_tasks.BonsaiVisualStimulusMixin
        """
        bonsai_viz_client = self.bonsai_stimulus['udp_client']
        bonsai_dict = {k: self.trials_table[k][self.trial_num] for k in
                       bonsai_viz_client.OSC_PROTOCOL
                       if k in self.trials_table.columns}
        bonsai_viz_client.send2bonsai(**bonsai_dict)

    def trial_completed(self, behavior_data):
        """Update outcome variables using bpod.session.current_trial
        Check trial for state entries, first value of first tuple"""
        # Update elapsed_time
        self.behavior_data = behavior_data
        correct = ~np.isnan(self.behavior_data["States timestamps"]["correct"][0][0])
        error = ~np.isnan(self.behavior_data["States timestamps"]["error"][0][0])
        no_go = ~np.isnan(self.behavior_data["States timestamps"]["no_go"][0][0])
        assert correct or error or no_go
        # Add trial's response time to the buffer
        self.trials_table.at[self.trial_num, 'response_time'] = misc.get_trial_rt(self.behavior_data)
        self.trials_table.at[self.trial_num, 'trial_correct'] = bool(correct)
        self.trials_table.at[self.trial_num, 'reward_amount'] = self.draw_reward_amount()

        # Update response buffer -1 for left, 0 for nogo, and 1 for rightward
        # what happens if position is 0?
        position = self.trials_table.at[self.trial_num, 'position']
        if (correct and position < 0) or (error and position > 0):
            response_side = 1
        elif (correct and position > 0) or (error and position < 0):
            response_side = -1
        elif no_go:
            response_side = 0
        self.trials_table.at[self.trial_num, 'response_side'] = response_side

        # SAVE TRIAL DATA
        # todo add the table current record
        save_dict = {"behavior_data": behavior_data}
        # Dump and save
        with open(self.paths['DATA_FILE_PATH'], 'a') as fp:
            fp.write(json.dumps(save_dict, cls=iotasks.ComplexEncoder) + '\n')
        # If more than 42 trials save transfer_me.flag
        if self.trial_num == 42:
            misc.create_flags(self.paths.DATA_FILE_PATH, self.task_params.POOP_COUNT)

    def check_stop_criterions(self):
        return misc.check_stop_criterions(
            self.init_datetime, self.trials_table['response_time'].values(), self.trial_num
        )

    def draw_reward_amount(self):
        """
        This method is to be overloaded if the task has a variable reward
        :return:
        """
        # fixme: correlation with valve reward time ?!?
        return self.task_params.REWARD_AMOUNT

    def draw_quiescent_period(self):
        """
        The quiescent period is drawn from a truncated exponential distribution
        """
        return self.task_params.QUIESCENT_PERIOD + misc.texp(factor=0.35, min_=0.2, max_=0.5)

    def draw_contrast(self):
        return misc.draw_contrast(self.task_params.CONTRAST_SET,
                                  self.task_params.CONTRAST_SET_PROBABILITY_TYPE)

    def check_sync_pulses(self):
        return sync_check(self)

    def show_trial_log(self):
        msg = f"""
##########################################
TRIAL NUM:            {self.trial_num}
STIM POSITION:        {self.position}
STIM CONTRAST:        {self.contrast}
STIM PHASE:           {self.stim_phase}

BLOCK NUMBER:         {self.block_num}
BLOCK LENGTH:         {self.block_len}
TRIALS IN BLOCK:      {self.block_trial_num}
STIM PROB LEFT:       {self.stim_probability_left}

RESPONSE TIME:        {self.response_time_buffer[-1]}
TRIAL CORRECT:        {self.trial_correct}

NTRIALS CORRECT:      {self.ntrials_correct}
NTRIALS ERROR:        {self.trial_num - self.ntrials_correct}
WATER DELIVERED:      {np.round(self.water_delivered, 3)} µl
TIME FROM START:      {self.elapsed_time}
TEMPERATURE:          {self.as_data['Temperature_C']} ºC
AIR PRESSURE:         {self.as_data['AirPressure_mb']} mb
RELATIVE HUMIDITY:    {self.as_data['RelativeHumidity']} %
##########################################"""
        log.info(msg)

    def draw_position(self, position_set=None, pleft=None):
        position_set = position_set or self.task_params.STIM_POSITIONS
        pleft = pleft or self.block_probability_left
        return int(np.random.choice(position_set, p=[pleft, 1 - pleft]))

    def psychometric_curve(self):
        pd_table = self.trials_table.iloc[:self.trial_num, :].copy()
        pd_table['signed_contrast'] = np.sign(pd_table['position']) * pd_table['contrast']

        psychometric_curves = pd_table.groupby('signed_contrast').agg(
            count=pd.NamedAgg(column="signed_contrast", aggfunc="count"),
            response_time=pd.NamedAgg(column="response_time", aggfunc="mean"),
            performance=pd.NamedAgg(column="trial_correct", aggfunc="mean"),
        )
        return psychometric_curves

    @property
    def iti_reward(self, assert_calibration=True):
        """
        Returns the ITI time that needs to be set in order to achieve the desired ITI,
        by subtracting the time it takes to give a reward from the desired ITI.
        """
        if assert_calibration:
            assert 'REWARD_VALVE_TIME' in self.calibration.keys(), 'Reward valve time not calibrated'
        return self.task_params.ITI_CORRECT - self.calibration.get('REWARD_VALVE_TIME', None)

    def reprJSON(self):
        """
        JSON representation of the session parameters - one way street
        :return:
        """
        def remove_from_dict(sx):
            if "weighings" in sx.keys():
                sx["weighings"] = None
            if "water_administration" in sx.keys():
                sx["water_administration"] = None
            return sx

        d = self.__dict__.copy()
        d["GO_TONE"] = "go_tone(freq={}, dur={}, amp={})".format(
            self.task_params.GO_TONE_FREQUENCY,
            self.task_params.GO_TONE_DURATION,
            self.task_params.GO_TONE_AMPLITUDE
        )
        d["WHITE_NOISE"] = "white_noise(freq=-1, dur={}, amp={})".format(
            self.task_params.WHITE_NOISE_DURATION,
            self.task_params.WHITE_NOISE_AMPLITUDE
        )

        d["SD"] = str(d.get('SD', None))
        d["CALIB_FUNC"] = str(d.get('CALIB_FUNC', None))

        d["LAST_TRIAL_DATA"] = None
        d["LAST_SETTINGS_DATA"] = None
        return d

    def display_logs(self):
        if self.paths.PREVIOUS_DATA_FILE:
            msg = f"""
##########################################
PREVIOUS SESSION FOUND
LOADING PARAMETERS FROM:       {self.PREVIOUS_DATA_FILE}
PREVIOUS NTRIALS:              {self.LAST_TRIAL_DATA["trial_num"]}
PREVIOUS WATER DRANK:          {self.LAST_TRIAL_DATA["water_delivered"]}
LAST REWARD:                   {self.LAST_TRIAL_DATA["reward_amount"]}
LAST GAIN:                     {self.LAST_TRIAL_DATA["stim_gain"]}
PREVIOUS WEIGHT:               {self.LAST_SETTINGS_DATA["SUBJECT_WEIGHT"]}
##########################################"""
            log.info(msg)

    def softcode_handler(self, code):
        """
         Soft codes should work with resasonable latency considering our limiting
         factor is the refresh rate of the screen which should be 16.667ms @ a frame
         rate of 60Hz
         1 : go_tone
         2 : white_noise
         """
        if code == 0:
            self.stop_sound()
        elif code == 1:
            self.play_tone()
        elif code == 2:
            self.play_noise()
        elif code == 3:
            self.trigger_bonsai_cameras()


class BiasedChoiceWorldSession(ChoiceWorldSession):

    def new_block(self):
        """
        if block_init_5050
            First block has 50/50 probability of leftward stim
            is 90 trials long
        """
        self.block_num += 1  # the block number is zero based
        self.block_trial_num = 0
        # handles the block length logic
        if self.task_params.BLOCK_INIT_5050 and self.block_num == 0:
            self.block_len = 90
        else:
            self.block_len = int(misc.texp(
                factor=self.task_params.BLOCK_LEN_FACTOR,
                min_=self.task_params.BLOCK_LEN_MIN,
                max_=self.task_params.BLOCK_LEN_MAX
            ))

        if self.block_num == 0:
            if self.task_params.BLOCK_INIT_5050:
                self.block_probability_left = 0.5
            else:
                self.block_probability_left = np.random.choice(self.task_params.BLOCK_PROBABILITY_SET)
        elif self.block_num == 1 and self.task_params.BLOCK_INIT_5050:
            self.block_probability_left = np.random.choice(self.task_params.BLOCK_PROBABILITY_SET)
        else:
            # this switches the probability of leftward stim for the next block
            self.block_probability_left = round(abs(1 - self.block_probability_left), 1)

    def next_trial(self):
        # First trial exception
        self.trial_num += 1
        self.block_trial_num += 1
        self.trial_correct = None
        if self.block_trial_num > (self.block_len - 1):
            self.new_block()
        pos = self.draw_position()
        self.trials_table.at[self.trial_num, 'quiescent_period'] = self.draw_quiescent_period()
        self.trials_table.at[self.trial_num, 'contrast'] = self.draw_contrast()
        self.trials_table.at[self.trial_num, 'stim_phase'] = random.uniform(0, 2 * math.pi)
        self.trials_table.at[self.trial_num, 'stim_sigma'] = self.task_params.STIM_SIGMA
        self.trials_table.at[self.trial_num, 'stim_angle'] = self.task_params.STIM_ANGLE
        self.trials_table.at[self.trial_num, 'block_num'] = self.block_num
        self.trials_table.at[self.trial_num, 'block_trial_num'] = self.block_trial_num
        self.trials_table.at[self.trial_num, 'stim_freq'] = self.task_params.STIM_FREQ
        self.trials_table.at[self.trial_num, 'stim_probability_left'] = self.block_probability_left
        self.trials_table.at[self.trial_num, 'trial_num'] = self.trial_num
        self.trials_table.at[self.trial_num, 'position'] = pos
        self.send_trial_info_to_bonsai()
