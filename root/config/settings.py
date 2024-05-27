# settings.py (Python)

import os

# Discord API token
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Moderation settings
FILTER_THRESHOLD = 0.8
WARNING_THRESHOLD = 3
MUTE_THRESHOLD = 5
BAN_THRESHOLD = 10

# Logging settings
LOGGING_LEVEL = 'INFO'