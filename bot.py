from pyrogram import Client, idle
#'‹ ٰ💸 ⇣ سورس الفراعنة ⇣ 💸 › .'#
from pyromod import listen



bot = Client(
    "mo",
    api_id=21627756,
    api_hash="fe77fbf0cae9f7f5ece37659e2466cf1",
    bot_token="7197234381:AAEYoNfw5En91ItaBhFcPRlN3zKevqhwgl0",#توكن المصنع
    plugins=dict(root="Mody")
    )

DEVS = ["UP_UO"] 


async def start_ahmedbot():
    print("تم تشغيل الصانع بنجاح..💗")
    #await bot.start()
    for hh in DEVS:
        try:
            await bot.send_message(hh, "**تم تشغيل الصانع بنجاح ...🥀**")
        except:
            pass
    await idle()
