from adafruit_motorkit import MotorKit
import board

def main():
    kit = MotorKit(i2c=board.I2C())
    m1      = kit.motor1
    m2      = kit.motor2
    m3      = kit.motor3
    m4      = kit.motor4

    m1.throttle = 0.3
    while 1:
        continue


if __name__ == '__main__':
    main()
