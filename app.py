import fastapi as fastapi
import sqlalchemy as sqlalchemy
import pydantic as pydantic

from fastapi import FastAPI
from sqlalchemy import create_engine, Column, String, Integer, Date, Text, ForeignKey, PrimaryKeyConstraint, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

app = FastAPI()

database_url = "postgresql+psycopg2://focoplus_6pmh_user:eMs126EpWdQTB2qxqamhFo5WIOtb7ovj@dpg-d8k0hc5dt1ts739e4ft0-a.oregon-postgres.render.com/focoplus_6pmh"

engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind=engine)
Base = declarative_base()

# modelagem

class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    senha = Column(String(8), nullable=False)
    nome = Column(String(100), nullable=False)
    numero = Column(String(13), nullable=False, unique=True)
    data_nascimento = Column(Date, nullable=False)
    neurodivergencia_id = Column(Integer, ForeignKey("neurodivergencia.id"), nullable=False)
    status = Column(String(100), nullable=False)
    objetivo = Column(Text, nullable=False)

class ModelUsuario(BaseModel):
    id: str
    email: str
    senha: str
    nome: str
    numero: str
    data_nascimento: str
    neurodivergencia_id: str
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
    materia_id = Column(Integer, ForeignKey("materia.id"), nullable=False)
    data_aula = Column(Date, nullable=False)
    conteudo = Column(Text, nullable=False)
    video = Column(Text, nullable=False)
    notes = Column(Text, nullable=False)
    empresa_id = Column(Integer, ForeignKey("empresa.id"), nullable=False)

class ModelAula(BaseModel):
    id: str
    titulo: str
    materia_id: str
    data_aula: str
    conteudo: str
    video: str
    notes: str
    empresa_id: str
    
    model_config = {"from_attributes": True}

class AulaUsuario(Base):
    __tablename__ = "aula_usuario"
    aluno_id = Column(Integer, ForeignKey("usuario.id"), primary_key =True, nullable=False)
    aula_id = Column(Integer, ForeignKey("aula.id"), primary_key =True, nullable=False)

class ModelAulaUsuario(BaseModel):
    aluno_id: str
    aula_id: str

    model_config = {"from_attributes": True}

class Anotacao(Base):
    __tablename__ = "anotacao"
    id = Column(Integer, primary_key = True, nullable=False)
    data_criacao = Column(DateTime, nullable=False)
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
    eixo_tematico = Column(String(40), nullable=False)
    aluno_id = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    escrita = Column(Text, nullable = False, unique=True)

class ModelRedacao(BaseModel):
    id: str
    tema: str
    eixo_tematico: str
    aluno_id: str
    escrita: str

    model_config = {"from_attributes": True}

class Simulado(Base):
    __tablename__ = "simulado"
    id = Column(Integer, primary_key = True, nullable=False)
    aula_id = Column(Integer, ForeignKey("aula.id"), nullable=False)
    exame = Column(Text, nullable = False)

class ModelSimulado(BaseModel):
    id: str
    aula_id: str
    exame: str

    model_config = {"from_attributes": True}

class Novidades(Base):
    __tablename__ = "novidades"
    id = Column(Integer, primary_key = True, nullable= False)
    noticias = Column(Text, nullable = False)

class ModelNovidades(BaseModel):
    id: str
    noticias: str

    model_config = {"from_attributes": True}

class Materia(Base):
    __tablename__ = "materia"
    id = Column(Integer, primary_key = True, nullable = False)
    area = Column(String(100), nullable = False, unique = True)

class ModelMateria(BaseModel):
    id: str
    area: str

    model_config = {"from_attributes": True}

class Revisao(Base):
    __tablename__ = "revisao"
    id = Column(Integer, primary_key = True, nullable = False)
    conteudo = Column(Text, nullable=False)
    aula_id = Column(Integer, ForeignKey("aula.id"), nullable = False)

class ModelRevisao(BaseModel):
    id: str
    conteudo: str
    aula_id: str

    model_config = {"from_attributes": True}

