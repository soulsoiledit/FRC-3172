import commands2

import constants

from commands.autonomous.autodrive import AutoDriveBW
from commands.autonomous.autodrive import AutoDriveFW
from commands.autonomous.autoshoot import AutoShoot

from subsystems.drive import DriveSubsystem
from subsystems.shooter import ShooterSubsystem

class AutoSequence(commands2.ParallelCommandGroup):

    def __init__(self, drive: DriveSubsystem, shooter: ShooterSubsystem):
        super().__init__(
            commands2.SequentialCommandGroup(
                AutoDriveBW(drive).withTimeout(4),
                AutoDriveFW(drive).withTimeout(1)
            ),

            commands2.SequentialCommandGroup(
                AutoShoot(shooter, -0.5).withTimeout(3),
                AutoShoot(shooter, -1).withTimeout(2)
            ),
        )
