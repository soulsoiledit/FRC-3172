import commands2
import wpilib

from commands.autonomous.autodrive import AutoDriveBW
from commands.autonomous.autodrive import AutoDriveFW
from commands.autonomous.autoshoot import AutoShoot

from subsystems.drive import DriveSubsystem
from subsystems.shooter import ShooterSubsystem

class AutoSequence(commands2.ParallelCommandGroup):

    def __init__(self, drive: DriveSubsystem, shooter: ShooterSubsystem):
        super().__init__(
            commands2.SequentialCommandGroup(

                AutoDriveBW(drive).withTimeout(3),
                AutoDriveFW(drive).withTimeout(0.9)

                # 0.5 * 1.75 = 0.4375
                # 
                # 0.88*1.25-0.8*1.25 = .1
                # 3.5*0.5 = 1.75 + 0.1 = 1.85 / 0.5 = 3.7 as final time?
            ),

            commands2.SequentialCommandGroup(
                AutoShoot(shooter, -0.6).withTimeout(4.5)
            ),
        )
