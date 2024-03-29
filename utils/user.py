from telethon.sync import TelegramClient
from telethon import functions, types, errors
from utils.statistics import update_stats
from utils.groups import get_group_ignored_status, set_group_ignor

import json, os, shutil, time, random

class User:
    def __init__(self, phone, sub_folder_count, post_bot_id, groups, folder_links, logger):

        self.error_status = False
        self.is_valid = True

        self.logger = logger

        self.sub_folder_count = sub_folder_count

        self.post_id = post_bot_id

        self.folder_links = folder_links

        self.folder_links_path = "./assets/data/folder_links.txt"

        self.phone = phone

        self.info_log("Начинаем работу.")

        self.invalid_sessions_folder_path = "./assets/invalid_sessions/"
        self.sessions_folder_path = "./assets/sessions"
        self.session = {
            "session_file_path": f"{self.sessions_folder_path}/{phone}.session",
            "json_file_path": f"{self.sessions_folder_path}/{phone}.json",
            "session_data":{}
        }

        self.groups = groups

        self.sub_groups = []

        self.get_session()
        if self.check_error(): return

    def info_log(self, message):
        message = f"[{self.phone}] {message}"
        print(message)
        self.logger.info(message)

    def error_log(self, message):
        message = f"[{self.phone}] {message}"
        print(message)
        self.logger.error(message)

        self.error_status = True

    def check_error(self):
        status = self.error_status

        if status:
            self.info_log("Завершаем работу для этого аккаунта")

            return status

    def del_invalid_session(self):

        files_to_move = [self.session["session_file_path"], self.session["json_file_path"]]
        try:

            for file in files_to_move:
                shutil.move(file, self.invalid_sessions_folder_path)
                # os.remove(file)

        except Exception as e:
            self.error_log("Ошибка при удаления сесси: {}".format(e))
            return

    def join_folder(self):
        try:
            self.client.connect()

            i = 0

            for folder in self.folder_links:
                if i < self.sub_folder_count:

                    i += 1

                    try:
                        folder_hash = folder.replace("https://t.me/addlist/", "")
                        result = self.client(functions.chatlists.CheckChatlistInviteRequest(slug=folder_hash))
                        if isinstance(result, types.chatlists.ChatlistInviteAlready):
                            self.info_log(f"Не удалось вступить папка уже добавлена в аккаунт: {folder}")
                        else:
                            self.info_log(f"Успешно зашел в папку: {folder}")

                            result = self.client(
                            functions.chatlists.JoinChatlistInviteRequest(slug=folder_hash, peers=result.peers))

                            self.set_stats(["joined_folders", 1])

                    except (errors.FloodWaitError, errors.FloodError) as e:
                        self.flood_wait(e)
                        continue

                    except Exception as e:
                        self.error_log("Ошибка при попытке зайти в папку, продолжаем: {}".format(e))
                        continue
                else:
                    self.info_log(f"Лимит вступление {self.sub_folder_count}:{i}")

                    break

            self.client.disconnect()
        except Exception as e:
            self.error_log("Ошибка при зайти в папку: {}".format(e))

    def set_stats(self, stat):
        # stat = ["sended_messages", 2]
        #stats[stat[0]] += stat[1]
        update_stats(stat[0], stat[1])

    def join_group(self, group):
        self.client(functions.channels.JoinChannelRequest(group))

    def send_post(self, entity, post_id):
        query = self.client.inline_query("@PostBot", post_id)
        message_id = query[0].click(entity).id

        time.sleep(2)

        message_status = self.client.get_messages(entity, ids=message_id)

        return message_status

    def create_folder(self):
        groups = self.sub_groups
        groups_entities = [self.client.get_input_entity(url) for url in groups]
        folder_id = random.randint(10, 99)


        folder = self.client(functions.messages.UpdateDialogFilterRequest(
            id=folder_id,
            filter=types.DialogFilter(
                id=folder_id,
                title=f'folder_{folder_id}',
                    pinned_peers=[],
                    include_peers=groups,
                    exclude_peers=[],
                    contacts=False,
                    non_contacts=False,
                    groups=False,
                    broadcasts=False,
                    bots=False,
                    exclude_muted=False,
                    exclude_read=False,
                    exclude_archived=False,
                    emoticon=''
                )
        ))

        folder_invite = self.client(functions.chatlists.ExportChatlistInviteRequest(
            chatlist=types.InputChatlistDialogFilter(
                filter_id=folder_id
            ),
            title=f'link_{folder_id}',
            peers=groups
        ))

        folder_link = folder_invite.invite.url

        self.add_folder_link(folder_link)
        self.set_stats(["created_folders", 1])

    def follow_groups(self):
        try:
            self.client.connect()

            t_joined = 0
            self.info_log(f"\n\nt-gived-groups:{len(self.groups)}\n\n")

            valid_groups = []

            self.info_log("Проверка групп на валидность")

            for group in self.groups:
                try:
                    self.client(functions.channels.GetChannelsRequest([group]))
                    self.info_log(f"Группа валидная: {group}")
                    valid_groups.append(group)

                except (errors.FloodWaitError, errors.FloodError) as e:
                    self.flood_wait(e)
                    pass

                except Exception as e:
                    self.info_log(f"Группа не валидна пропускаем: {e}")
                    continue

            if not valid_groups:
                raise Exception("Все группы недоступны. Невозможно создать папку.")

            self.info_log(f"Проверка валидации заверщена всего валидных групп из 100: {len(valid_groups)}")

            self.groups = valid_groups

            for group in self.groups:
                try:

                    group_ignored_status = get_group_ignored_status(group)

                    if group_ignored_status:
                        self.info_log(f"Пропускаем группу уже использовалась: {group}")
                        continue

                    ignored_status = set_group_ignor(group)

                    if not ignored_status:
                        self.info_log(f"Ошибка при попытке установки нового статуса пропускаем: {group}")
                        continue

                    self.join_group(group=group)

                    t_joined += 1

                    self.set_stats(["joined_groups", 1])
                    self.sub_groups.append(group)

                    self.info_log("Успешно зашли в группу: {}".format(group))



                except (errors.FloodWaitError, errors.FloodError) as e:
                    self.flood_wait(e)
                    continue

                except Exception as e:
                    self.set_stats(["not_joined_groups", 1])
                    self.info_log(f"Ошибка при попытке входа в группу ({group}) продолжаем работу: {e}")

                    continue

            self.info_log(f"\n\nT-joined: {t_joined}\n\n")
            try:

                if len(self.sub_groups) > 0:
                    self.create_folder()

                else:
                    self.info_log("Пропускаем создание папки так как групп для подписки меньше чем 0")

            except Exception as e:
                self.info_log("Ошибка при попытке создании папки: {}".format(e))

            self.client.disconnect()
        except Exception as e:
            self.error_log("Ошибка при попытке работы с группой: {}".format(e))
            return

    def flood_wait(self, error):
        seconds = error.seconds
        self.info_log(f"Ошибка спим {seconds} секунд : {error}")
        time.sleep(seconds)

    def send_messages(self):
        try:
            self.client.connect()

            for group in self.groups:
                try:
                    post_sended_status = self.send_post(entity=group, post_id=self.post_id)

                    if post_sended_status:
                        self.set_stats(["sended_messages", 1])
                        self.info_log("Успешно отправил сообщение в группу: {}".format(group))
                    else:
                        self.set_stats(["not_sended_messages", 1])
                        self.info_log("Не удалось отправить сообщение в группу: {}".format(group))

                except (errors.FloodWaitError, errors.FloodError) as e:
                    self.flood_wait(e)
                    continue

                except Exception as e:
                    self.set_stats(["not_sended_messages", 1])
                    self.info_log("Ошибка при попытке отправки сообщения продолжаем работу: {}".format(e))

            self.client.disconnect()
        except Exception as e:
            self.error_log("Ошибка при попытке работы с группой: {}".format(e))
            return


    # def start(self):
    #     try:
    #         self.client.connect()

    #         for group in self.groups:
    #             try:
    #                 self.join_group(group=group)

    #                 self.set_stats(["joined_groups", 1])
    #                 self.sub_groups.append(group)

    #                 self.info_log("Успешно зашли в группу: {}".format(group))

    #             except Exception as e:
    #                 self.set_stats(["not_joined_groups", 1])
    #                 self.info_log("Ошибка при попытке входа в группу продолжаем работу: {}".format(e))

    #             try:
    #                 post_sended_status = self.send_post(entity=group, post_id=self.post_id)

    #                 if post_sended_status:
    #                     self.set_stats(["sended_messages", 1])
    #                     self.info_log("Успешно отправил сообщение в группу: {}".format(group))
    #                 else:
    #                     self.set_stats(["not_sended_messages", 1])
    #                     self.info_log("Не удалось отправить сообщение в группу: {}".format(group))

    #             except Exception as e:
    #                 self.set_stats(["not_sended_messages", 1])
    #                 self.info_log("Ошибка при попытке отправки сообщения продолжаем работу: {}".format(e))

    #         try:

    #             if len(self.sub_groups) > 0:
    #                 self.create_folder()

    #             else:
    #                 self.info_log("Пропускаем создание папки так как групп для подписки меньше чем 0")

    #         except Exception as e:
    #             self.info_log("Ошибка при попытке создании папки: {}".format(e))

    #         self.client.disconnect()
    #     except Exception as e:
    #         self.error_log("Ошибка при попытке работы с группой: {}".format(e))
    #         return

    def add_folder_link(self, folder_link):

        try:
            with open(self.folder_links_path, "a", encoding="utf-8") as file:
                file.write(f"\n{folder_link}")

            self.info_log(f"Добавлена ссылка на группу: {folder_link}")

        except Exception as e:
            self.error_log("Ошибка при записать ссылку на папку: {}".format(e))
            return

    def files_exists(self, files):
        all_files_exist = all(os.path.exists(file_name) for file_name in files)

        return all_files_exist

    def get_session(self):


        try:
            files_exists = self.files_exists(files=[self.session["json_file_path"], self.session["session_file_path"]])

            if not files_exists:
                self.error_log("Ошибка не все файлы найдены")
                return

        except Exception as e:
            self.error_log("Ошибка при попытке проверки файлов на существование: {}".format(e))
            return

        try:
            with open("{}".format(self.session["json_file_path"]), "r", encoding="utf-8") as file:
                file_content = file.read()
                json_content = json.loads(file_content)

                self.session["session_data"] = json_content
        except Exception as e:
            self.error_log("Ошибка при попытке получение данных о сесси: {}".format(e))
            return

    def session_valid(self):
        try:
            self.is_valid = True

            session = self.session["session_file_path"]
            app_id = self.session["session_data"]["app_id"]
            app_id = self.session["session_data"]["app_id"]


            self.client = TelegramClient(session, app_id, app_id)
            self.client.connect()

            if not self.client.is_user_authorized():
                self.is_valid = False
                self.error_log("Аккаунт не валидный. Удалён.")
                self.set_stats(["invalid_sessions", 1])

                return

            self.info_log("Аккаунт валидный")
            self.set_stats(["valid_sessions", 1])

            self.client.disconnect()

        except Exception as e:
            self.is_valid = False
            self.error_log("Ошибка при попытке проверки валидации аккаунт не валидный: {}".format(e))
            return
