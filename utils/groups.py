import time

ignored_groups_txt_path = './assets/ignored_groups.txt'

def reset_ignored_groups():
    try:
        time.sleep(2)

        with open(ignored_groups_txt_path, 'w') as file:
            file.write("")

        time.sleep(2)

    except Exception as e:
        print(f"Ошибка при попытке записи групп: {e}")
        return None

def get_group_ignored_status(group_name):
    try:
        time.sleep(1)
        with open(ignored_groups_txt_path, 'r') as file:
            for line in file:
                if line.strip() == group_name:
                    return True
            return False
    except FileNotFoundError:
        print(f"Файл не найден")
        return None
    except Exception as e:
        print(f"Ошибка при попытке чтения статуса группы: {e}")
        return None

def set_group_ignor(group_name):
    try:
        with open(ignored_groups_txt_path, 'a') as file:
            file.write(f"\n{group_name}")

        return True

    except FileNotFoundError:
        print(f"Файл не найден")
        return None
    except Exception as e:
        print(f"Ошибка при попытке установки статуса группы: {e}")
        return None
