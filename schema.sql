drop table if exists applications;
drop table if exists users;
drop table if exists progression;
create table applications (
  id serial primary key ,
  name text not null,
  age text not null,
  country text not null,
  battletag text not null,
  armory text not null,
  specs text not null,
  rig text not null,
  experience text not null,
  improve text not null,
  what_it_takes text not null,
  ui text not null,
  logs text not null,
  headset text not null,
  raids text not null,
  prevention text not null,
  additional text not null,
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
insert into progression (name, bosses, normal, heroic, mythic) values ('Emerald Nightmare', 7, 7, 7, 3);
insert into progression (name, bosses, normal, heroic, mythic) values ('Trial of Valor', 3, 3, 0, 0);
insert into applications (name, age, country, battletag, armory, specs, rig, experience, improve, what_it_takes, ui, logs, headset, raids, prevention, additional)
values ('name', 'age', 'country', 'battletag', 'armory', 'specs', 'rig', 'experience', 'improve', 'what_it_takes', 'ui', 'logs', 'headset', 'raids', 'prevention', 'additional');
insert into applications (name, age, country, battletag, armory, specs, rig, experience, improve, what_it_takes, ui, logs, headset, raids, prevention, additional)
values ('name', 'age', 'country', 'battletag', 'armory', 'specs', 'rig', 'experience', 'improve', 'what_it_takes', 'ui', 'logs', 'headset', 'raids', 'prevention', 'additional');
insert into applications (name, age, country, battletag, armory, specs, rig, experience, improve, what_it_takes, ui, logs, headset, raids, prevention, additional)
values ('name', 'age', 'country', 'battletag', 'armory', 'specs', 'rig', 'experience', 'improve', 'what_it_takes', 'ui', 'logs', 'headset', 'raids', 'prevention', 'additional');
insert into users (name, pw_hash)
values ('admin', 'pbkdf2:sha1:1000$86o1V3VC$101ccd9dbea9aac4f760b9b783c4ba2f35fad8d5');