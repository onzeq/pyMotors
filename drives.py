from adafruit_motorkit import MotorKit


def main():
    kit     = MotorKit()
    m1      = kit.motor1
    m2      = kit.motor2
    m3      = kit.motor3
    m4      = kit.motor4

    m1.throttle = 0.3



if __name__ == '__main__':
    main()