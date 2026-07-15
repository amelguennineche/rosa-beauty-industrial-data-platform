from src.database import get_engine


engine = get_engine()


with engine.connect() as connection:
    print("Connexion PostgreSQL réussie")