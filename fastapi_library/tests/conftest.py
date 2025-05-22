import json
import os
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from app.models import Base
from app.database import engine, AsyncSessionLocal
from main import app


@pytest_asyncio.fixture
async def client():
    async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac


@pytest_asyncio.fixture(scope="session", autouse=True)
async def prepare_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture
async def session():
    async with AsyncSessionLocal() as current_session:
        yield current_session


@pytest_asyncio.fixture
def author_data():
    filepath = os.path.join("tests", "data", "author.json")
    with open(filepath, encoding='utf-8') as f:
        return json.load(f)
