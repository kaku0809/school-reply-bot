import os
from aiogram import Bot, Dispatcher, executor, types

TOKEN = os.getenv("8246939553:AAHDJ6oCOMYA6Fcojwiz_EMlN2hIvS5Bbpw")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["reply"])
async def reply_handler(message: types.Message):
    args = message.get_args()

    if not args:
        await message.reply("❗ Формат: /reply user_id текст ответа")
        return

    parts = args.split(maxsplit=1)
    if len(parts) < 2:
        await message.reply("❗ Формат: /reply user_id текст ответа")
        return

    user_id, answer = parts

    try:
        await bot.send_message(
            chat_id=int(user_id),
            text=f"📩 Ответ администрации:\n\n{answer}"
        )
        await message.reply("✅ Ответ отправлен пользователю")
    except Exception as e:
        await message.reply(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
