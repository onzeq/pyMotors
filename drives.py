import time
from adafruit_motorkit import MotorKit
import board

def main():
    kit = MotorKit(i2c=board.I2C())
    m1      = kit.motor1
    m2      = kit.motor2
    m3      = kit.motor3
    m4      = kit.motor4

    
    while 1:
        kit.motor1.throttle = 1.0
        time.sleep(0.5)
        kit.motor1.throttle = 0
        
    


if __name__ == '__main__':
    main()
