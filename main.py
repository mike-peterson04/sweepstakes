from contestant import Contestant
from sweepstake import Sweepstake
import user_interface


def run_simulation():
    contestants = user_interface.generate_test_users()
    s = Sweepstake('test')
    for x in contestants:
        s.register_contestant(x)
        s.print_contestant_info(x)


if __name__ == '__main__':
    run_simulation()
