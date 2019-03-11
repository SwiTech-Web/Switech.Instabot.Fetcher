from plugins.config import CONFIGURATION


def update_user_repository(rows):
    with open(CONFIGURATION.config['Target'], 'w', encoding='utf-8') as repository:
        repository.write("{},{},{}".format(rows[0], rows[1], rows[2]))
    return
