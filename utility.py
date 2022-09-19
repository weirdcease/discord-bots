import os
from firebase_admin import credentials, initialize_app, db
import json
import nextcord
import dotenv

dotenv.load_dotenv()

FIREBASE_KEY = json.loads(os.getenv("FIREBASE_KEY"), strict=False)
DEBUG_WEBHOOK = os.getenv("DEBUG_WEBHOOK")

mains = [929931487279718490, 926776827589054484, 814158378653712455, 1011058430007578727] # REAL, STORAGE-1, big, Doge Den
moderated = [929931487279718490] # REAL
owner_guilds = [929931487279718490, 926776827589054484, 814158378653712455] # REAL, STORAGE-1, big
owners = {743340045628342324, 982116742815944764} # CAS, novemdecillion, 

cred = credentials.Certificate(FIREBASE_KEY)
initialize_app(cred, {
    'databaseURL': 'https://casbot-db-default-rtdb.firebaseio.com'
})

debug_webhook = nextcord.SyncWebhook.from_url(DEBUG_WEBHOOK)

status_types = {
    "online": nextcord.Status.online, 
    "dnd": nextcord.Status.dnd, 
    "idle": nextcord.Status.idle, 
    "invisible": nextcord.Status.invisible
}

activity_types = {
    "playing": nextcord.ActivityType.playing, 
    "streaming": nextcord.ActivityType.streaming, 
    "listening to": nextcord.ActivityType.listening, 
    "watching": nextcord.ActivityType.watching, 
    "competing in": nextcord.ActivityType.competing
}