import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = PROJECT_ROOT / ".env"

load_dotenv(dotenv_path=ENV_FILE)


@dataclass(frozen=True)
class Settings:
    bot_token: str


def get_settings() -> Settings:
    bot_token = os.getenv("BOT_TOKEN", "").strip()

    if not bot_token:
        raise ValueError(
            "BOT_TOKEN belum diisi. "
            "Silakan periksa file .env di root project."
        )

    return Settings(
        bot_token=bot_token,
    )
