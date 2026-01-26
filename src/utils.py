import os
from datetime import datetime
from config_loader import get_config

config = get_config()

copyright_year = str(datetime.now().year)

def check_env_vars():
    required_keys = ['SUPABASE_ID', 'SUPABASE_TOKEN']

    if not all(k in dict(os.environ).keys() for k in required_keys):
        print("Missing some environment var", file=sys.stderr)
        sys.exit(1)


def check_toml_config(config):
    required_keys = ['general', 'metadata', 'supabase', 'colors', 'stations']

    station_required_keys = [
        'name', 'client', 'network', 'location',
        'channel', 'amplification', 'text_station'
    ]

    if not all(k in config.keys() for k in required_keys):
        print("Missing some main config key", file=sys.stderr)
        sys.exit(1)

    for station in config['stations'].keys():
        if not all(k in config['stations'][station].keys() for k in station_required_keys):
            print(f"Missing some station {station} config key", file=sys.stderr)
            sys.exit(1)


def put_copyright(station_text):
    general_copyright = config['general']['COPYRIGHT']

    copyright_text = f"{general_copyright} {copyright_year}"

    return f"{station_text} {copyright_text}"


def get_image_metadata():
    return {
        'Author': config['metadata']['AUTHOR'],
        'Copyright': config['metadata']['COPYRIGHT'],
        'Software': 'auto-sismograma',
        'Disclaimer': config['metadata']['COPYRIGHT']
    }
