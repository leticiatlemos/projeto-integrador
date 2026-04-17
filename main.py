from fastapi import FastAPI
from sqlalchemy import create_engine, Column, String, Integer, LocalDate, Text, ForeignKey, PrimaryKeyConstraint, LocalDateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

app = FastAPI()

database_url = x

engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind=engine)
Base = declarative_base

# modelagem

class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    senha = Column(String(8), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    nome = Column(String(100), nullable=False)
    data_nascimento = Column(LocalDate, nullable=False)
    genero = Column(String(50), nullable=False)
    neurodivergencia = Column(String(100), nullable=False)
    status = Column(String(100), nullable=False)
    objetivo = Column(Text, nullable=False)

class ModelUsuario(BaseModel):
    id: str
    email: str
    senha: str
    cpf: str
    nome: str
    data_nascimento: str
    genero: str
    neurodivergencia: str
    status: str
    objetivo: str

    model_config = {"from_attributes": True}

class Empresa(Base):
    __tablename__ = "empresa"
    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String(80), nullable=False)

class ModelEmpresa(BaseModel):
    id: str
    nome: str

    model_config = {"from_attributes": True}

class Aula(Base):
    __tablename__ = "aula"
    id = Column(Integer, primary_key=True, nullable=False)
    titulo = Column(String(100), nullable=False)
    materia = Column(String(100), nullable=False)
    data_aula = Column(LocalDate, nullable=False)
    video = Column(Text, nullable=False)
    notes = Column(Text, nullable=False)
    empresa_id = Column(Integer, ForeignKey("empresa.id"), nullable=False)

class ModelAula(BaseModel):
    id: str
    titulo: str
    materia: str
    data_aula: str
    video: str
    notes: str
    empresa_id: str

    model_config = {"from_attributes": True}

class AulaUsuario(Base):
    __tablename__ = "aula_usuario"
    usuario_id = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    aula_id = Column(Integer, ForeignKey("aula.id"), nullable=False)
    PrimaryKeyConstraint("usuario_id", "aula_id", name="aula_usuario_pk")

class ModelAulaUsuario(BaseModel):
    usuario_id: str
    aula_id: str

    model_config = {"from_attributes": True}

class Anotacao(Base):
    __tablename__ = "anotacao"
    id = Column(Integer, primary_key = True, nullable=False)
    data_criacao = Column(LocalDateTime, nullable=False)
    conteudo = Column(Text, nullable=False)
    aula_id = Column(Integer, ForeignKey("aula.id"), nullable=False)

class ModelAnotacao(BaseModel):
    id: str
    data_criacao: str
    conteudo: str
    aula_id: str

    model_config = {"from_attributes": True}

class Redacao(Base):
    __tablename__ = "redacao"
    id = Column(Integer, primary_key = True, nullable=False)
    tema = Column(String(100), nullable=False)
    aluno = Column(String(100), nullable=False)
    escrita = Column(Text, nullable = False, unique=True)

class ModelRedacao(BaseModel):
    id: str
    tema: str
    aluno: str
    escrita: str

    model_config = {"from_attributes": True}

class Simulado(Base):
    __tablename__ = "simulado"
    id = Column(Integer, primary_key = True, nullable=False)
    exame = Column(Text, nullable = False)

class ModelSimulado(BaseModel):
    id: str
    exame: str

    model_config = {"from_attributes": True}

class NovidadesEnem(Base):
    __tablename__ = "novidadesenem"
    id = Column(Integer, primary_key = True, nullable= False)
    noticias = Column(Text, nullable = False)

class ModelNovidadesEnem(BaseModel):
    id: str
    noticias: str

    model_config = {"from_attributes"}

class Materia(Base):
    __tablename__ = "materia"
    id = Column(Integer, primary_key = True, nullable = False)
    titulo = Column(String(100), nullable = False, unique = True)
    simulado_id = Column(Integer, ForeignKey("simulado.id"), nullable = False)

class ModelMateria(BaseModel):
    id = str
    titulo = str
    simulado_id = str

    model_config = {"from_attributes": True}

class Cn(Base):
    __tablename__ = "CN"
    id = Column(Integer, primary_key = True, nullable=False)
    conteudocn = Column(Text, nullable=False)
    materia_id = Column(Integer, ForeignKey("materia.id", nullable=False))

class ModelCn(BaseModel):
    id: str
    conteudocn: str
    materia_id: str

    model_config = {"from_attributes": True}

class Ch(Base):
    __tablename__ = "Ch"
    id = Column(Integer, primary_key = True, nullable=False)
    conteudoch = Column(Text, nullable=False)
    materia_id = Column(Integer, ForeignKey("materia.id", nullable=False))

class ModelCh(BaseModel):
    id: str
    conteudoch: str
    materia_id: str

    model_config = {"from_attributes": True}

class Mat(Base):
    __tablename__ = "mat"
    id = Column(Integer, primary_key = True, nullable=False)
    conteudomat = Column(Text, nullable=False)
    materia_id = Column(Integer, ForeignKey("materia.id", nullable=False))

class ModelMat(BaseModel):
    id: str
    conteudomat: str
    materia_id: str

    model_config = {"from_attributes": True}

class LP(Base):
    __tablename__ = "Lp"
    id = Column(Integer, primary_key = True, nullable=False)
    conteudolp = Column(Text, nullable=False)
    materia_id = Column(Integer, ForeignKey("materia.id", nullable=False))

class ModelLP(BaseModel):
    id: str
    conteudolp: str
    materia_id: str

    model_config = {"from_attributes": True}

