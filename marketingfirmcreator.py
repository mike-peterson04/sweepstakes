import user_interface
from marketingfirm import MarketingFirm


class MarketingFirmCreator:
    # def __init__(self):
    #     self.firm = self.choose_manager_type()
    #     return self.firm

    def choose_manager_type(self):
        manager_type = user_interface.select_manager()
        firm = MarketingFirm(manager_type)
        return firm

