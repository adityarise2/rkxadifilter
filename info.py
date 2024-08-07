import re, logging
from os import environ
from Script import script

def is_enabled(type, value):
    data = environ.get(type, str(value))
    if data.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif data.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        print(f'Error - {type} is invalid, exiting now')
        exit()

def is_valid_ip(ip):
    ip_pattern = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    return re.match(ip_pattern, ip) is not None

# Bot information
API_ID = environ.get('API_ID', '28900444')  #api id of your telegram id
if len(API_ID) == 0:
    print('Error - API_ID is missing, exiting now')
    exit()
else:
    API_ID = int(API_ID)
API_HASH = environ.get('API_HASH', '7343be63958388e1d88c2961efe5a9e6') #api hash of your telegram id
if len(API_HASH) == 0:
    print('Error - API_HASH is missing, exiting now')
    exit()
BOT_TOKEN = environ.get('BOT_TOKEN', '6622811670:AAE72KucgGLfCRJ8ieKa8VVgtMqNaO0jFyk') #bot token from botfather
if len(BOT_TOKEN) == 0:
    print('Error - BOT_TOKEN is missing, exiting now')
    exit()
PORT = int(environ.get('PORT', '80')) #don't change anything 

# Bot pics
PICS = (environ.get('PICS', 'https://graph.org/file/1b75c537d954286006a0a.jpg https://graph.org/file/be1f6f6a6c5ace723bcaa.jpg
https://graph.org/file/2fa25721508a75b4c5022.jpg
https://graph.org/file/7c104cf23ea0bb906ccab.jpg
https://graph.org/file/73d5ab40b451c2263858d.jpg
https://graph.org/file/b06a7c81217ceac8745fa.jpg
https://graph.org/file/b298a69de146ee0193ad4.jpg
https://graph.org/file/3b888f732925d0b859e34.jpg
https://graph.org/file/34dc07c6473be09ce0fb1.jpg
https://graph.org/file/c65c31b06dffd6c5ea243.jpg
https://graph.org/file/14e985979638cbaf469b4.jpg
https://graph.org/file/529a78b24ec37048ef3c1.jpg
https://graph.org/file/6d57595c89db1b7f2f5b8.jpg
https://graph.org/file/c2a4bf44199a6281ddbba.jpg
https://graph.org/file/19922147ccfc8074a41c3.jpg
https://graph.org/file/12214f733de715f6a68e6.jpg
https://graph.org/file/64901de8c123c7bd3f44d.jpg
https://graph.org/file/f226ae236e7451579076b.jpg')).split()

# Bot Admins
ADMINS = environ.get('ADMINS', '5397893493') #apni tg id daalo
if len(ADMINS) == 0:
    print('Error - ADMINS is missing, exiting now')
    exit()
else:
    ADMINS = [int(admins) for admins in ADMINS.split()]

# Channels
INDEX_CHANNELS = [int(index_channels) if index_channels.startswith("-") else index_channels for index_channels in environ.get('INDEX_CHANNELS', '-1001648519555').split()]
if len(INDEX_CHANNELS) == 0:
    print('Info - INDEX_CHANNELS is empty')
AUTH_CHANNEL = [int(auth_channels) for auth_channels in environ.get('AUTH_CHANNEL', '-1001916993962').split()]
if len(AUTH_CHANNEL) == 0:
    print('Info - AUTH_CHANNEL is empty')
LOG_CHANNEL = environ.get('LOG_CHANNEL', '-1001899266690') #bot log channel -1005293546253
if len(LOG_CHANNEL) == 0:
    print('Error - LOG_CHANNEL is missing, exiting now')
    exit()
else:
    LOG_CHANNEL = int(LOG_CHANNEL)
IS_FSUB = is_enabled('IS_FSUB', True)

# support group
SUPPORT_GROUP = environ.get('SUPPORT_GROUP', '-1001914728318') #support group id ex:  -1002936246860
if len(SUPPORT_GROUP) == 0:
    print('Error - SUPPORT_GROUP is missing, exiting now')
    exit()
else:
    SUPPORT_GROUP = int(SUPPORT_GROUP)

# MongoDB information
DATABASE_URL = environ.get('DATABASE_URL', "mongodb+srv://ajnetwork1:ySypMfTFQpuoUEHk@cluster0.rk3tmfk.mongodb.net/?retryWrites=true&w=majority") #mongo db url
if len(DATABASE_URL) == 0:
    print('Error - DATABASE_URL is missing, exiting now')
    exit()
DATABASE_NAME = environ.get('DATABASE_NAME', "ajnetwork")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Files')

# Links
SUPPORT_LINK = environ.get('SUPPORT_LINK', 'https://t.me/+wzB-8NWd6vdhOTI1')
UPDATES_LINK = environ.get('UPDATES_LINK', 'https://t.me/ajcinemassofcl')
FILMS_LINK = environ.get('FILMS_LINK', 'https://t.me/RkMovie_group')
TUTORIAL = environ.get("TUTORIAL", "https://t.me/how_to_open_linkzz/13")
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/how_to_open_linkzz/13")

# Bot settings
DELETE_TIME = int(environ.get('DELETE_TIME', 3600)) # Add time in seconds 
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
MAX_BTN = int(environ.get('MAX_BTN', 10)) #don't change anything in Language 
LANGUAGES = [language.lower() for language in environ.get('LANGUAGES', 'english hindi telugu tamil kannada malayalam').split()]
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
FILE_CAPTION = environ.get("FILE_CAPTION", script.FILE_CAPTION)
SHORTLINK_URL = environ.get("SHORTLINK_URL", "publicearn.com")
SHORTLINK_API = environ.get("SHORTLINK_API", "74b308ea3b6b466a5116613403c051e12327485b")
VERIFY_EXPIRE = int(environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
WELCOME_TEXT = environ.get("WELCOME_TEXT", script.WELCOME_TEXT)
INDEX_EXTENSIONS = [extensions.lower() for extensions in environ.get('INDEX_EXTENSIONS', 'mp4 mkv').split()]
STICKERS_IDS = (
    "CAACAgUAAxkBAAED2UZms5qalePhwtwWl69xZxyZtdTj2AACMAwAApwpoFZ1r-Lrpn9OpB4E"
).split()

# boolean settings 
GROUP_FSUB = is_enabled('GROUP_FSUB', False) 
PM_SEARCH = is_enabled('PM_SEARCH', True) #switch True or False for searching results in bot pm😃
IS_VERIFY = is_enabled('IS_VERIFY', False)
AUTO_DELETE = is_enabled('AUTO_DELETE', False)
WELCOME = is_enabled('WELCOME', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
LONG_IMDB_DESCRIPTION = is_enabled("LONG_IMDB_DESCRIPTION", False)
LINK_MODE = is_enabled("LINK_MODE", True)
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
IMDB = is_enabled('IMDB', True)
SPELL_CHECK = is_enabled("SPELL_CHECK", True)
SHORTLINK = is_enabled('SHORTLINK', False)


PAYMENT_QR = environ.get('PAYMENT_QR', 'http://graph.org/file/cacbbea472e5a48ce0d64.jpg') #telegraph link of your QR code 
UPI_ID = environ.get('UPI_ID', 'Rishikesh-sharma09@axl') # Add your upi id here
# for stream
IS_STREAM = is_enabled('IS_STREAM', True) #true if you want stream feature active in your bot
BIN_CHANNEL = environ.get("BIN_CHANNEL", "") #if is_stream = true then add a channel id ex: -10026393639
if len(BIN_CHANNEL) == 0:
    print('Error - BIN_CHANNEL is missing, exiting now')
    exit()
else:
    BIN_CHANNEL = int(BIN_CHANNEL)
URL = environ.get("URL", "") #if heroku then paste the app link here ex: https://heroku......./
if len(URL) == 0:
    print('Error - URL is missing, exiting now')
    exit()
else:
    if URL.startswith(('https://', 'http://')):
        if not URL.endswith("/"):
            URL += '/'
    elif is_valid_ip(URL):
        URL = f'http://{URL}/'
    else:
        print('Error - URL is not valid, exiting now')
        exit()
