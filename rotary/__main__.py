import argparse
import roter

DESCRIPTION = """
This is a simple cut-up generator tool to build new English language
lines.
"""



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("-i", nargs='?',
                        default='rotary/data/inputs.txt',
                        help="directory of ")

    args = parser.parse_args()
    rot = roter.Roter(args.i)
