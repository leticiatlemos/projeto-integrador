create database focoplus7;

create table usuario(
   id serial primary key,
   email varchar(100) not null unique,
   senha char(8) not null,
   nome varchar(100) not null,
   numero char(13) not null,
   data_nascimento date not null,
   objetivo text not null
);

create table neurodivergencia(
	id serial primary key,	
	neurodivergencia varchar (50),
	especificacao varchar (50),
	descricao text
);

create table empresa(
   id serial primary key,
   nome varchar (80) not null
);

create table materia (
	id serial primary key,
	area varchar (100) not null unique
);

create table aula(
   id serial primary key,
   titulo varchar(100) not null,
   data_aula date not null,
   video text not null,
   notes text not null,
   empresa_id int not null,
   foreign key (empresa_id) references empresa(id),
   materia_id int not null,
   foreign key (materia_id) references materia(id)
);


create table aula_usuario(
   primary key (usuario_id, aula_id),
   aula_id int not null,
   foreign key (aula_id) references aula(id),
   usuario_id int not null,
   foreign key (usuario_id) references usuario(id)
);


create table anotacao(
   id serial primary key,
   data_criacao timestamp not null,
   conteudo text not null,
   aula_id int not null,
   foreign key (aula_id) references aula(id)
);



create table redacao (
	id serial primary key,
	tema varchar (100) not null,
	eixo_tematico varchar (40) not null,
	escrita text not null unique,
	usuario_id int not null,
	foreign key (usuario_id) references usuario(id) 
);

create table simulado (
	id serial primary key,
	exame text not null,
	aula_id int not null,
	foreign key (aula_id) references aula(id)
);

create table novidades (
	id serial primary key ,
	noticias text not null
);

create table revisao(
	id serial primary key,
	conteudo text not null, 
	aula_id int not null,
	foreign key (aula_id) references aula(id) 
);

insert into usuario (email, senha, nome, numero, data_nascimento, objetivo)
values ('usuario@gmail.com', '1234', 'Fulano', '5524999999999', '2009-02-02', 'Passar em medicina');

alter table usuario
add neurodivergencia_id int;

alter table usuario 
add foreign key (neurodivergencia_id) references neurodivergencia(id);

alter table aula 
add conteudo text not null;

alter table revisao
drop column conteudo;

insert into neurodivergencia (neurodivergencia, especificacao, descricao)
values ('Autismo', 'Nível 1', 'Hiperfoco em dinossauros')

select *
from usuario
where id = 2;

SELECT 
    u.id,
    u.nome,
    u.email,
    u.numero,
    u.data_nascimento,
    u.objetivo,
    n.neurodivergencia,
    n.especificacao,
    n.descricao
FROM usuario u
LEFT JOIN neurodivergencia n 
    ON u.neurodivergencia_id = n.id
WHERE u.id = 2;

SELECT nome
FROM usuario
WHERE nome = 'Fulano';

SELECT *
FROM usuario
WHERE nome = 'Fulano';

SELECT *
FROM usuario
WHERE email = 'usuario@gmail.com';

INSERT INTO empresa (nome) VALUES ('FocoPlus');

INSERT INTO materia (area) VALUES ('Ciencias Naturais');

SELECT id, titulo FROM aula;

INSERT INTO aula (titulo, data_aula, video, notes, empresa_id, materia_id, conteudo) 
VALUES ('Introdução à Biologia Celular', '2026-04-30', 'https://videoexemplo.com/aula1', 'Aula introdutória sobre células', 1, 1, 'Conteúdo completo sobre estrutura celular, organelas e funções'
);

INSERT INTO simulado (exame, aula_id) 
VALUES ('Simulado ENEM - Linguagens e Códigos', 2);

SELECT * 
FROM simulado;

SELECT 
    s.id,
    s.exame,
    a.titulo AS aula,
    a.data_aula
FROM simulado s
INNER JOIN aula a 
    ON s.aula_id = a.id;

INSERT INTO redacao (tema, eixo_tematico, escrita, usuario_id) 
VALUES ('Os desafios da educação no Brasil', 'Educação', 'A educação no Brasil enfrenta diversos desafios estruturais, como a falta de investimento e desigualdade no acesso...', 2
);

SELECT DISTINCT tema 
FROM redacao;

SELECT 
    m.area AS materia,
    a.titulo,
    a.conteudo
FROM materia m
INNER JOIN aula a 
    ON a.materia_id = m.id
WHERE m.area = 'Ciencias Naturais';

SELECT nome
FROM usuario
WHERE email = 'usuario@gmail.com'
  AND senha = '1234';

SELECT 
    u.id AS usuario_id,
    u.nome,
    n.neurodivergencia,
    n.especificacao,
    n.descricao
FROM usuario u
INNER JOIN neurodivergencia n 
    ON u.neurodivergencia_id = n.id
WHERE u.id = 1;