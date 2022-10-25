import os
import tcolors
from colorama import Back
from envparse import env

print(os.environ.get('LOGIN'))
env.read_envfile('options.env')
print(tcolors.Color.BLUE, tcolors.BgColor.YELLOW, os.environ.get('PASSWORD'))
print(Back.BLACK + os.environ.get('LOGIN'))
