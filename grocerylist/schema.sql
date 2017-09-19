drop table if exists item;
create table item (
	id integer primary key autoincrement,
	name text not null,
	checked integer,
	dollars integer,
	cents integer
);
