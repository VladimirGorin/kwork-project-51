from telethon.sync import TelegramClient, functions, types, errors

import random
import time


def flood_wait(self, error):
    seconds = error.seconds
    self.info_log(f"Ошибка спим {seconds} секунд : {error}")
    time.sleep(seconds)


SESSION_PATH = './sessions/19784888551.session'
API_ID = 16623
API_HASH = "8c9dbfe58437d1739540f5d53c72ae4b"
FOLDER_ID = "folder_13"

with TelegramClient(SESSION_PATH, API_ID, API_HASH) as client:
    groups = ['https://t.me/almaty_otp', 'https://t.me/daromstrezhevoy', 'https://t.me/pangans', 'https://t.me/pangansales', 'https://t.me/pareniebrest_1', 'https://t.me/pattaya01', 'https://t.me/pattaya_1', 'https://t.me/pattayaj', 'https://t.me/ads_pattaya', 'https://t.me/tai_kuplu_prodam', 'https://t.me/pattayasale', 'https://t.me/permanent_01', 'https://t.me/irk4x4', 'https://t.me/mirrypch', 'https://t.me/pokachi_chat', 'https://t.me/kypiprodaiiii', 'https://t.me/poland_like', 'https://t.me/help_onemay', 'https://t.me/MMarino', 'https://t.me/poslugi_ua', 'https://t.me/privet_thai_store', 'https://t.me/prodaga_asic', 'https://t.me/kommunarkabaraholkadet', 'https://t.me/KommunarkaBaraholka', 'https://t.me/mentinao', 'https://t.me/phuket_baraxlanet', 'https://t.me/phuket2nd', 'https://t.me/phuketsell', 'https://t.me/pkhuketi', 'https://t.me/phuke_baraholka', 'https://t.me/kupi_proday_akadem', 'https://t.me/kupi_proday_eleven', 'https://t.me/zklubimovo2', 'https://t.me/euroklass_sale', 'https://t.me/RenaultZoeMarket', 'https://t.me/rostovnadonubaraholka', 'https://t.me/fishing25baraholka', 'https://t.me/rybalka_ru', 'https://t.me/rybaksale', 'https://t.me/baraholka_fishing', 'https://t.me/prokshino_biz', 'https://t.me/samuibaraholka', 'https://t.me/seishelu_360', 'https://t.me/adsserbia', 'https://t.me/slavnaya_baraholka_chat', 'https://t.me/sportivnaya_derevnya_baraxolka']
    valid_groups = []

    folders = client(functions.messages.GetDialogFiltersRequest())


    for folder in folders:
        try:
            folder_id = folder.id
            include_peers = folder.include_peers
            if folder_id == FOLDER_ID:
                break

        except Exception as e:
            print(e)

    folder_invite = client(functions.chatlists.ExportChatlistInviteRequest(
        chatlist=types.InputChatlistDialogFilter(
            filter_id=folder_id
        ),
        title=f'link_{folder_id}',
        peers=include_peers
    ))


    folder_link = folder_invite.invite.url
    print(folder_link)

    # for group in groups:
    #     try:
    #         client.send_message(group, ".")
    #         print(f"Группа валидная: {group}")
    #         valid_groups.append(group)

    #     except (errors.FloodWaitError, errors.FloodError) as e:
    #         flood_wait(e)
    #         pass

    #     except Exception as e:
    #         print(f"Группа не валидна пропускаем: {e}")
    #         continue

    # if not valid_groups:
    #     raise Exception("Все группы недоступны. Невозможно создать папку.")

    # print(valid_groups)

    # groups_entities = [client.get_input_entity(url) for url in valid_groups]
    # folder_id = random.randint(10, 99)

    # folder = client(functions.messages.UpdateDialogFilterRequest(
    #     id=folder_id,
    #     filter=types.DialogFilter(
    #         id=folder_id,
    #         title=f'folder_{folder_id}',
    #                 pinned_peers=[],
    #                 include_peers=groups_entities,
    #                 exclude_peers=[],
    #                 contacts=False,
    #                 non_contacts=False,
    #                 groups=False,
    #                 broadcasts=False,
    #                 bots=False,
    #                 exclude_muted=False,
    #                 exclude_read=False,
    #                 exclude_archived=False,
    #                 emoticon=''
    #                 )
    # ))

    # print(folder_id)

    # folder_invite = client(functions.chatlists.ExportChatlistInviteRequest(
    #     chatlist=types.InputChatlistDialogFilter(
    #         filter_id=folder_id
    #     ),
    #     title=f'link_{folder_id}',
    #     peers=groups_entities
    # ))

    # folder_link = folder_invite.invite.url

# with open("./groups.txt") as file:
#     lines = [line.strip() for line in file.readlines()]
#     print(lines)
