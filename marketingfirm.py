import user_interface
from sweepstake import Sweepstake


class MarketingFirm:
    def __init__(self, manager):
        self.manager = manager

    def create_sweepstakes(self):
        sweepstake = Sweepstake(user_interface.name_sweepstake())
        self.manager.insert_sweepstakes(sweepstake)

