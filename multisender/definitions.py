from pathlib import Path

ROOT_DIR = Path(__file__).parent
LOG_DIR = Path(ROOT_DIR, "log")
SETTINGS_DIR = Path(ROOT_DIR, "settings")
PROVIDERS_TOML = Path(SETTINGS_DIR, "providers.toml")
SETTINGS_TOML = Path(SETTINGS_DIR, "settings.toml")
SECRETS_TOML = Path(SETTINGS_DIR, ".secrets.toml")
PUBLIC_KEYS_TXT = Path(SETTINGS_DIR, "public_keys.txt")
DOTENV_FILE = Path(SETTINGS_DIR, ".env")
