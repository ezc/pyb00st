#!/usr/bin/env python3

from pyb00st.movehub import MoveHub
from pyb00st.constants import *

from time import sleep

MY_MOVEHUB_ADD = '00:16:53:A4:CD:7E'
MY_BTCTRLR_HCI = 'hci0'

try:
    mymovehub = MoveHub(MY_MOVEHUB_ADD, MY_BTCTRLR_HCI)
    mymovehub.subscribe_all()
    mymovehub.listen_tilt(tilt_basic=True)

    while True:
        sleep(0.2)
        if mymovehub.last_tilt in TILT_BASIC_VALUES:
            print(TILT_BASIC_TEXT[mymovehub.last_tilt])
finally:
    mymovehub.stop()

