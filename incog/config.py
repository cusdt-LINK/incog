# Can be multiple prefixes, like this: ("!", "?")
BOT_PREFIX = ("!")
TOKEN = "YOUR BOT TOKEN GOES HERE"
APPLICATION_ID = "YOUR APP ID GOES HERE"
OWNERS = [YOUR OWNER ID GOES HERE]
BLACKLIST = []
 # Default cogs that I have created
STARTUP_COGS = [
    "cogs.cryptoticker" , "cogs.general", "cogs.help", "cogs.owner", "cogs.rpc",
]
BASE_CURRENCY = "usd"
URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids="
COIN_LIST = "https://api.coingecko.com/api/v3/coins/list"
SUPPORTED_CURRENCIES = "https://api.coingecko.com/api/v3/simple/supported_vs_currencies"
