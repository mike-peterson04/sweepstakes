from contestant import Contestant
from sweepstake import Sweepstake
from marketingfirmcreator import MarketingFirmCreator
import user_interface

# project requires package yagmail to be installed
# pip install -e git+https://github.com/kootenpv/yagmail#egg=yagmail[all]


def run_simulation():
    user_interface.bare_bones_front_end(MarketingFirmCreator())


if __name__ == '__main__':
    run_simulation()
