from configparser import ConfigParser

#Read config.ini file
def get_config():
    config = ConfigParser()
    config.read('config.txt')

    my_config = {
        'path': config.get('PATH', 'path'),
        'sla': config.get('SLA', 'sla'),
        'path_key': config.get('GGS', 'path_key'),
        'ggs_url': config.get('GGS', 'ggs_url'),
        'ggs_name': config.get('GGS', 'ggs_name'),
        'all_files': config.get('MODE', 'all_files'),

    }
    return my_config

