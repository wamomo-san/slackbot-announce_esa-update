# slackbot-announce_esa-update

# Overview
[esa.io](https://k3webtech.esa.io/) の更新があると定時に教えてくれる slackbot

# Description
毎週日曜の 21:00( 予定 ) になると登録してある esa.io の記事の更新の有無を取得し、slack の特定のチャンネルに対して通知するシステム。使用言語は Python3。slackbot 自体は Heroku 上で稼働。

### Directry
```
slackbot-announce_esa/
    ├ const/
    |    └ messages_esa_io.py
    ├ plugins/
    |    ├ __init__.py
    |    └ notify_updated_esa_io.py 
    ├ private/
    |    ├ api_token_esa.py
    |    └ api_token_slack.py
    ├ src/ 
    |    └ esa_io.py 
    |
    └ run.slackbot.py
```
### Requirement
```
slackbot-announce_esa/
     └ private/
         ├ api_token_esa.py
         └ api_token_slack.py
```
