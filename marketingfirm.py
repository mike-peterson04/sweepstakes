import user_interface
from sweepstake import Sweepstake


class MarketingFirm:
    # using dependency injection where MarketingFirm depends on having a compatible manager inserted
    # this makes the code more flexible as any manager with insert_sweepstakes(sweepstake) method will work
    def __init__(self, manager):
        self.manager = manager

    def create_sweepstakes(self):
        sweepstake = Sweepstake(user_interface.name_sweepstake())
        self.manager.insert_sweepstakes(sweepstake)

