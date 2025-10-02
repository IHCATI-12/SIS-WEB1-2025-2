# definir a conexao com o banco e a sessao (porta de entrada para executar consultas)
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {}
)

@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connetcion, _):
    cursor = dbapi_connetcion.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)