from models import db
from sqlalchemy.orm import sessionmaker

def pega_sessao():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session 
    finally: # Usando o finally eu garanto que a sessão irá fechar independente do resultado (sucesso/ou não) da sessão
        session.close()