import pytest
from async_factory_boy.factory.sqlalchemy import AsyncSQLAlchemyFactory
from app.models import Author



@pytest.mark.asyncio
async def test_str_native(session, author_data):
    author = Author(**author_data)
    session.add(author)
    await session.commit()
    assert str(author) == f"{author_data['name']}: {author_data['birthday_year']}"


@pytest.mark.asyncio
async def test_str_factory(session, author_data):

    class AuthorFactory(AsyncSQLAlchemyFactory):
        class Meta:
            model = Author
            sqlalchemy_session = session

    author = await AuthorFactory.create(**author_data)
    assert str(author) == f"{author_data['name']}: {author_data['birthday_year']}"
