from contestant import Contestant
from sweepstake import Sweepstake


def run_simulation():
    contestants = generate_test_users()
    s = Sweepstake('test')
    for x in contestants:
        s.register_contestant(x)


if __name__ == '__main__':
    run_simulation()
