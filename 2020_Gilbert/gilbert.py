import board
import time
from adafruit_servokit import ServoKit
from digitalio import DigitalInOut, Direction


kit = ServoKit(channels=8)

pin_onoff = DigitalInOut(board.D21)
pin_onoff.direction = Direction.INPUT

pin_hightog = DigitalInOut(board.D19)
pin_hightog.direction = Direction.INPUT

pin_revtog = DigitalInOut(board.D16)
pin_revtog.direction = Direction.INPUT

for x in range(80):
    print(x, "On/Off: ", pin_onoff.value,
             " | High: ", pin_hightog.value,
             " | Rev: ", pin_revtog.value)
    if pin_onoff.value:
        if (pin_revtog.value and pin_hightog.value) or pin_revtog.value:
            kit.continuous_servo[0].throttle = -0.5
        elif pin_hightog.value and not pin_revtog.value:
            kit.continuous_servo[0].throttle = 1
        else:
            kit.continuous_servo[0].throttle = 0.5
    else:
        kit.continuous_servo[0].throttle = 0
    time.sleep(1)

kit.continuous_servo[0].throttle = 0
