# stats_deafult = {
#     "not_sended_messages": 0,
#     "sended_messages": 0,
#     "joined_groups": 0,
#     "not_joined_groups": 0,
#     "created_folders": 0,
#     "joined_folders": 0,
#     "valid_sessions": 0,
#     "invalid_sessions": 0,
# }


import json

stats_json_path = './assets/statistics.json'

def clear_stats():
    try:
        with open(stats_json_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("File not found.")
        return

    for key in data:
        data[key] = 0

    with open(stats_json_path, 'w') as file:
        json.dump(data, file, indent=4)

def update_stats(key, value):
    try:
        with open(stats_json_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {
            "not_sended_messages": 0,
            "sended_messages": 0,
            "joined_groups": 0,
            "not_joined_groups": 0,
            "created_folders": 0,
            "joined_folders": 0,
            "valid_sessions": 0,
            "invalid_sessions": 0
        }

    if key in data:
        data[key] += value
    else:
        print("Ключ не найден в json")

    with open(stats_json_path, 'w') as file:
        json.dump(data, file, indent=4)

def read_stats():
    try:
        with open(stats_json_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Файл не найден")
        return None

def get_stats_message():
    stats = read_stats()

    stats_message = f'''\nОтправлено всего сообщений: {stats.get("sended_messages")}
    \nНЕ отправлено сообщений всего: {stats.get("not_sended_messages")}
    \n\nЗашли в группу всего: {stats.get("joined_groups")}
    \nНЕ смогли зайти в группы всего: {stats.get("not_joined_groups")}
    \n\nСоздано папок всего: {stats.get("created_folders")}
    \nВсего зашли в папки: {stats.get("joined_folders")}
    \nВсего валидных сессий: {stats.get("valid_sessions")}
    \nВсего не валидных сессий: {stats.get("invalid_sessions")}
    '''

    return stats_message
