from iblrig.base_choice_world import TrainingChoiceWorldSession
import iblrig.misc

TRAINING_PHASE = -1
ADAPTIVE_REWARD = -1.0


class Session(TrainingChoiceWorldSession):
    extractor_tasks = ['TrialRegisterRaw', 'ChoiceWorldTrials', 'TrainingStatus']

    @staticmethod
    def extra_parser():
        """ :return: argparse.parser() """
        parser = super(Session, Session).extra_parser()
        parser.add_argument('--training_phase', option_strings=['--training_phase'],
                            dest='training_phase', default=TRAINING_PHASE, type=int)
        parser.add_argument('--adaptive_reward', option_strings=['--adaptive_reward'],
                            dest='adaptive_reward', default=ADAPTIVE_REWARD, type=float)
        return parser


if __name__ == "__main__":  # pragma: no cover
    kwargs = iblrig.misc.get_task_arguments(parents=[Session.extra_parser()])
    sess = Session(**kwargs)
    sess.run()
