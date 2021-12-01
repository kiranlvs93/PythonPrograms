import random
import datetime
import time


def waiting_game_method1():
    """
    Method 1
    Generate a random no b/w 1-5 seconds
	Print a msg saying that the user waits for those many seconds and press enter to start
	Enter is pressed
	Wait for next enter and capture the time interval from previous enter
	Subtract the current time - old time - timetowait to get the delay
    :return:
    """
    print("Begin waiting game.Enter 'quit' to quit the game")
    while True:
        best_time = 0
        exp_wait_time = random.randint(1, 5)
        print("****************************************")
        inp = input(f"Your target time is {exp_wait_time}sec.\n------Press enter to begin------\n "
                    f"...Press enter again exactly after {exp_wait_time}sec...")
        if inp == 'quit':
            break
        then = datetime.datetime.now()
        input()
        now = datetime.datetime.now()
        diff = now - then - datetime.timedelta(0, exp_wait_time)
        print(f"\nElapse time:: {(now - then).seconds}.{(now - then).microseconds} seconds")
        print(f"{diff.seconds}.{diff.microseconds} seconds delay")


def waiting_game_method2():
    target = random.randint(2, 4)  # target seconds to wait
    print(f"Your target time is {target} seconds")
    input(' ---Press Enter to Begin--- ')
    start = time.perf_counter()

    input(f'\n... Press Enter again after {target} seconds...')
    elapsed = time.perf_counter() - start

    print("\nElapsed time: {0:.3f} seconds".format(elapsed))
    if elapsed == target:
        print('(Unbelievable! Perfect timing!)')
    elif elapsed < target:
        print('({0:.3f} seconds too fast)'.format(target - elapsed))
    else:
        print('({0:.3f} seconds too slow)'.format(elapsed - target))


if __name__ == '__main__':
    waiting_game_method2()
