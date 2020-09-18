import wpilib
import rev
from wpilib import DMC60
from wpilib import VictorSP as vSP
from wpilib.drive import DifferentialDrive as Drivetrain
from wpilib import SpeedControllerGroup as sCG
from ctre import WPI_VictorSPX as vSPX
from ctre import WPI_TalonSRX as tSRX
from rev.color import ColorSensorV3

class Beatrice(wpilib.TimedRobot):

    def robotInit(self):
        self.printTimer = wpilib.Timer()
        self.printTimer.start()

        self.xbox = wpilib.XboxController(0)
        self.lh = wpilib.interfaces.GenericHID.Hand(0)
        self.rh = wpilib.interfaces.GenericHID.Hand(1)
        self.colorSensor = ColorSensorV3(wpilib.I2C.Port.kOnboard)
        self.ultrasonicSensor = wpilib.AnalogInput(0)
        # self.ultrasonicSensor2 = wpilib.AnalogInput(1)
        self.gyro = wpilib.ADXRS450_Gyro()

        # Drivetrain
        self.lDrive = sCG(vSPX(0), vSPX(3))
        self.rDrive = sCG(vSPX(1), vSPX(2))
        self.drive = Drivetrain(self.lDrive, self.rDrive)

        # Grab: Long rod that pulls all the ball in
        self.grab = tSRX(0)

        # Shoot
        self.shoot1 = tSRX(1)
        self.shoot2 = tSRX(2)
        self.shoot2.setInverted(1)
        self.shoot = sCG(self.shoot1, self.shoot2)

        # Elevator
        self.elevator = DMC60(0)

        # Wheel: Wheel to rotate wheel
        self.wheel = rev.CANSparkMax(1, rev.CANSparkMaxLowLevel.MotorType(0))

        # Lift
        self.lift1 = vSP(1)
        self.lift2 = vSP(2)
        self.lift = sCG(self.lift1, self.lift2)

        self.reset()  # i.e. ensure defaults are set
        self.speedRatio = 2/3
        self.goneUp = 0

        self.loops = 0  # counter for program loops
        self.timer = wpilib.Timer()  # init timer

    def reset(self):
        pass

    def controlDrive(self):
        lh_y = self.xbox.getY(self.lh)*0.7  # shift gears
        rh_x = self.xbox.getX(self.rh)*0.8

        self.drive.arcadeDrive(lh_y, rh_x, 1)

    def controlGrab(self):
        if self.xbox.getBumper(self.lh):
            self.grab.set(-0.5)
        else:
            self.grab.set(0)

    def controlWheel(self):
        if self.xbox.getYButton():
            self.wheel.set(0.5)
        else:
            self.wheel.set(0)

    def controlElevator(self):
        if self.xbox.getBumper(self.rh):
            self.elevator.set(-0.9)
        else:
            self.elevator.set(0)

    def controlShoot(self):
        if self.xbox.getXButton():
            self.shoot.set(0.5)
        else:
            self.shoot.set(0)

    def controlLift(self):
        if self.xbox.getStartButton():
            self.goneUp = 1
            self.lift.set(-0.5)
        elif self.xbox.getBackButton() and self.goneUp:
            self.lift.set(0.75)
        else:
            self.lift.set(0)

    def autonomousInit(self):
        self.reset()

    def autonomousPeriodic(self):
        # write autonomous things
        pass

    def disabledInit(self):
        self.reset()

    def disabledPeriodic(self):
        self.reset()

    def teleopInit(self):
        self.reset()
        self.drive.setSafetyEnabled(1)

    def senseColor(self):
        color = self.colorSensor.getColor()

        # Get the individual components of the color
        red = round(color.red*255, 0)
        green = round(color.green*255, 0)

        color = "None"
        if red > 120:
            color = "red"
        elif green > 90:
            color = "blue"
            if green > 130:
                color = "green"
                if red > 70:
                    color = "yellow"
        else:
            color = "unknown"

        return color

    def logSomething(self):
        if self.printTimer.hasPeriodPassed(1):
            self.logger.info("Color: {}".format(self.senseColor()))

    def teleopPeriodic(self):
        self.controlDrive()
        self.controlGrab()
        self.controlShoot()
        self.controlElevator()
        self.controlWheel()
        self.controlLift()

        logging = 0

        if logging:
            self.logSomething()


if __name__ == '__main__':
    wpilib.run(Beatrice)
