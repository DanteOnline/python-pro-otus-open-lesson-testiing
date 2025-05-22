# main.py

from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.database import AsyncSessionLocal
from app.models import Author

app = FastAPI()

async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session


@app.get("/authors")
async def get_authors(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Author))
    authors = result.scalars().all()
    return [{"id": a.id, "name": a.name, "birthday_year": a.birthday_year} for a in authors]
