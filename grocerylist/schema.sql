drop table if exists item;
create table item (
	id integer primary key autoincrement,
	name text,
	dollars integer,
	cents integer
);
