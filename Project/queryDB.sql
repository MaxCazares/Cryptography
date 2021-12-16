create database gradesCrypto;
use gradesCrypto;

create table alumno(
    Boleta varchar(10) primary key unique,
    Nombre varchar(30)
);

create table asignatura(
    ID varchar(4) primary key unique,
    nombreMat varchar (30)
);

create table nota(
    IDnota int not null auto_increment primary key,
    idAsig varchar(4),
    calificacion varbinary(256),
    idAlumno varchar(10)
);
alter table nota add constraint fk1 foreign key (idAsig) references asignatura(ID);
alter table nota add constraint fk2 foreign key (idAlumno) references alumno(Boleta);
insert into asignatura values('C224','ADOO');

drop database gradesCrypto;