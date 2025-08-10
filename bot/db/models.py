from bot.db.database import Base 
from sqlalchemy.orm import Mapped, mapped_column

class News(Base):
    __tablename__ = "news"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] 
    link: Mapped[str] 
    description: Mapped[str]
    is_sent: Mapped[bool] = mapped_column(default=False)

class Sources(Base):
    __tablename__ = "sources"

    id: Mapped[int] = mapped_column(primary_key=True)
    link: Mapped[str] 
    