class Revisao(Base):
    __tablename__ = "revisao"
    id = Column(Integer, primary_key = True, nullable = False)
    conteud = Column(Text, nullable=False)
    aula_id = Column(Integer, ForeignKey("aula.id"), nullable = False)

# métodos
## Listagem de Itens (métodos GET)

### Geral

@app.get("/usuario")
def listarUsuarios():
    conexao = SessionLocal()
    usuarios = conexao.query(Usuario).all()
    conexao.close()
    return{"usuarios": [ModelUsuario.model_validate(u).dict() for u in usuarios]}

@app.get("/empresa")
def listarEmpresas():
    conexao = SessionLocal()
    empresas = conexao.query(Empresa).all()
    conexao.close
    return{"empresas": [ModelEmpresa.model_validate(e).dict() for e in empresas]}

@app.get("/aula")
def listarAulas():
    conexao = SessionLocal()
    aulas = conexao.query(Aula).all()
    conexao.close
    return{"aulas": [ModelAula.model_validate(a).dict() for a in aulas]}

@app.get("/aulas_usuarios")
def listarAulaUsuarios():
    conexao = SessionLocal()
    aulasusuarios = conexao.query(AulaUsuario).all()
    conexao.close
    return{"aulas_usuarios": [ModelAulaUsuario.model_validate(au).dict for au in aulasusuarios]}

@app.get("anotacao")
def listarAnotacoes():
    conexao = SessionLocal()
    anotacoes = conexao.query(Anotacao).all()
    conexao.close
    return{"anotacoes": [ModelAnotacao.model_validate(an).dict for an in anotacoes]}

# fazer: redacao, simulado, novidadesenem, materia, cn, ch, mat, lp, revisao

### Por ID

@app.get("/usuario/id")
def buscarUsuario(id: str):
    conexao = SessionLocal()
    u = conexao.query(Usuario).filter(Usuario.id == id).first()
    conexao.close
    if u:
        return{"usuarios": ModelUsuario.model_validate(u).dict()}
    return {"mensagem": "Usuário não encontrado."}

@app.get("/empresa/id")
def buscarEmpresa(id: str):
    conexao = SessionLocal()
    e = conexao.query(Empresa).filter(Empresa.id==id).first()
    conexao.close
    if e:
        return{"empresas": ModelEmpresa.model_validate(e).dict()}
    return {"mensagem": "Empresa não encontrada."}

@app.get("/aula/id")
def buscarAula(id: str):
    conexao = SessionLocal()
    a = conexao.query(Aula).filter(Aula.id == id).first()
    conexao.close
    if a:
        return{"aulas": ModelUsuario.model_validate(a).dict()}
    return {"mensagem": "Aula não encontrada."}

# fazer: buscar conexão aluno-aula

@app.get("/anotacao")
def buscarAnotacao(id = str):
    conexao = SessionLocal()
    an = conexao.query(Anotacao).filter(Anotacao.id==id).first()
    conexao.close
    if an:
        return{"anotacoes": ModelAnotacao.model_validate(an).dict}
    return {"mensagem": "Anotação não encontrada."}

# fazer: redacao, simulado, novidadesenem, materia, cn, ch, mat, lp, revisao

## Cadastro de Itens (métodos POST)

@app.post("/usuario")
def criarUsuario(u: ModelUsuario):
    conexao = SessionLocal()
    novoUsuario = Usuario(**u.dict())
    conexao.add(novoUsuario)
    conexao.commit()
    conexao.refresh(novoUsuario)
    conexao.close()
    return {"mensagem": "Usuário cadastrado com sucesso!", "usuario": ModelUsuario.model_validate(novoUsuario).dict()}

@app.post("/empresa")
def criarEmpresa(e: ModelEmpresa):
    conexao = SessionLocal()
    novaEmpresa = Empresa(**e.dict())
    conexao.add(novaEmpresa)
    conexao.commit()
    conexao.refresh(novaEmpresa)
    conexao.close()
    return {"mensagem": "Empresa cadastrada com sucesso!", "empresa": ModelEmpresa.model_validate(novaEmpresa).dict()}

@app.post("/aula")
def criarAula(a: ModelAula):
    conexao = SessionLocal()
    novaAula = Aula(**a.dict())
    conexao.add(novaAula)
    conexao.commit()
    conexao.refresh(novaAula)
    conexao.close()
    return {"mensagem": "Aula cadastrada com sucesso!", "aula": ModelAula.model_validate(novaAula).dict()}

@app.post("/aulausuario")
def criarAulaUsuario(au: ModelAulaUsuario):
    conexao = SessionLocal()
    novaAulaUsuario = AulaUsuario(**au.dict())
    conexao.add(novaAulaUsuario)
    conexao.commit()
    conexao.refresh(novaAulaUsuario)
    conexao.close()
    return {"mensagem": "Conexão Aula-Usuário cadastrada com sucesso!", "aulausuario": ModelAulaUsuario.model_validate(novaAulaUsuario).dict()}

@app.post("/aulausuario")
def criarAulaUsuario(an: ModelAnotacao):
    conexao = SessionLocal()
    novaAnotacao = Anotacao(**an.dict())
    conexao.add(novaAnotacao)
    conexao.commit()
    conexao.refresh(novaAnotacao)
    conexao.close()
    return {"mensagem": "Anotação cadastrada com sucesso!", "anotacao": ModelAnotacao.model_validate(novaAnotacao).dict()}

# fazer: redacao, simulado, novidadesenem, materia, cn, ch, mat, lp, revisao
