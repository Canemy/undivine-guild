drop table if exists applications;
drop table if exists users;
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