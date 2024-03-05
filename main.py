import install

from utils.user import User

from clear_screen import clear
from utils.statistics import get_stats_message, clear_stats

from multiprocessing import Pool

import logging, sys, os

class Main():
    def __init__(self):
        self.logger = self.initialize_logger()

        self.max_workers = 3

        self.main_menu = [{"title": "[1] Проверка на валидность", "value": 1}, {"title": "[2] Подписка на группы и создание папок", "value": 2}, {"title": "[3] Подписка на папки", "value": 3}, {"title": "[4] Рассылка", "value": 4}]
        self.main_menu_titles = '\n'.join(item["title"] for item in self.main_menu)
        self.main_menu_values = [item["value"] for item in self.main_menu]
        self.menu_choices = {
            1: self.validation_sessions,
            2: self.follow_groups,
            3: self.join_to_folders,
            4: self.send_messages
        }

        clear_stats()
        self.start()

    def info_log(self, message):
        print(message)

    def error_log(self, message):
        print(message)
        input("\nНажмите ENTER что бы закрыть консоль.")
        sys.exit(1)

    def stats_log(self):

        self.info_log(get_stats_message())
        self.logger.info(get_stats_message())

    def read_file(self, path):
        with open(path, 'r', encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

        return lines

    def get_data(self):
        try:
            self.groups = self.read_file("./assets/data/groups.txt")
            self.folder_links = self.read_file("./assets/data/folder_links.txt")
            self.post_id = self.read_file("./assets/data/post_id.txt")[0]
            self.sub_folder_count = int(self.read_file("./assets/data/sub_count.txt")[0])
            self.sessions = self.get_session("./assets/sessions/")

        except Exception as e:
            self.error_log(f"Ошибка при чтение данных: {e}")

    def get_session(self, directory):
        files_set = set()
        for filename in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, filename)):
                name_without_extension = os.path.splitext(filename)[0]
                files_set.add(name_without_extension)
        return list(files_set)

    def execute_task(self, task_function):
        with Pool(processes=self.max_workers) as pool:
            pool.starmap(self.run_task, [(phone, task_function) for phone in self.sessions])

        pool.close()
        pool.join()

        self.info_log("Все потоки завершили выполнение.")

    def run_task(self, phone, task):
        task(phone)

        # try:
        #     session = User(phone=phone, sub_folder_count=self.sub_folder_count, post_bot_id=self.post_id, groups=self.groups[:100], folder_links=self.folder_links, logger=self.logger)
        #     session.session_valid()

        #     session.client.connect()

        #     session.client.send_message("Hesoyamijs", "Привет мир")
        # except Exception as e:
        #     print(e)
        #     return


    def join_to_folders(self, phone):
        try:
            session = User(phone=phone, sub_folder_count=self.sub_folder_count, post_bot_id=self.post_id, groups=self.groups[:100], folder_links=self.folder_links, logger=self.logger)
            if session.check_error(): return

            session.session_valid()
            if session.check_error(): return
            if not session.is_valid: return



            session.join_folder()
            if session.check_error(): return
        except Exception as e:
            self.info_log(f"[{phone}] Ошибка оброботке сесси: {e}")

    def send_messages(self, phone):

        try:
                session = User(phone=phone, sub_folder_count=self.sub_folder_count, post_bot_id=self.post_id, groups=self.groups[:100], folder_links=self.folder_links, logger=self.logger)

                if session.check_error(): return
                session.session_valid()

                if session.check_error(): return
                if not session.is_valid: return

                self.groups = self.groups[100:]

                session.send_messages()
                if session.check_error(): return

        except Exception as e:
            self.info_log(f"[{phone}] Ошибка оброботке сесси: {e}")

    def validation_sessions(self, phone):
        try:
                session = User(phone=phone, sub_folder_count=self.sub_folder_count, post_bot_id=self.post_id, groups=self.groups[:100], folder_links=self.folder_links, logger=self.logger)

                if session.check_error(): return
                session.session_valid()

                if session.check_error():
                    session.del_invalid_session()

        except Exception as e:
            self.info_log(f"[{phone}] Ошибка оброботке сесси: {e}")

    def follow_groups(self, phone):
        try:
                session = User(phone=phone, sub_folder_count=self.sub_folder_count, post_bot_id=self.post_id, groups=self.groups[:100], folder_links=self.folder_links, logger=self.logger)


                if session.check_error(): return
                session.session_valid()

                if session.check_error(): return
                if not session.is_valid: return

                self.groups = self.groups[100:]

                session.follow_groups()
                if session.check_error(): return

        except Exception as e:
            self.info_log(f"[{phone}] Ошибка оброботке сесси: {e}")

    def start(self):
        self.info_log(f"Введите нужный номер\n\n{self.main_menu_titles}\n\n")

        try:
            main_menu_choice = int(input("Номер: "))
            if not main_menu_choice in self.main_menu_values:
                self.error_log("Номер не найден!")
        except ValueError:
            self.error_log("Введите число!")

        clear()
        self.get_data()

        if main_menu_choice in self.menu_choices:
            self.execute_task(self.menu_choices[main_menu_choice])
        else:
            self.error_log("Неверный выбор меню.")

        # if main_menu_choice == 1:
        #     self.validation_sessions()
        # elif main_menu_choice == 2:
        #     self.follow_groups()
        # elif main_menu_choice == 3:
        #     self.join_to_folders()
        # elif main_menu_choice == 4:
        #     self.send_messages()



        try:
            self.stats_log()
        except Exception as e:
            self.error_log(f"Не удалось отправить статистику: {e}")

    def initialize_logger(self):
        logger = logging.getLogger("GLOBAL")
        logger.setLevel(logging.DEBUG)

        log_file = './assets/logs/main.log'
        file_handler = logging.FileHandler(filename=log_file, encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        return logger

try:
    if __name__ == "__main__":
        Main()

except KeyboardInterrupt:
    input("\nНажмите ENTER что бы закрыть консоль.")
    sys.exit(1)

input("\nНажмите ENTER что бы закрыть консоль.")
