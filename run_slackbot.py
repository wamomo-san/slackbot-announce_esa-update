# coding: utf-8

from slackbot.bot import Bot

from plugins.notify_updated_esa_io import notify_updated_esa

def main():
    notify_updated_esa()

if __name__ == "__main__":
    print("---- slack bot Start ----")
    main()
