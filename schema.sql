drop table if exists applications;
drop table if exists users;
create table applications (
  id integer primary key autoincrement,
  battletag text not null,
  experience text not null,
  class text not null,
  improve text not null,
  attendance text not null,
  rig text not null,
  personal text not null,
  checked bit default 0,
  datetime date default current_timestamp
);
create table users (
  id integer primary key autoincrement,
  name text not null,
  pw_salt text not null
);