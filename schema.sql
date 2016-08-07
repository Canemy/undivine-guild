drop table if exists applications;
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