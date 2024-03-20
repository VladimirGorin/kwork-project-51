from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetChannelsRequest


with TelegramClient('./assets/sessions/19733622857.session', 16623, "8c9dbfe58437d1739540f5d53c72ae4b") as client:
    groups = [
        "https://t.me/obyavlenia_samara",
        "https://t.me/baraholka1631",
        "https://t.me/Samara_objavleniya",
        "https://t.me/samaraob",
        "https://t.me/samara_bazar",
        "https://t.me/zarabotok_samara_vakansii",
        "https://t.me/samara_bazarchat",
        "https://t.me/ocmru64samara",
        "https://t.me/samara_iphone",
        "https://t.me/samara_doska",
        "https://t.me/samara_ads_house",
        "https://t.me/lsgser",
        "https://t.me/ob_i_rabota_samara",
        "https://t.me/samara_kupi",
        "https://t.me/samarau_rulya",
        "https://t.me/doskasamara",
        "https://t.me/velosamara_flood",
        "https://t.me/talk_samara",
        "https://t.me/doska_obyavleniy_samara",
        "https://t.me/ev_market_spb",
        "https://t.me/saltcloud_corporation_baraholka",
        "https://t.me/arenda_Piter_Sdam",
        "https://t.me/ads_spb1",
        "https://t.me/spb_chatf",
        "https://t.me/piter_stock",
        "https://t.me/spb_baraxolka",
        "https://t.me/baraholka_spb",
        "https://t.me/baraholkaspbnum1",
        "https://t.me/bo78ru",
        "https://t.me/spb_chat_ru",
        "https://t.me/bezrealtora_chat",
        "https://t.me/birja_truda_spb",
        "https://t.me/baraholka_vape_spb",
        "https://t.me/vape_chat_spb",
        "https://t.me/vapebarahspb",
        "https://t.me/m6vhqlwp3ce3mdy6",
        "https://t.me/baraxolka_otdam_darom_spb",
        "https://t.me/gruzchiki_peterburg",
        "https://t.me/indispbnewfaces2",
        "https://t.me/baracholkadetispb",
        "https://t.me/kyplu_prodam_na_neve",
        "https://t.me/garagesalecivi",
        "https://t.me/doska_spb_vip",
        "https://t.me/psk_start",
        "https://t.me/untolov",
        "https://t.me/rabota_orenburg_chat",
        "https://t.me/baraholkasaintpeterburg",
        "https://t.me/indispbnewfaces",
        "https://t.me/uter_nashol",
        "https://t.me/komnedpiter",
        "https://t.me/piterburglek",
        "https://t.me/medsharing_spb",
        "https://t.me/crypto_piter_exchange",
        "https://t.me/rastenia_spb",
        "https://t.me/obyavlenia_piter",
        "https://t.me/baraholkasppb",
        "https://t.me/baraholka178",
        "https://t.me/spbavito",
        "https://t.me/baraholkario",
        "https://t.me/Piterads",
        "https://t.me/kuplyu_prodam_piter",
        "https://t.me/sale_78",
        "https://t.me/lift9898",
        "https://t.me/darompiterburg",
        "https://t.me/restojobspb2",
        "https://t.me/spbdogs",
        "https://t.me/pokospb",
        "https://t.me/radio_spb",
        "https://t.me/radio_spb_rynok",
        "https://t.me/spb_reklama_24",
        "https://t.me/nalichman_spb_chat",
        "https://t.me/sanktpeterburgrabotabaraholka",
        "https://t.me/billboard_spb",
        "https://t.me/metroparnas",
        "https://t.me/spb99909",
        "https://t.me/zayavki_shalandi_trali_spb",
        "https://t.me/indispbnewfaces8",
        "https://t.me/doska_obyavlenij_sankt_peterburg",
        "https://t.me/businessnedvigimosty",
        "https://t.me/zimaleto_objavlenia",
        "https://t.me/vape_saransk13ruuus",
        "https://t.me/alpha_vape_shop",
        "https://t.me/vapesaransk",
        "https://t.me/vapebarahol",
        "https://t.me/saransk13rus2022",
        "https://t.me/rynok_penza_saransk",
        "https://t.me/baraholka_penza_saransk",
        "https://t.me/saransk_baraholka",
        "https://t.me/vapesaranck",
        "https://t.me/vape13",
        "https://t.me/moto_saransk",
        "https://t.me/saransk_obyavleniya",
        "https://t.me/objavleniyasaransk",
        "https://t.me/tabasaran_chat",
        "https://t.me/doska_obyavlenij_saransk",
        "https://t.me/ozon_saratov_seller",
        "https://t.me/vape_obmen",
        "https://t.me/vape164",
        "https://t.me/changevape64",
        "https://t.me/baraholkavapesaratov",
        "https://t.me/baraholkasaratov1"
    ]

    valid_groups = []

    for group in groups:
        try:
            result = client(GetChannelsRequest([
                group
            ]))

            valid_groups.append(group)
        except Exception as e:
            print(f"Группа не валидная пропускаем {e}")
            continue

    print(valid_groups)
    # for channel in result.chats:
    #     print("Название канала:", channel.title)
    #     print("ID канала:", channel.id)
    #     print("Описание канала:", channel.about)
    #     print("-------------")
