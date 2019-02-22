import argparse
import subprocess
import sys

# read terminal width
columns = int(subprocess.check_output(['stty', 'size']).decode().split()[1])


# argparse
parser = argparse.ArgumentParser(description='Horizontal rule')

parser.add_argument('-c',
                    dest='color',  # argument name
                    type=str,
                    help='Character color')

parser.add_argument('-b',
                    dest='background',  # argument name
                    type=str,
                    help='Background color')

parser.add_argument('-s',
                    dest='string',  # argument name
                    type=str,
                    help='Character',
                    default='-')

args = parser.parse_args()


# take parameters from arguments
string = args.string
color = args.color
background = args.background


# colors
def frgnd(color=''):
    # foreground pallet
    pallete = {
        'black': '30',
        'red': '31',
        'green': '32',
        'yellow': '33',
        'blue': '34',
        'magenta': '35',
        'cyan': '36',
        'white': '37',
    }
    return pallete.get(color, '')


def bckgrnd(color=''):
    # background pallet
    pallete = {
        'black': '40',
        'red': '41',
        'green': '42',
        'yellow': '43',
        'blue': '44',
        'magenta': '45',
        'cyan': '46',
        'white': '47',
    }
    return pallete.get(color, '')


# create string
create_string = args.string * columns

colors = '0;' + frgnd(color) + ';' + bckgrnd(background)

print('\x1b[%sm%s\x1b[0m' % (colors, create_string[:columns]))
