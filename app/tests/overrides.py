# app/tests/overrides.py
from fastapi import Depends
from fastapi_sso.sso.base import OpenID
from sqlalchemy.orm import Session

# ---- Dummy logged-in user override ----
def get_logged_user_override() -> OpenID:
    """Return a fake OpenID user to bypass real login."""
    return OpenID(
        id="123",
        email="john.doe@example.com",
        display_name="John Doe",
        provider="google",
    )

# ---- Dummy database session override ----
def get_db_override() -> Session:
    """Return a fake DB session to bypass real database connection."""
    class DummyDB:
        def close(self): ...
    yield DummyDB()
