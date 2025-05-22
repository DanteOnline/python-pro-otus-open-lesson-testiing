import pytest
from app.models import Author
from app.database import AsyncSessionLocal


@pytest.mark.asyncio
async def test_get_authors(client):
    # Предварительно добавим автора в БД
    async with AsyncSessionLocal() as session:
        author = Author(name="Test Author", birthday_year=1990)
        session.add(author)
        await session.commit()

    response = await client.get("/authors")
    assert response.status_code == 200
    data = response.json()
    assert any(a["name"] == "Test Author" for a in data)
