from telethon.sync import TelegramClient, functions, types
from telethon.tl.functions.channels import GetChannelsRequest

import random

with TelegramClient('./assets/sessions/19734498126.session', 16623, "8c9dbfe58437d1739540f5d53c72ae4b") as client:
    groups = [
        "https://t.me/abakantop19",
        "https://t.me/abakanraboty",
        "https://t.me/avtorynok_abakana",
        "https://t.me/baraholka_abakan",
        "https://t.me/vapebaraxolkaabakan",
        "https://t.me/mining19club",
        "https://t.me/obyavleniyaabakan",
        "https://t.me/doska_obyavlenij_abakan",
        "https://t.me/neftyannik001",
        "https://t.me/azovkids",
        "https://t.me/the_wro",
        "https://t.me/azov_kupi",
        "https://t.me/azovbaraholka",
        "https://t.me/reklama161rus",
        "https://t.me/baraholkaazov",
        "https://t.me/baraholka_geroev",
        "https://t.me/baraholka_stolichka",
        "https://t.me/baraholkamoskvamo",
        "https://t.me/kids7_9_tashkent",
        "https://t.me/rasskazovo_detki",
        "https://t.me/obyavlenie_azov",
        "https://t.me/loverasskazovo",
        "https://t.me/baraholka_stomat_24",
        "https://t.me/elena111agarina",
        "https://t.me/kuplu_prodam_yashkino",
        "https://t.me/lgo_chat",
        "https://t.me/chat_gepatit",
        "https://t.me/azovskoepoberejieobyavlenie",
        "https://t.me/azov61rus",
        "https://t.me/obyavleniya_azov",
        "https://t.me/obyavlenie_piter",
        "https://t.me/schools_online",
        "https://t.me/rasskazovo2sale",
        "https://t.me/tb_petrol",
        "https://t.me/seowrite",
        "https://t.me/rasskazovochat",
        "https://t.me/chat_sanfrancisco_rusrek",
        "https://t.me/chat_sandiego_rusrek",
        "https://t.me/RussiansInGeorgia",
        "https://t.me/radioradostru",
        "https://t.me/miachat",
        "https://t.me/doska_obyavlenij_azov",
        "https://t.me/pirekchat",
        "https://t.me/reklama16region",
        "https://t.me/avitoalmet",
        "https://t.me/ocmru16almetyevsk",
        "https://t.me/baraholka_almetyevsk",
        "https://t.me/almet_baraholka",
        "https://t.me/almetyevskfleamarket",
        "https://t.me/kupiprodaialm",
        "https://t.me/kupi_almet",
        "https://t.me/almetyevskbazar",
        "https://t.me/obyavlenia_almetyevsk",
        "https://t.me/daromalmet",
        "https://t.me/spectechalmet",
        "https://t.me/vape_almet116chat",
        "https://t.me/talk_almetyevsk",
        "https://t.me/mining_hotel38",
        "https://t.me/ezh38chat",
        "https://t.me/buvape38",
        "https://t.me/bestpeopleonearth",
        "https://t.me/barahlo38",
        "https://t.me/baraholka_angarska",
        "https://t.me/shelechovprivockzalnyi",
        "https://t.me/irkvape",
        "https://t.me/mr_vape_baraxolka",
        "https://t.me/vaper38",
        "https://t.me/mama_club38",
        "https://t.me/angarskdobro",
        "https://t.me/ang038",
        "https://t.me/doska_obyavlenij_angarsk",
        "https://t.me/anhgerka",
        "https://t.me/detki_as",
        "https://t.me/anzherka_as",
        "https://t.me/arzamasov2",
        "https://t.me/shmot_baraxolka_arzamas",
        "https://t.me/vape_baraxolka_arzamas_dymohod",
        "https://t.me/baraxolkaarzamas",
        "https://t.me/vapearzamas",
        "https://t.me/avito_armavir",
        "https://t.me/armavir_baraholk",
        "https://t.me/armavir93",
        "https://t.me/Armavir_Reklama",
        "https://t.me/armavir_24",
        "https://t.me/barahollka_armavir",
        "https://t.me/baraholkaarm_nvk",
        "https://t.me/armanovo1",
        "https://t.me/kupi_armavir",
        "https://t.me/chamlykskaya",
        "https://t.me/armavirsell",
        "https://t.me/gorod_armavir",
        "https://t.me/vse_obyavleniya_armavir",
        "https://t.me/farpostArtem",
        "https://t.me/prodam_kyplyu_artemovsk_bahmut",
        "https://t.me/or7jdzthkto5mtcy",
        "https://t.me/otdam_darom_artem",
        "https://t.me/baraholkavapearh",
        "https://t.me/apx102",
        "https://t.me/arhangelsk_obyavleniya"
    ]

    valid_groups = ['https://t.me/abakantop19', 'https://t.me/abakanraboty', 'https://t.me/baraholka_abakan', 'https://t.me/vapebaraxolkaabakan', 'https://t.me/mining19club', 'https://t.me/obyavleniyaabakan', 'https://t.me/doska_obyavlenij_abakan', 'https://t.me/neftyannik001', 'https://t.me/azovkids', 'https://t.me/the_wro', 'https://t.me/azov_kupi', 'https://t.me/azovbaraholka', 'https://t.me/reklama161rus', 'https://t.me/baraholkaazov', 'https://t.me/baraholka_geroev', 'https://t.me/baraholkamoskvamo', 'https://t.me/kids7_9_tashkent', 'https://t.me/rasskazovo_detki', 'https://t.me/obyavlenie_azov', 'https://t.me/loverasskazovo', 'https://t.me/baraholka_stomat_24', 'https://t.me/elena111agarina', 'https://t.me/kuplu_prodam_yashkino', 'https://t.me/lgo_chat', 'https://t.me/chat_gepatit', 'https://t.me/azovskoepoberejieobyavlenie', 'https://t.me/azov61rus', 'https://t.me/obyavleniya_azov', 'https://t.me/obyavlenie_piter', 'https://t.me/schools_online', 'https://t.me/rasskazovo2sale', 'https://t.me/tb_petrol', 'https://t.me/seowrite', 'https://t.me/rasskazovochat', 'https://t.me/chat_sanfrancisco_rusrek', 'https://t.me/chat_sandiego_rusrek', 'https://t.me/RussiansInGeorgia', 'https://t.me/radioradostru', 'https://t.me/miachat', 'https://t.me/doska_obyavlenij_azov', 'https://t.me/pirekchat', 'https://t.me/reklama16region', 'https://t.me/avitoalmet', 'https://t.me/ocmru16almetyevsk', 'https://t.me/baraholka_almetyevsk', 'https://t.me/almet_baraholka', 'https://t.me/almetyevskfleamarket', 'https://t.me/kupiprodaialm', 'https://t.me/kupi_almet', 'https://t.me/almetyevskbazar', 'https://t.me/obyavlenia_almetyevsk', 'https://t.me/daromalmet', 'https://t.me/spectechalmet', 'https://t.me/vape_almet116chat', 'https://t.me/talk_almetyevsk', 'https://t.me/mining_hotel38', 'https://t.me/ezh38chat', 'https://t.me/buvape38', 'https://t.me/bestpeopleonearth', 'https://t.me/barahlo38', 'https://t.me/baraholka_angarska', 'https://t.me/irkvape', 'https://t.me/vaper38', 'https://t.me/mama_club38', 'https://t.me/angarskdobro', 'https://t.me/ang038', 'https://t.me/doska_obyavlenij_angarsk', 'https://t.me/anhgerka', 'https://t.me/detki_as', 'https://t.me/anzherka_as', 'https://t.me/arzamasov2', 'https://t.me/shmot_baraxolka_arzamas', 'https://t.me/baraxolkaarzamas', 'https://t.me/vapearzamas', 'https://t.me/avito_armavir', 'https://t.me/armavir_baraholk', 'https://t.me/armavir93', 'https://t.me/Armavir_Reklama', 'https://t.me/armavir_24', 'https://t.me/barahollka_armavir', 'https://t.me/baraholkaarm_nvk', 'https://t.me/armanovo1', 'https://t.me/armavirsell', 'https://t.me/gorod_armavir', 'https://t.me/vse_obyavleniya_armavir', 'https://t.me/farpostArtem', 'https://t.me/prodam_kyplyu_artemovsk_bahmut', 'https://t.me/or7jdzthkto5mtcy', 'https://t.me/otdam_darom_artem', 'https://t.me/baraholkavapearh', 'https://t.me/apx102', 'https://t.me/arhangelsk_obyavleniya']


    # for group in groups:
    #     try:
    #         result = client(GetChannelsRequest([
    #             group
    #         ]))

    #         valid_groups.append(group)
    #     except Exception as e:
    #         print(f"Группа не валидная пропускаем {e}")
    #         continue

    # print(valid_groups)
    # for channel in result.chats:
    #     print("Название канала:", channel.title)
    #     print("ID канала:", channel.id)
    #     print("Описание канала:", channel.about)
    #     print("-------------")


    folder_id = 95
    groups_entities = [client.get_input_entity(url) for url in valid_groups]

    print(folder_id)


    # folder = client(functions.messages.UpdateDialogFilterRequest(
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
    #             )
    #     ))

    folder_invite = client(functions.chatlists.ExportChatlistInviteRequest(
            chatlist=types.InputChatlistDialogFilter(
                filter_id=folder_id
            ),
            title=f'link_{folder_id}',
            peers=groups_entities
        ))

    folder_link = folder_invite.invite.url
    print(folder_link)
