# tournament-manager

A simple tournament manager. An organizer creates a tournament, adds participants, starts it and enters results; anyone can browse brackets, standings and player profiles.

## Features

- Three formats: single elimination, round robin and Swiss (fixed rounds, or win/loss thresholds like LoL Worlds)
- Random or manual seeding, configurable scoring (presets: chess, football, LoL)
- Participants linked to accounts or plain names, teams with rosters
- User accounts, profiles with statistics, admin panel

## Stack

Python 3.12, FastAPI, SQLAlchemy, SQLite, Jinja2 + Bootstrap 5 (dark theme), uv, pytest.

## Running

```bash
uv sync
uv run dev    # server with autoreload
uv run test   # pytest (extra arguments are passed through)
```

App: http://127.0.0.1:8000, API docs (Swagger): http://127.0.0.1:8000/docs

## License

MIT
