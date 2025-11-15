from fastapi import Depends, HTTPException
from models import db
from sqlalchemy.orm import sessionmaker, Session
from models import Usuario
from main import SECRET_KEY, ALGORITHM, oauth2_schema
from jose import jwt, JWTError

def pegar_sessao():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session 
    finally: # Usando o finally eu garanto que a sessão irá fechar independente do resultado (sucesso/ou não) da sessão
        session.close()




def verificar_token(token: str = Depends(oauth2_schema), session: Session = Depends(pegar_sessao)):
    #verificar se o token é valido
    try:        
        dic_info = jwt.decode(token, SECRET_KEY, ALGORITHM)
        id_usuario = int(dic_info.get("sub"))
    except JWTError:
        raise HTTPException(status_code=401, detail="Acesso Negado, verifique a validade do token")
    
    #extrair o ID do usuário do token
    usuario =  session.query(Usuario).filter(Usuario.id==id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Acesso Inválido")
    return usuario