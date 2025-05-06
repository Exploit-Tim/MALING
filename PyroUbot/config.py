import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "60"))

DEVS = list(map(int, os.getenv("DEVS", "5662169739").split()))

API_ID = int(os.getenv("API_ID", "27418440"))

API_HASH = os.getenv("API_HASH", "0a08a360e0e9f41b9896f655c300d09d")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7479639589:AAHKoviyiAbmiMB0wqTx-IPWVKyaQyUDPRM")

OWNER_ID = int(os.getenv("OWNER_ID", "5662169739"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Kinaya:KontolXD#123@kinaya.yuf2elr.mongodb.net/?retryWrites=true&w=majority&appName=Kinaya")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT","1"))

USER_GROUP = os.getenv("USER_GROUP", "@azellotesti")