class Neurodivergencia(Base):
    __tablename__ = "neurodivergencia"
    id = Column(Integer, primary_key = True, nullable = False)
    neurodivergencia = Column(String, nullable = False)
    especificacao = Column(String)
    descricao = Column(Text, nullable = False)

class ModelNeurodivergencia(BaseModel):
    id: str
    neurodivergencia: str
    especificacao: str
    descricao: str
    
    model_config = {"from_attributes": True}

# Base.metadata.create_all(bind=engine)

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
    conexao.close()
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
    conexao.close()
    return{"aulas_usuarios": [ModelAulaUsuario.model_validate(au).dict for au in aulasusuarios]}

@app.get("/anotacao")
def listarAnotacoes():
    conexao = SessionLocal()
    anotacoes = conexao.query(Anotacao).all()
    conexao.close()
    return{"anotacoes": [ModelAnotacao.model_validate(an).dict for an in anotacoes]}

@app.get("/redacao")
def listarRedacoes():
    conexao = SessionLocal()
    redacoes = conexao.query(Redacao).all()
    conexao.close()
    return{"redacoes": [ModelRedacao.model_validate(r).dict for r in redacoes]}

@app.get("/simulado")
def listarSimulados():
    conexao = SessionLocal()
    simulados = conexao.query(Simulado).all()
    conexao.close()
    return{"simulados": [ModelSimulado.model_validade(s).dict for s in simulados]}

@app.get("/novidades")
def listarNovidades():
    conexao = SessionLocal()
    novidades = conexao.query(Novidades).all()
    conexao.close()
    return{"novidades": [ModelNovidades.model_validate(n).dict for n in novidades]}

@app.get("/materia")
def listarMaterias():
    conexao = SessionLocal()
    materias = conexao.query(Materia).all()
    conexao.close()
    return{"materias": [ModelMateria.model_validade(m).dict for m in materias]}

@app.get("/revisao")
def listarRevisoes():
    conexao = SessionLocal()
    revisoes = conexao.query(Revisao).all()
    conexao.close()
    return{"revisoes": [ModelRevisao.model_validate(re).dict for re in revisoes]}


@app.get("/neurodivergencia")
def listarNeurodivergencias():
    conexao = SessionLocal()
    neurodivergencias = conexao.query(Neurodivergencia).all()
    conexao.close()
    return{"neurodivergencias": [ModelRevisao.model_validate(d).dict for d in neurodivergencias]}

### Por ID

@app.get("/usuario/id")
def buscarUsuario(id: str):
    conexao = SessionLocal()
    u = conexao.query(Usuario).filter(Usuario.id == id).first()
    conexao.close()
    if u:
        return{"usuarios": ModelUsuario.model_validate(u).dict()}
    return {"mensagem": "Usuário não encontrado."}

@app.get("/empresa/id")
def buscarEmpresa(id: str):
    conexao = SessionLocal()
    e = conexao.query(Empresa).filter(Empresa.id==id).first()
    conexao.close()
    if e:
        return{"empresas": ModelEmpresa.model_validate(e).dict()}
    return {"mensagem": "Empresa não encontrada."}

@app.get("/aula/id")
def buscarAula(id: str):
    conexao = SessionLocal()
    a = conexao.query(Aula).filter(Aula.id == id).first()
    conexao.close()
    if a:
        return{"aulas": ModelUsuario.model_validate(a).dict()}
    return {"mensagem": "Aula não encontrada."}

# fazer: buscar conexão aluno-aula

@app.get("/alunoAula/id")
def buscaAlunoAula(aluno_id: str, aula_id: str):
    conexao = SessionLocal()
    us = conexao.query(AulaUsuario).filter(AulaUsuario.aluno_id == aluno_id).first()
    au = conexao.query(AulaUsuario).filter(AulaUsuario.aula_id == aula_id).first()
    conexao.close()
    if us and au:
        return{"alunosaulas": ModelAulaUsuario.model_validate(us, au).dict()}
    return{"mensagem": "O usuário não está registrado nesta aula."}


