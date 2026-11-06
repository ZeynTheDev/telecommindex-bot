from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message


router = Router(name="start")


@router.message(CommandStart())
async def command_start(message: Message) -> None:
    first_name = (
        message.from_user.first_name
        if message.from_user
        else "teman"
    )

    await message.answer(
        f"Halo, {first_name}! 👋\n\n"
        "Selamat datang di Community Index Bot.\n\n"
        "Bot ini dirancang untuk membantu komunitas "
        "mengelola katalog, indeks resource, dan pengajuan "
        "dari para anggotanya.\n\n"
        "Saat ini bot masih dalam tahap pengembangan.\n\n"
        "Gunakan /help untuk melihat perintah yang tersedia."
    )


@router.message(Command("help"))
async def command_help(message: Message) -> None:
    await message.answer(
        "📚 BANTUAN COMMUNITY INDEX BOT\n\n"
        "Perintah yang tersedia:\n\n"
        "/start - Memulai penggunaan bot\n"
        "/help - Menampilkan panduan penggunaan\n\n"
        "Fitur katalog, pencarian, dan pengajuan "
        "akan ditambahkan pada tahap pengembangan berikutnya."
    )
