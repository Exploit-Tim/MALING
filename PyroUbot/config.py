import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "60"))

DEVS = list(map(int, os.getenv("DEVS", "1332083384").split()))

API_ID = int(os.getenv("API_ID", "26143381"))

API_HASH = os.getenv("API_HASH", "56620ed86f5aaf3b0f584ae69f869a14")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8088363847:AAETl3JJSy92K5bihG6wY_y8xOoIc_QzAIA")

OWNER_ID = int(os.getenv("OWNER_ID", "1332083384"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://ubotKuzu:KuzurokenBaku234@bakuzaan.qsum4.mongodb.net/?retryWrites=true&w=majority&appName=bakuzaan")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT","-1002457551830"))

USER_GROUP = os.getenv("USER_GROUP", "@xwinkels")