@app.get("/anotacao/id")
def buscarAnotacao(id: str):
    conexao = SessionLocal()
    an = conexao.query(Anotacao).filter(Anotacao.id==id).first()
    conexao.close()
    if an:
        return{"anotacoes": ModelAnotacao.model_validate(an).dict()}
    return {"mensagem": "Anotação não encontrada."}

@app.get("/redacao/id")
def buscarRedacao(id: str):
    conexao = SessionLocal()
    r = conexao.query(Redacao).filter(Redacao.id==id).first()
    conexao.close()
    if r:
        return{"redacoes": ModelRedacao.model_validate(r).dict()}
    return {"mensagem": "Redação não encontrada."}

@app.get("/simulado/id")
def buscarSimulado(id: str):
    conexao = SessionLocal()
    s = conexao.query(Simulado).filter(Simulado.id==id).first()
    conexao.close()
    if s:
        return{"simulados": ModelSimulado.model_validate(s).dict()}
    return {"mensagem": "Simulado não encontrado."}

@app.get("novidades/id")
def buscarNovidades(id: str):
    conexao = SessionLocal()
    n = conexao.query(Novidades).filter(Novidades.id==id).first()
    conexao.close()
    if n:
        return{"novidades": ModelNovidades.model_validate(n).dict()}
    return {"mensagem": "Notícia não encontrada."}

@app.get("materia/id")
def buscarMateria(id: str):
    conexao = SessionLocal()
    m = conexao.query(Materia).filter(Materia.id==id).first()
    conexao.close()
    if m:
        return{"materia": ModelMateria.model_validate(m).dict()}
    return {"mensagem": "Matéria não encontrada."}

@app.get("revisao/id")
def buscarRevisao(id: str):
    conexao = SessionLocal()
    r = conexao.query(Revisao).filter(Revisao.id==id).first()
    conexao.close()
    if r:
        return{"revisao": ModelRevisao.model_validate(r).dict()}
    return {"mensagem": "Revisão não encontrada."}


@app.get("neurodivergencia/id")
def buscarNeurodivergencia(id: str):
    conexao = SessionLocal()
    d = conexao.query(Neurodivergencia).filter(Neurodivergencia.id==id).first()
    conexao.close()
    if d:
        return{"neurodivergencia": ModelRevisao.model_validate(d).dict()}
    return {"mensagem": "Deficiência não encontrada."}

## Cadastro de Itens (métodos POST)

@app.post("/usuarioCadastro")
def criarUsuario(u: ModelUsuario):
    conexao = SessionLocal()
    novoUsuario = Usuario(**u.dict())
    conexao.add(novoUsuario)
    conexao.commit()
    conexao.refresh(novoUsuario)
    conexao.close()
    return {"mensagem": "Usuário cadastrado com sucesso!", "usuario": ModelUsuario.model_validate(novoUsuario).dict()}

@app.post("/empresaCadastro")
def criarEmpresa(e: ModelEmpresa):
    conexao = SessionLocal()
    novaEmpresa = Empresa(**e.dict())
    conexao.add(novaEmpresa)
    conexao.commit()
    conexao.refresh(novaEmpresa)
    conexao.close()
    return {"mensagem": "Empresa cadastrada com sucesso!", "empresa": ModelEmpresa.model_validate(novaEmpresa).dict()}

@app.post("/aulaCadastro")
def criarAula(a: ModelAula):
    conexao = SessionLocal()
    novaAula = Aula(**a.dict())
    conexao.add(novaAula)
    conexao.commit()
    conexao.refresh(novaAula)
    conexao.close()
    return {"mensagem": "Aula cadastrada com sucesso!", "aula": ModelAula.model_validate(novaAula).dict()}

