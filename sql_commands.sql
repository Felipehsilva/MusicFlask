-- create database playMusica;

use playMusica; 

create table musica(
id_musica int primary key auto_increment not null,
nome_musica varchar(50) not null,
cantor_banda varchar(50) not null,
genero_musica varchar(20) not null);


select * from musica;

insert into musica(nome_musica, cantor_banda, genero_musica) values('Toda via me alegrarei', 'Samuel Messias', 'Gospel');
insert into musica(nome_musica, cantor_banda, genero_musica) values('O Sol', 'Vitor Kley', 'Pop');

insert into musica (nome_musica, cantor_banda, genero_musica) values('Cavalo de Troia','MC Kevin','Funk'),
('Isis','MC Kako', 'Funk'),
('Pai eh quem cria', 'Tierry','Sertanejjo'),
('lobo Guara','Hungria','Rep'),
('Meu Abrigo', 'Mellin','Pop');


select * from musica where genero_musica = "Funk";
select * from musica where cantor_banda like'M%';
select * from musica where genero_musica <> "Funk";
select * from musica where id_musica < 5;

update musica set genero_musica = 'Sertanejo' where id_musica = 5;
update musica set cantor_banda ='Melin', genero_musica = 'Pop' where id_musica = 7;

delete from musica where id_musica = 3;

-- CRUD Creat, Read, Update, Delete
/*
TABELA Usuario
*/
create table usuario(
id_usuario int primary key auto_increment not null,
nome_usuario varchar(50) not null,
login_usuario varchar(20) not null,
senha_usuario varchar(15) not null);

select * from usuario;

insert into usuario(nome_usuario,login_usuario,senha_usuario)
values('Felipe','felipe','admin');

insert into usuario(nome_usuario,login_usuario,senha_usuario)
values('Jose Paulo','jose','1234');

-- limpa os dados da tabela sem deletar a tabela
truncate table usuario;

alter table usuario
add unique(login_usuario);

insert into usuario(nome_usuario,login_usuario,senha_usuario)
values('Felipe','felipe','admin');

insert into usuario(nome_usuario,login_usuario,senha_usuario)
values('Felipeh','felipe2','admin2');

delete from usuario where id_usuario = 4;

 