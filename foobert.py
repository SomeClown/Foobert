#!/usr/bin/env python3

import os
from slackclient import SlackClient
from random import randint
import time
import click
import json

__author__ = "SomeClown"
__license__ = "MIT"
__maintainer__ = "Teren Bryson"
__email__ = "teren@packetqueue.net"


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
EPILOG = 'Have a fun time throwing foo\'s at bars'

slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

color_black2 = "\033[1;30m{0}\033[00m"
color_red2_on = "\033[01;31m"
color_red2_off = "\33[00m"
color_green2 = "\033[1;32m{0}\033[00m"
color_yellow2 = "\033[1;33m{0}\033[00m"
color_blue2 = "\033[1;34m{0}\033[00m"
color_purple2 = "\033[1;35m{0}\033[00m"
color_cyan2 = "\033[1;36m{0}\033[00m"
color_white2 = "\033[1;37m{0}\033[00m"


@click.group(epilog=EPILOG, context_settings=CONTEXT_SETTINGS)
def cli():
    """
    Quick and dirty proof of concept. Randomly sends text from file to a slack channel
    :return: 
    """
    pass


@click.command(options_metavar='[spam file]', short_help='Spam a foo')
@click.argument('spam_file', metavar=['file'])
def fortune_spam(spam_file):
    """
    The much vaunted 'spam' option. #KeepCalmAndSpamOn
    :param spam_file: 
    :return: 
    """

    parsed_fortunes = []
    n = 0
    try:
        with open(spam_file, 'r') as f:
            temp_fortunes = f.read().split('%')
            for item in temp_fortunes:
                parsed_fortunes.append(item.split('%'))

        for item in parsed_fortunes:
            for a, b in enumerate(item):
                item[a] = b.replace('\n', ' ')

        while n <= len(parsed_fortunes) - 1:
            rand_timer = randint(600, 1800)
            rand_item = randint(0, len(parsed_fortunes) - 1)
            message = ''.join(parsed_fortunes[rand_item])
            sc.api_call(
                "chat.postMessage",
                channel="#general",
                text=message
            )
            print(message)
            n += n
            time.sleep(rand_timer)
    except BaseException as e:
        print('Not sure what shit the bed, but the shit looks like this:')
        print(color_red2_on + str(e) + color_red2_off)


@click.command(options_metavar='[no options]', short_help='return a list of channels')
def retrieve_channel():
    foo = sc.api_call(
        "channels.list"
    )
    channels = foo['channels']
    for item in channels:
        print(color_red2_on + item['name'] + color_red2_off + ': ' + item['purpose']['value'])

cli.add_command(fortune_spam, 'spam')
cli.add_command(retrieve_channel, 'channels')

if __name__ == '__main__':
    try:
        cli()
    except TypeError as err:
        print('Not sure what shit the bed (you probably fucked up), but the error is below:')
        print(color_red2_on + str(err) + color_red2_off)