@app.post("/aulausuarioCadastro")
def criarAulaUsuario(au: ModelAulaUsuario):
    conexao = SessionLocal()
    novaAulaUsuario = AulaUsuario(**au.dict())
    conexao.add(novaAulaUsuario)
    conexao.commit()
    conexao.refresh(novaAulaUsuario)
    conexao.close()
    return {"mensagem": "Conexão Aula-Usuário cadastrada com sucesso!", "aulausuario": ModelAulaUsuario.model_validate(novaAulaUsuario).dict()}

@app.post("/anotacaoCadastro")
def criarAnotacao(an: ModelAnotacao):
    conexao = SessionLocal()
    novaAnotacao = Anotacao(**an.dict())
    conexao.add(novaAnotacao)
    conexao.commit()
    conexao.refresh(novaAnotacao)
    conexao.close()
    return {"mensagem": "Anotação cadastrada com sucesso!", "anotacao": ModelAnotacao.model_validate(novaAnotacao).dict()}

# fazer: novidades, materia, revisao

@app.post("/redacaoCadastro")
def criarRedacao(r: ModelRedacao):
    conexao = SessionLocal()
    novaRedacao = Redacao(**r.dict())
    conexao.add(novaRedacao)
    conexao.commit()
    conexao.refresh(novaRedacao)
    conexao.close()
    return {"mensagem": "Redação cadastrada com sucesso!", "redacao": ModelRedacao.model_validate(novaRedacao).dict()}

@app.post("/simuladoCadastro")
def criarSimulado(s: ModelSimulado):
    conexao = SessionLocal()
    novoSimulado = Simulado(**s.dict())
    conexao.add(novoSimulado)
    conexao.commit()
    conexao.refresh(novoSimulado)
    conexao.close()
    return {"mensagem": "Simulado cadastrado com sucesso!", "simulado": ModelSimulado.model_validate(novoSimulado).dict()}



@app.post("/neurodivergenciaCadastro")
def criarNeurodivergencia(d: ModelNeurodivergencia):
    conexao = SessionLocal()
    novaNeurodivergencia = Neurodivergencia(**d.dict())
    conexao.add(novaNeurodivergencia)
    conexao.commit()
    conexao.refresh(novaNeurodivergencia)
    conexao.close()
    return {"mensagem": "Neurodivergencia cadastrada com sucesso!", "neurodivergencia": ModelNeurodivergencia.model_validate(novaNeurodivergencia).dict()}

### Login
@app.get("/login")
def login(email: str, senha: str):
    conexao = SessionLocal()
    e = conexao.query(Usuario).filter(Usuario.email == email).first()
    s = conexao.query(Usuario).filter(Usuario.senha == senha).first()
    conexao.close()
    if e and s:
        return{"mensagem": "Login realizado com sucesso!"}
    return{"mensagem": "E-mail ou senha incorretos. Tente novamente."}

### Filtros
@app.get("/filtrarAulasMateria")
def filtroAula(materia_id: str):
    conexao = SessionLocal()
    m = conexao.query(Aula).filter(Aula.materia_id == materia_id).first()
    conexao.close()
    if m:
        return{"aulas": ModelAula.model_validate(m).dict()}

@app.get("/filtrarAulasEmpresa")
def filtroEmpresa(empresa_id: str):
    conexao = SessionLocal()
    e = conexao.query(Aula).filter(Aula.empresa_id == empresa_id).first()
    conexao.close()
    if e:
        return{"aulas": ModelAula.model_validate(e).dict()}

@app.get("/filtrarAulasData")
def filtroData(data_aula: str):
    conexao = SessionLocal()
    d = conexao.query(Aula).filter(Aula.data_aula == data_aula).first()
    conexao.close()
    if d:
        return{"aulas": ModelAula.model_validate(d).dict()}

@app.get("/aulaPesquisar")
def pesquisarAula(titulo: str):
    conexao = SessionLocal()
    t = input()
    ti = t.split(" ")
    tt = conexao.query(Aula).filter((t2 in ti) in Aula.titulo).first()
    conexao.close()
    if tt:
        return{"aulas": ModelAula.model_validate(tt).dict()}
