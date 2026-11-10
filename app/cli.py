"""Shortcuts exposed as `uv run dev` and `uv run test`."""
import sys

import pytest
import uvicorn


def dev() -> None:
    uvicorn.run("app.main:app", reload=True)


def test() -> None:
    sys.exit(pytest.main(sys.argv[1:]))
