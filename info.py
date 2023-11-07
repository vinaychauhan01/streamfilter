import re, sys, logging
from os import environ
from Script import script

logging.basicConfig(level=logging.ERROR)

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
API_ID = environ.get('API_ID', '21518327')
if len(API_ID) == 0:
    logging.error('API_ID is missing, exiting now')
    exit()
else:
    API_ID = int(API_ID)
API_HASH = environ.get('API_HASH', 'e72f588b3e4763f01eecfc3c4aa7e8ac')
if len(API_HASH) == 0:
    logging.error('API_HASH is missing, exiting now')
    exit()
BOT_TOKEN = environ.get('BOT_TOKEN', '6631914295:AAG4Eo1SsoB6bSR5nxaoknPiBY9ICHsEgu0')
if len(BOT_TOKEN) == 0:
    logging.error('BOT_TOKEN is missing, exiting now')
    exit()
PORT = int(environ.get('PORT', ''))

# Bot pics
PICS = (environ.get('PICS', 'https://telegra.ph/file/4ebd5576305bbfeb1cb25.jpg https://telegra.ph/file/9b7ec883efbe41c7cccbd.jpg https://telegra.ph/file/5483741c734210af56a1c.jpg https://telegra.ph/file/4204644e28f1d84460080.jpg https://telegra.ph/file/e46f1bb743506fb498071.jpg')).split()

# Bot Admins
ADMINS = environ.get('ADMINS', '5741918628')
if len(ADMINS) == 0:
    logging.error('ADMINS is missing, exiting now')
    exit()
else:
    ADMINS = [int(admins) for admins in ADMINS.split()]

# Channels
INDEX_CHANNELS = [int(index_channels) if index_channels.startswith("-") else index_channels for index_channels in environ.get('INDEX_CHANNELS', '-1001953164960').split()]
AUTH_CHANNEL = [int(auth_channels) for auth_channels in environ.get('AUTH_CHANNEL', '').split()]
LOG_CHANNEL = environ.get('LOG_CHANNEL', '-1001839965169')
if len(LOG_CHANNEL) == 0:
    logging.error('LOG_CHANNEL is missing, exiting now')
    exit()
else:
    LOG_CHANNEL = int(LOG_CHANNEL)
    
SUPPORT_GROUP = environ.get('SUPPORT_GROUP', '-1001901111266')
if len(SUPPORT_GROUP) == 0:
    logging.error('SUPPORT_GROUP is missing, exiting now')
    exit()
else:
    SUPPORT_GROUP = int(SUPPORT_GROUP)
    
OPENAI_API = environ.get('OPENAI_API', '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')
if len(OPENAI_API) == 0:
    logging.error('OPENAI_API is missing, exiting now')
    exit()

# MongoDB information
DATABASE_URL = environ.get('DATABASE_URL', "mongodb+srv://vinayjaat1:vinaych123@vinay2.hoiyhkt.mongodb.net/?retryWrites=true&w=majority")
if len(DATABASE_URL) == 0:
    logging.error('DATABASE_URL is missing, exiting now')
    exit()
DATABASE_NAME = environ.get('DATABASE_NAME', "vinay2")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Files')

# Links
SUPPORT_LINK = environ.get('SUPPORT_LINK', 'https://t.me/+jk6NurGlXA8wZDBl')
UPDATES_LINK = environ.get('UPDATES_LINK', 'https://t.me/+hhTGonwyLeQ5NGZl')

# Bot settings
AUTO_FILTER = is_enabled((environ.get('AUTO_FILTER', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SPELL_CHECK = is_enabled(environ.get("SPELL_CHECK", "True"), True)
SHORTLINK = is_enabled((environ.get('SHORTLINK', "False")), False)
DELETE_TIME = int(environ.get('DELETE_TIME', 3600)) # Add time in seconds
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "False")), False)
WELCOME = is_enabled((environ.get('WELCOME', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
LINK_MODE = is_enabled(environ.get("LINK_MODE", "True"), True)
CACHE_TIME = int(environ.get('CACHE_TIME', 300))

# Other
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
FILE_CAPTION = environ.get("FILE_CAPTION", script.FILE_CAPTION)
SHORTLINK_URL = environ.get("SHORTLINK_URL", "Vnshortener.com")
SHORTLINK_API = environ.get("SHORTLINK_API", "1ee9140a88d9813183e2af2870487c5eae50e285")
VERIFY_EXPIRE = int(environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = is_enabled(environ.get("IS_VERIFY", "False"), False)
WELCOME_TEXT = environ.get("WELCOME_TEXT", script.WELCOME_TEXT)
TUTORIAL = environ.get("TUTORIAL", "https://t.me/SL_Bots_Updates")
INDEX_EXTENSIONS = [extensions.lower() for extensions in environ.get('INDEX_EXTENSIONS', 'mp4 mkv').split()]

# stream features vars
BIN_CHANNEL = environ.get("BIN_CHANNEL", "-1001670122897")
if len(BIN_CHANNEL) == 0:
    logging.error('BIN_CHANNEL is missing, exiting now')
    exit()
else:
    BIN_CHANNEL = int(BIN_CHANNEL)
URL = environ.get("URL", "")
if len(URL) == 0:
    logging.error('URL is missing, exiting now')
    exit()
else:
    if URL.startswith('https://'):
        if not URL.endswith("/"):
            URL += '/'
    elif '.' in URL:
        URL = f'http://{URL}:{PORT}/'
    else:
        logging.error('URL is not valid, exiting now')
        exit()
