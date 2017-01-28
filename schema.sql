--drop table if exists applications;
--drop table if exists users;
--drop table if exists progression;
--drop table if exists recruitment;
--drop table if exists roster;
drop table if exists gallery;
--drop table if exists category;
--create table applications (
--  id serial primary key ,
--  name text not null,
--  age text not null,
--  country text not null,
--  battletag text not null,
--  armory text not null,
--  specs text not null,
--  rig text not null,
--  experience text not null,
--  improve text not null,
--  what_it_takes text not null,
--  ui text not null,
--  logs text not null,
--  headset text not null,
--  raids text not null,
--  prevention text not null,
--  additional text not null,
--  datetime date default current_timestamp
--);
--create table users (
--  id serial primary key,
--  name text not null,
--  pw_hash text not null
--);
--create table progression (
--  id serial primary key,
--  name text not null,
--  bosses smallint not null,
--  normal smallint not null,
--  heroic smallint not null,
--  mythic smallint not null,
--  show text not null
--);
--create table recruitment (
--  id serial primary key,
--  class text not null,
--  spec1 text not null,
--  spec1_prio text not null,
--  spec2 text not null,
--  spec2_prio text not null,
--  spec3 text,
--  spec3_prio text,
--  spec4 text,
--  spec4_prio text
--);
--create table roster (
--  name text primary key,
--  rank smallint not null,
--  class smallint not null,
--  level smallint not null,
--  thumbnail text not null,
--  description text,
--  show text not null
--);
create table gallery (
  file text primary key,
  title text not null,
  description text not null,
  category text not null
);
--create table category (
--  shortcut text primary key,
--  name text not null
--);

--insert into users (name, pw_hash) values ('admin', 'pbkdf2:sha1:1000$092Ys003$d5b8b87be5cb99254f91ad1565220b493d752831');