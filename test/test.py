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
    group = ["dasasdadsads", "https://t.me/mvlotrada", "https://t.me/baraholka_mlt", "https://t.me/murino_baraholka_devyatkino"]

    # for gro in group:
    #     print(gro)
    #     client(functions.channels.JoinChannelRequest(gro))

    client:TelegramClient

    groups_entities = [client.get_input_entity(
            url) for url in group]
    folder_id = random.randint(10, 99)

    folder_id = 20

    for gp in groups_entities:
        try:
            print(gp)
            gten = client.get_entity(gp)
            print(gten.admin_rights)
        except Exception as e:
            print(e)

    folder_invite = client(functions.chatlists.ExportChatlistInviteRequest(
            chatlist=types.InputChatlistDialogFilter(
                filter_id=folder_id
            ),
            title=f'link_{folder_id}',
            peers=groups_entities
        ))

    folder_link = folder_invite.invite.url
    print(folder_link)

    # print(groups_entities)

    # client(functions.messages.UpdateDialogFilterRequest(
    #         id=folder_id,
    #         filter=types.DialogFilter(
    #             id=folder_id,
    #             title=f'folder_{folder_id}',
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
    #     ))


    # print(folder_id)
    # client(functions.channels.JoinChannelRequest(group))
    # ent = client.get_entity(group)
    # print(ent)
