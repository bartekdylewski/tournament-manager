import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Session cookie signing key. Override in production via the environment.
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-insecure-secret-change-me")

DATABASE_URL = os.environ.get(
    "DATABASE_URL", f"sqlite:///{(BASE_DIR / 'data' / 'tournament.db').as_posix()}"
)
