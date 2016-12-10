--drop table if exists applications;
--drop table if exists users;
--drop table if exists progression;
drop table if exists recruitment;
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
--  mythic smallint not null
--);
create table recruitment (
  id serial primary key,
  class text not null,
  spec1 text not null,
  spec1_prio text not null,
  spec2 text not null,
  spec2_prio text not null,
  spec3 text,
  spec3_prio text,
  spec4 text,
  spec4_prio text
);

insert into recruitment (class, spec1, spec1_prio, spec2, spec2_prio, spec3, spec3_prio, spec4, spec4_prio)
values ('DK', 'Blood', 'None', 'Frost', 'None', 'Unholy', 'None', '', '');
insert into recruitment (class, spec1, spec1_prio, spec2, spec2_prio, spec3, spec3_prio, spec4, spec4_prio)
values ('DH', 'Havoc', 'Medium', 'Vengeance', 'None', '', '', '', '');
insert into recruitment (class, spec1, spec1_prio, spec2, spec2_prio, spec3, spec3_prio, spec4, spec4_prio)
values ('Druid', 'Balance', 'Medium', 'Feral', 'None', 'Guardian', 'None', 'Restoration', 'None');
insert into recruitment (class, spec1, spec1_prio, spec2, spec2_prio, spec3, spec3_prio, spec4, spec4_prio)
values ('Hunter', 'BM', 'None', 'Marksmanship', 'None', 'Survival', 'None', '', '');
insert into recruitment (class, spec1, spec1_prio, spec2, spec2_prio, spec3, spec3_prio, spec4, spec4_prio)
values ('Mage', 'Arcane', 'None', 'Fire', 'High', 'Frost', 'High', '', '');
insert into recruitment (class, spec1, spec1_prio, spec2, spec2_prio, spec3, spec3_prio, spec4, spec4_prio)
values ('Monk', 'Brewmaster', 'None', 'Mistweaver', 'High', 'Windwalker', 'None', '', '');
insert into recruitment (class, spec1, spec1_prio, spec2, spec2_prio, spec3, spec3_prio, spec4, spec4_prio)
values ('Paladin', 'Holy', 'Medium', 'Protection', 'None', 'Retribution', 'None', '', '');
insert into recruitment (class, spec1, spec1_prio, spec2, spec2_prio, spec3, spec3_prio, spec4, spec4_prio)
values ('Priest', 'Discipline', 'High', 'Holy', 'None', 'Shadow', 'High', '', '');
insert into recruitment (class, spec1, spec1_prio, spec2, spec2_prio, spec3, spec3_prio, spec4, spec4_prio)
values ('Rogue', 'Assassination', 'None', 'Outlaw', 'None', 'Subtlety', 'None', '', '');
insert into recruitment (class, spec1, spec1_prio, spec2, spec2_prio, spec3, spec3_prio, spec4, spec4_prio)
values ('Shaman', 'Elemental', 'High', 'Enhancement', 'High', 'Restoration', 'None', '', '');
insert into recruitment (class, spec1, spec1_prio, spec2, spec2_prio, spec3, spec3_prio, spec4, spec4_prio)
values ('Warlock', 'Affliction', 'None', 'Demonology', 'High', 'Destruction', 'High', '', '');
insert into recruitment (class, spec1, spec1_prio, spec2, spec2_prio, spec3, spec3_prio, spec4, spec4_prio)
values ('Warrior', 'Arms', 'Medium', 'Fury', 'None', 'Protection', 'None', '', '');
