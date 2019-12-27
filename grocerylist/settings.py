import os

import toml

config_file = os.environ['APP_CONFIG']

with open(config_file) as f:
    config = toml.load(f)
