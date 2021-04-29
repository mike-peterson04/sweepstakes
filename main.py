from contestant import Contestant
from sweepstake import Sweepstake
import user_interface

# project requires package yagmail to be installed
# pip install -e git+https://github.com/kootenpv/yagmail#egg=yagmail[all]


def run_simulation():
    contestants = user_interface.generate_test_users()

    s = Sweepstake('test')
    for x in contestants:
        s.register_contestant(x)
    user_interface.notify_contestants(s, s.pick_winner())


if __name__ == '__main__':
    run_simulation()
