import toml

_config = None

def get_config():
    global _config
    if _config is None:
        _config = toml.load('config.toml')
    return _config
