from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")

# DB conditionals
DB_URI = env.str('DB_URI')
HOST = env.str('HOST')
DATABASE = env.str('DATABASE')
USER = env.str('USER')
PASSWORD = env.str('PASSWORD')