import wpilib
import wpilib.simulation
from wpimath.system import LinearSystemId
from wpimath.system.plant import DCMotor

import constants

from pyfrc.physics.core import PhysicsInterface

import typing

if typing.TYPE_CHECKING:
    from robot import Cletus


class PhysicsEngine:
    """
    Simulates a motor moving something that strikes two limit switches,
    one on each end of the track. Obviously, this is not particularly
    realistic, but it's good enough to illustrate the point
    """

    def __init__(self, physics_controller: PhysicsInterface, robot: "Cletus"):

        self.physics_controller = physics_controller

        # Motors
        self.l_motor = wpilib.simulation.PWMSim(
            robot.container.drive.front_left.getChannel()
        )
        self.r_motor = wpilib.simulation.PWMSim(
            robot.container.drive.front_right.getChannel()
        )

        self.system = LinearSystemId.identifyDrivetrainSystem(1.98, 0.2, 1.5, 0.3)
        self.drivesim = wpilib.simulation.DifferentialDrivetrainSim(
            self.system,
            0.381 * 2,
            DCMotor.CIM(2),
            10,
            0.0508,
        )

    def update_sim(self, now: float, tm_diff: float) -> None:
        # Simulate the drivetrain
        l_motor = self.l_motor.getSpeed()
        r_motor = self.r_motor.getSpeed()

        voltage = wpilib.RobotController.getInputVoltage()
        self.drivesim.setInputs(r_motor * voltage, l_motor * voltage)
        self.drivesim.update(tm_diff)

        self.physics_controller.field.setRobotPose(self.drivesim.getPose())
