import sys
import time
import argparse
import random
import pyautogui


SCREEN_SIZE = pyautogui.size()


def fishing(*args):
    pyautogui.moveTo(350, 1000)
    pyautogui.click()
    time.sleep(1)
    while True:
        pyautogui.keyDown('e')
        time.sleep(6)
        pyautogui.keyUp('e')
        time.sleep(6.2)


def oil_loop(hold_time):
    """
    Internal loop for collection oil based resources
    Returns: None (infinite loop)
    """
    while True:
        pyautogui.moveTo(350, 1000)
        pyautogui.mouseDown()
        time.sleep(hold_time)
        pyautogui.mouseUp()

        pyautogui.moveTo(500, 1000)
        pyautogui.mouseDown()
        time.sleep(hold_time)
        pyautogui.mouseUp()

        pyautogui.moveTo(630, 1000)
        pyautogui.mouseDown()
        time.sleep(hold_time)
        pyautogui.mouseUp()

        pyautogui.moveTo(775, 1000)
        pyautogui.mouseDown()
        time.sleep(hold_time)
        pyautogui.mouseUp()


def oil_well(*args):
    """
    For doing the oil activity
    Args:
        *args: from the arg_parser

    Returns: None, loops forever (until Ctrl-C)

    """
    oil_args = args[0]
    if oil_args.level == 0 or oil_args.level == 1:
        hold_time = 4.5
    elif oil_args.level == 2 or oil_args.level == 3:
        # Harvest is 25% quicker from level 2 and up
        hold_time = (4.5/100) * 75
    else:
        raise EnvironmentError(f"{oil_args.level} is not a valid level for this skill")

    pyautogui.click(350, 1000)
    time.sleep(0.5)

    if oil_args.gasoline:
        pyautogui.moveTo(100, 1300)
        pyautogui.click()
        oil_loop(hold_time)
    elif oil_args.kerosene:
        pyautogui.moveTo(630, 1300)
        pyautogui.click()
        oil_loop(hold_time)
    elif oil_args.solar:
        pyautogui.moveTo(340, 1300)
        pyautogui.click()
        oil_loop(hold_time)


def no_op(*args) -> None:
    """
    Just called by argparser if no command is specified by the user

    Returns: EnvironmentError

    """
    raise EnvironmentError(f"Need to supply a command to run!  use --help for available commands")


def arg_parser(cmdline_args: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.set_defaults(func=no_op)
    subparsers = parser.add_subparsers()

    # Oil Parser
    oil_parser = subparsers.add_parser("oil")
    oil_parser.set_defaults(func=oil_well)
    oil_parser.add_argument("-l", "--level", type=int, default=0)
    oil_grp = oil_parser.add_mutually_exclusive_group(required=True)
    oil_grp.add_argument("-k", "--kerosene", action="store_true")
    oil_grp.add_argument("-g", "--gasoline", action="store_true")
    oil_grp.add_argument("-s", "--solar", action="store_true")

    # Fishing parser
    fishing_parser = subparsers.add_parser("fish")
    fishing_parser.set_defaults(func=fishing)

    # Mining Parser (it's the same as fishing key-wise so just call fishing function.
    mining_parser = subparsers.add_parser("mine")
    mining_parser.set_defaults(func=fishing)

    # Return the completed parser Namespace
    return parser.parse_args(cmdline_args)


if __name__ == "__main__":
    parsed_args = arg_parser(sys.argv[1:])
    parsed_args.func(parsed_args)
