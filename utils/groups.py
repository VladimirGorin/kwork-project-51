import json, time

groups_json_path = './assets/groups.json'

def update_groups(groups):
    try:
        time.sleep(2)

        data = []

        for group in groups:
            obj = {"group": group, "status": False}
            data.append(obj)

        with open(groups_json_path, 'w') as file:
            json.dump(data, file, indent=4)

        time.sleep(2)

    except Exception as e:
        print(f"Ошибка при попытке чтение группы: {e}")
        return None


def get_group_status(group_name):
    try:
        time.sleep(1)
        with open(groups_json_path, 'r') as file:
            data = json.load(file)
            for obj in data:
                if obj["group"] == group_name:
                    return obj["status"]

            return None
    except FileNotFoundError:
        print(f"Файл не найден")
        return None
    except Exception as e:
        print(f"Ошибка при попытке чтение статуса группы: {e}")
        return None

def set_group_status(group_name, new_status):
    try:
        time.sleep(1)
        with open(groups_json_path, 'r') as file:
            data = json.load(file)

        found = False
        for obj in data:
            if obj["group"] == group_name:
                obj["status"] = new_status
                found = True
                break

        if not found:
            print(f"Группа '{group_name}' не найдена в файле")
            return False

        with open(groups_json_path, 'w') as file:
            json.dump(data, file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Файл не найден")
        return None
    except Exception as e:
        print(f"Ошибка при попытке чтение статуса группы: {e}")
        return None
