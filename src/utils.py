from datetime import datetime
from config_loader import get_config

config = get_config()

copyright_year = str(datetime.now().year)

def put_copyright(station_text):
    general_copyright = config['general']['COPYRIGHT']

    copyright_text = f"{general_copyright} {copyright_year}"

    return f"{station_text} {copyright_text}"

