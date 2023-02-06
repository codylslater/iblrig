#!/usr/bin/env python
# @Author: Niccolò Bonacchi
# @Creation_Date: Thursday, January 31st 2019, 4:12:19 pm
# @Editor: Michele Fabbri
# @Edit_Date: 2022-02-01
"""
Find the number of poop pellets recorded by user
"""
from pathlib import Path

from dateutil import parser

from iblrig.graphic import numinput
from iblrig.misc import patch_settings_file

from iblrig.path_helper import load_extrasettings # needed to stop the remotes if connected

IBLRIG_DATA = Path().cwd().parent.parent.parent.parent / "iblrig_data" / "Subjects"  # noqa


def poop() -> None:
     # maybe this is a good time to stop the recording..
    extrasettings = load_extrasettings()
    if 'labcams_addresses' in extrasettings.keys():
        for dval in extrasettings['labcams_addresses']:
            address = (dval['address'],dval['port'])
            import socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto('softtrigger=0'.encode(), 0, address)
            sock.sendto('acquire=0'.encode(), 0, address)
    # Developers: Do you have advise on a better place for this? THANKS!!
    
    poop_flags = list(IBLRIG_DATA.rglob("poop_count.flag"))
    poop_flags = sorted(
        poop_flags, key=lambda x: (parser.parse(x.parent.parent.name), int(x.parent.name)),
    )
    if not poop_flags:
        return
    flag = poop_flags[-1]
    session_name = "/".join(flag.parent.parts[-3:])
    poop_count = numinput(
        "Poop up window", f"Enter poop pellet count for session: \n{session_name}"
    )
    patch = {"POOP_COUNT": poop_count}
    patch_settings_file(str(flag.parent), patch)
    flag.unlink()


if __name__ == "__main__":
    poop()
    # IBLRIG_DATA = '/home/nico/Projects/IBL/github/iblrig/scratch/test_iblrig_data/Subjects'  # noqa
    # IBLRIG_DATA = Path(IBLRIG_DATA)
    # print('.')
