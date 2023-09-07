import configparser

# Create a configparser object
config = configparser.ConfigParser()

# Load the config.ini file
config.read('config.ini')

bot_token = config['API']['bot_token']