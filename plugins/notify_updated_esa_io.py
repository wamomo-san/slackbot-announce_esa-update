from slacker import Slacker

import re
import os, sys
sys.path.append(os.pardir)

from src import esa_io
from const.messages_esa_io import UPDATED_ESA, NO_UPDATED, DETAIL_UPDATED_ESA
from private.api_token_slack import API_TOKEN_SLACK

def notify_updated_esa():
    esa = esa_io.Esa()
    updated_articles = esa.checkEsa()

    slack = Slacker(API_TOKEN_SLACK)

    slack_channel = "announce"

    if (updated_articles == None):
        slack.chat.post_message(slack_channel, NO_UPDATED, as_user=True)
    else:
        slack.chat.post_message(slack_channel, UPDATED_ESA, as_user=True)
        for article in updated_articles:
            splited_date = re.split('[T+:]', article['updated_at'])
            updated_date = splited_date[0] + " " + splited_date[1] + ":" + splited_date[2]
            slack.chat.post_message(
                slack_channel, 
                DETAIL_UPDATED_ESA.format(
                article['name'],
                article['created_by']['screen_name'],
                updated_date,
                article['url']
            ), as_user=True)
