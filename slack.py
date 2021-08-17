#!/usr/bin/python3

import os.path
import os
import datetime
from tabulate import tabulate
from argparse import ArgumentParser
import warnings
from warnings import warn as warning

parser = ArgumentParser()
parser.add_argument( '-m', '--message', dest='message', default=None, help='Message')
parser.add_argument( '-c', '--channel', dest='channel', default=None, help='Channel to message')
results = parser.parse_args()

# read secrets. assumes file exists in ~/.SLACK_SECRETS
from pathlib import Path
file = str(Path.home()) + os.sep + '.SLACK_SECRETS'
exec(open(file).read())

if results.channel == 'icaoberg':
	url = CHANNEL_ICAOBERG
elif results.channel == 'bil-dev':
	url = CHANNEL_BIL_DEV
elif results.channel == 'bil-all':
	url = CHANNEL_BIL_ALL
else:
	print('Unknown channel name. Exiting method.')
	exit()

command = 'curl -X POST -H \'Content-type: application/json\' --data \'{"text":"' + results.message + '"}\' ' + url
os.system(command)
exit()
