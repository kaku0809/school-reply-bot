import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message

TOKEN = os.getenv("8246939553:AAHDJ6oCOMYA6Fcojwiz_EMlN2hIvS5Bbpw")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def reply_handler(message: Message):
    if not message.text:
        return

    if message.text.startswith("/reply"):
        parts = message.text.split(maxsplit=2)

        if len(parts) < 3:
            await message.reply("❗ Формат: /reply user_id текст ответа")
            return

        user_id = parts[1]
        answer = parts[2]

        try:
            await bot.send_message(
                chat_id=int(user_id),
                text=f"📩 Ответ администрации:\n\n{answer}"
            )
            await message.reply("✅ Ответ отправлен")
        except Exception as e:
            await message.reply(f"❌ Ошибка: {e}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
