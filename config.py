import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "24054192")) #optional
API_HASH = getenv("API_HASH", "ed9a8a61a1b4a1ad0915cbe87ba490ed") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "@MAD1BOY").split()))
OWNER_ID = int(getenv("OWNER_ID" "5901320319"))
MONGO_URL = getenv("MONGO_URL" "mongodb+srv://madpanel:madboy11@atlascluster.gprqayn.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster")
BOT_TOKEN = getenv("BOT_TOKEN", "8030899275:AAFOT2-RGOX3FrM5Gztpss0JMCrk6OKr0mY")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3c52a01057865f7511168.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER" "@MAD1BOY")
LOG_GROUP = getenv("LOG_GROUP" "-1002295296865")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
