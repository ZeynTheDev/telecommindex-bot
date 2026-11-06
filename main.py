import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from app.config import Settings, get_settings
from app.handlers.start import router as start_router


async def run_bot(settings: Settings) -> None:
    dispatcher = Dispatcher()

    dispatcher.include_router(start_router)

    async with Bot(token=settings.bot_token) as bot:
        bot_info = await bot.get_me()

        bot_identity = (
            f"@{bot_info.username}"
            if bot_info.username
            else str(bot_info.id)
        )

        logging.info("Authenticated as %s", bot_identity)

        await bot.set_my_commands(
            [
                BotCommand(
                    command="start",
                    description="Mulai menggunakan bot",
                ),
                BotCommand(
                    command="help",
                    description="Tampilkan bantuan",
                ),
            ]
        )

        logging.info("Bot is starting with long polling.")

        await dispatcher.start_polling(
            bot,
            close_bot_session=False,
        )


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    try:
        settings = get_settings()
    except ValueError as error:
        raise SystemExit(f"Configuration error: {error}") from error

    try:
        asyncio.run(run_bot(settings))
    except KeyboardInterrupt:
        logging.info("Bot stopped by user.")


if __name__ == "__main__":
    main()
