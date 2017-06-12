#!/usr/bin/env python3

import os
from slackclient import SlackClient
from random import randint
import time

slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)
new_fortunes = ''
parsed_fortunes = []
n = 0

try:
    with open('fortunes', 'r') as f:
        temp_fortunes = f.read().split('%')
        for item in temp_fortunes:
            parsed_fortunes.append(item.split('%'))

    for item in parsed_fortunes:
        for a, b in enumerate(item):
            item[a] = b.replace('\n', ' '.lstrip(' '))

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
    print(e)
