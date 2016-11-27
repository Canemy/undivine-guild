drop table if exists applications;
drop table if exists users;
drop table if exists progression;
create table applications (
  id serial primary key ,
  battletag text not null,
  experience text not null,
  class text not null,
  improve text not null,
  attendance text not null,
  rig text not null,
  personal text not null,
  datetime date default current_timestamp
);
create table users (
  id serial primary key,
  name text not null,
  pw_hash text not null
);
create table progression (
  id serial primary key,
  name text not null,
  bosses smallint not null,
  normal smallint not null,
  heroic smallint not null,
  mythic smallint not null
);
insert into progression (name, bosses, normal, heroic, mythic) values ('Emerald Nightmare', 7, 7, 7, 0);