# (c) @AM_ROBOTS

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 1216307744))
    API_HASH = os.environ.get("API_HASH", "eff30dac5504a8660e69bfe19f668571")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6657820331:AAFs5VD_70rOmWfQNmhVM8kyqrPWFLfj9oA")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "alltypmovie_bot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQFqmCIANdmkeorIKoFu0Y6C8w8NtrkIrWdOSdULGOq-3kxkvt3pEh8vFeMZhLQoQjBFBNt4YlWclZtBb39ozXQo76BegyxSd8OCvvxeArt51z8g2ozem4MQD3ckpL81gXTrYC8UP-CfcuDrfqVZXEhdEh5nMFTvyvPNIe0ojCvFSFsfdsf3nzoYDhyaQafh1Ik1SR9bIILmTe7Ix_c1galgkilUwqVvQT7fdC7vsm7sDgzKXeZWtbRb8_wGHPw2WnVrGf6mC-4WGAWMkv2i1FQubTWRnxiX1pBcQ3inAUnBRqqR4v3Qb0tODy74_XqfALKl1X0v7ASIrb-v2T8lU-UoJIatawAAAABIf2IgAA")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1001783989785))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    DATABASE_URL = os.environ.get("DATABASE_URL")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is all type movie bot.
    
    
    
🤖 My Name: <a href='https://t.me/netflixrequstgroup1>all type movie bot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

👨‍💻 Created By: <a href='https://t.me/netflix_india_007'>Ravi Barna</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer : <a href='https://t.me/netflix_india_007'>Ravi Barna</a></b>
"""
If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm all type movie bot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @netflix_india_007</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm all type movie bot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @netflix_india_007</a></b>
"""

