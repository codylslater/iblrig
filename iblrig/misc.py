"""
Provides collection of functionality used throughout the iblrig repository.

Assortment of functions, frequently used, but without a great deal of commonality. Functions can,
and should, be broken out into their own files and/or classes as the organizational needs of this
repo change over time.
"""
import argparse
import datetime
import logging
from pathlib import Path
from typing import Optional, Union, Literal, Iterable

import numpy as np


FLAG_FILE_NAMES = [
    "transfer_me.flag",
    "create_me.flag",
    "poop_count.flag",
    "passive_data_for_ephys.flag",
]

log = logging.getLogger("iblrig")


def _get_task_argument_parser(parents=None):
    """
    This function returns the task argument parser with extra optional parameters if provided
    This function is kept separate from parsing for unit tests purposes.
    """
    parser = argparse.ArgumentParser(parents=parents or [])
    parser.add_argument("-s", "--subject", required=True, help="--subject ZFM-05725")
    parser.add_argument("-u", "--user", required=False, default=None,
                        help="alyx username to register the session")
    parser.add_argument("-p", "--projects", nargs="+", default=[],
                        help="project name(s), something like 'psychedelics' or 'ibl_neuropixel_brainwide_01'; if specify "
                             "multiple projects, use a space to separate them")
    parser.add_argument("-c", "--procedures", nargs="+", default=[],
                        help="long description of what is occurring, something like 'Ephys recording with acute probe(s)'; "
                             "be sure to use the double quote characters to encapsulate the description and a space to separate "
                             "multiple procedures")
    parser.add_argument('-w', '--weight', type=float, dest='subject_weight_grams',
                        required=False, default=None)
    parser.add_argument('--no-interactive', dest='interactive', action='store_false')
    parser.add_argument('--append', dest='append', action='store_true')
    parser.add_argument('--stub', type=Path, help="Path to _ibl_experiment.description.yaml stub file.")
    parser.add_argument('--log-level', default="INFO", help="verbosity of the console logger (default: INFO)",
                        choices=['NOTSET', 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL'])
    parser.add_argument('--wizard', dest='wizard', action='store_true')
    return parser


def _post_parse_arguments(**kwargs):
    """
    This is called to post-process the arguments after parsing. It is used to force the interactive
    mode to True (as it is a call from a user) and to override the settings file value for the user.
    This function is split for unit-test purposes.
    :param kwargs:
    :return:
    """
    # if the user is specified, then override the settings file value
    user = kwargs.pop('user')
    if user is not None:
        kwargs['iblrig_settings'] = {'ALYX_USER': user}
    return kwargs


def get_task_arguments(parents=None):
    """
    This function parses input to run the tasks. All the variables are fed to the Session instance
    task.py -s subject_name -p projects_name -c procedures_name --no-interactive
    :param extra_args: list of dictionaries of additional argparse arguments to add to the parser
        For example, to add a new toto and titi arguments, use:
        get_task_arguments({'--toto', type=str, default='toto'}, {'--titi', action='store_true', default=False})
    :return:
    """
    parser = _get_task_argument_parser(parents=parents)
    kwargs = vars(parser.parse_args())
    return _post_parse_arguments(**kwargs)


def _isdatetime(x: str) -> Optional[bool]:
    """
    Check if string is a date in the format YYYY-MM-DD.

    :param x: The string to check
    :return: True if the string matches the date format, False otherwise.
    :rtype: Optional[bool]
    """
    try:
        datetime.strptime(x, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def get_session_path(path: Union[str, Path]) -> Optional[Path]:
    """Returns the session path from any filepath if the date/number
    pattern is found"""
    if path is None:
        return
    if isinstance(path, str):
        path = Path(path)
    sess = None
    for i, p in enumerate(path.parts):
        if p.isdigit() and _isdatetime(path.parts[i - 1]):
            sess = Path().joinpath(*path.parts[: i + 1])

    return sess


def get_port_events(events: dict, name: str = "") -> list:
    out: list = []
    for k in events:
        if name in k:
            out.extend(events[k])
    out = sorted(out)

    return out


def texp(factor: float = 0.35, min_: float = 0.2, max_: float = 0.5) -> float:
    """Truncated exponential
    mean = 0.35
    min = 0.2
    max = 0.5
    """
    x = np.random.exponential(factor)
    if min_ <= x <= max_:
        return x
    else:
        return texp(factor=factor, min_=min_, max_=max_)


def get_biased_probs(n: int, idx: int = -1, p_idx: float = 0.5) -> list[float]:
    """
    Calculate biased probabilities for all elements of an array such that the
    `i`th value has probability `p_i` for being drawn relative to the remaining
    values.

    See: https://github.com/int-brain-lab/iblrig/issues/74

    Parameters
    ----------
    n : int
        The length of the array, i.e., the number of probabilities to generate.
    idx : int, optional
        The index of the value that has the biased probability. Defaults to -1.
    p_idx : float, optional
        The probability of the `idx`-th value relative to the rest. Defaults to 0.5.

    Returns
    -------
    List[float]
        List of biased probabilities.

    Raises
    ------
    ValueError
        If `idx` is outside the valid range [-1, n), or if `p_idx` is 0.
    """
    if idx < -1 or idx >= n:
        raise ValueError("Invalid index. Index should be in the range [-1, n).")
    if n == 1:
        return [1.0]
    if p_idx == 0:
        raise ValueError("Probability must be larger than 0.")
    z = n - 1 + p_idx
    p = [1 / z] * n
    p[idx] *= p_idx
    return p


def draw_contrast(contrast_set: Iterable[float],
                  probability_type: Literal["skew_zero", "biased", "uniform"] = "biased",
                  idx: int = -1,
                  idx_probability: float = 0.5) -> float:
    """
    Draw a contrast value from a given iterable based to the specified probability type

    Parameters
    ----------
    contrast_set : list[float]
        The set of contrast values from which to draw.
    probability_type : Literal["skew_zero", "biased", "uniform"], optional
        The type of probability distribution to use.
        - "skew_zero" or "biased": Draws with a biased probability distribution based on idx and idx_probability,
        - "uniform": Draws with a uniform probability distribution.
        Defaults to "biased".
    idx : int, optional
        Index for probability manipulation (with "skew_zero" or "biased"), default: -1.
    idx_probability : float, optional
        Probability for the specified index (with "skew_zero" or "biased"), default: 0.5.

    Returns
    -------
    float
        The drawn contrast value.

    Raises
    ------
    ValueError
        If an unsupported `probability_type` is provided.
    """
    if probability_type in ["skew_zero", "biased"]:
        p = get_biased_probs(n=len(contrast_set), idx=idx, p_idx=idx_probability)
        return np.random.choice(contrast_set, p=p)
    elif probability_type == "uniform":
        return np.random.choice(contrast_set)
    else:
        raise ValueError("Unsupported probability_type. Use 'skew_zero', 'biased', or 'uniform'.")
