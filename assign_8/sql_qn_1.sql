

create database IF NOT EXISTS testing;
USE testing;
drop table ODI_rankings;
create table  ODI_rankings
	(
		Tid int PRIMARY KEY,
		Ranks int unique,
		Tname varchar(50) unique NOT NULL,
		matches int NOT NULL,
		points int  default 0,
		rating int NOT NULL,
		check (rating > 20)

	);

insert into ODI_rankings VALUES(1,1,"England",43,5372,125);
insert into ODI_rankings VALUES(2,2,"India",47,5669,121);
insert into ODI_rankings VALUES(3,3,'South Africa',39,4488,115);
insert into ODI_rankings VALUES(4,4,'New Zealand',33,3729,113);
insert into ODI_rankings VALUES(5,5,'Australia',40,4342,109);
insert into ODI_rankings VALUES(6,6,'Pakistan',41,3846,94);
insert into ODI_rankings VALUES(7,7,'Bangladesh',35,3155,90);
insert into ODI_rankings VALUES(8,8,'West Indies',39,3022,77);
insert into ODI_rankings VALUES(9,9,'Sri Lanka',43,3266,76);
insert into ODI_rankings VALUES(10,10,'Afghanistan',31,1961,63);
insert into ODI_rankings VALUES(11,11,'Zimbabwe',30,1609,54);
insert into ODI_rankings VALUES(12,12,'Ireland',26,1176,45);
insert into ODI_rankings VALUES(13,13,'Scotland',10,373,37);
insert into ODI_rankings VALUES(14,14,'Nepal',8,152,19);
insert into ODI_rankings VALUES(15,15,'United Arab Emirates',15,144,10);
insert into ODI_rankings VALUES(16,16,'Papua New Guinea',9,50,6);

#1
select Tname from ODI_rankings where rating>100;
select Tname from ODI_rankings where rating<100 and matches<40;
select Tname from ODI_rankings where Tname like "%s";
select Tname from ODI_rankings where Tname NOT like "%a";
select Tname from ODI_rankings where matches in (15,40,39);
select * from ODI_rankings order by matches, points;
drop view odi;
create view odi as select * from ODI_rankings where matches>30;
select * from odi;
delete from ODI_rankings where Tname = "Papua_New_Guinea";

#2
drop table IF EXISTS points;
create table if NOT EXISTS points
	(
		Pos int not null ,
		Tid int PRIMARY KEY ,
		played int,
		won int,
		lost int,
		TNR int default 0,
		points int,
		NRR decimal(3,2),
		FOREIGN KEY(Tid) references ODI_rankings(Tid)
	);

insert into points values(1,4,4,3,0,1,7,2.16);
insert into points values(2,5,4,3,1,0,6,0.57);
insert into points values(3,2,3,2,0,1,5,0.53);
insert into points values(4,1,3,2,1,0,4,1.30);
insert into points values(5,9,4,1,1,2,4,-1.51);
insert into points values(6,8,3,1,1,1,3,2.05);
insert into points values(7,7,4,1,2,1,3,-0.71);
insert into points values(8,6,4,1,2,1,3,-1.79);
insert into points values(9,3,4,0,3,1,1,-0.95);
insert into points values(10,10,3,0,3,0,0,-1.49);

#2.3 not done

#2.4
select * from ODI_rankings o, points p  where o.Tid=p.Tid;
#2.5
select ODI_rankings.* from ODI_rankings o, points p  where o.Tid=p.Tid and Ranks between 6 and 16;
#2.6
alter table points add column Tied int default 0;
#2.7
alter table points change TNR NR int default 0;
drop table Results;
create table Results
(Team1 int,
Team2 int,
Marginruns int,
Marginwickets int,
Month varchar(15),
Day int,
Place varchar(30)
);

insert into results values(1,3,104,null,'May',30,'The Oval');
insert into results values(8,6,null,7,'May',31,'Trent Bridge');
insert into results values(4,9,null,10,'June',1,'Sophia Gardens');
insert into results values(5,10,null,7,'June',1,'Bristol');
insert into results values(7,3,21,null,'June',2,'The Oval');
insert into results values(6,1,14,null,'June',3,'Trent Bridge');
insert into results values(9,10,34,null,'June',4,'Sophia Gardens');
insert into results values(2,3,null,6,'June',5,'Rose Bowl');
insert into results values(4,7,null,2,'June',5,'The Oval');
insert into results values(5,8,15,null,'June',6,'Trent Bridge');
insert into results values(6,9,null,null,'June',7,'Bristol');
insert into results values(1,7,106,null,'June',8,'Sophia Gardens');
insert into results values(4,10,null,7,'June',8,'Taunton');
insert into results values(2,5,36,null,'June',9,'The Oval');
insert into results values(3,8,null,null,'June',10,'Rose Bowl');
insert into results values(7,9,null,null,'June',11,'Bristol');
insert into results values(5,6,41,null,'June',12,'Taunton');
insert into results values(2,4,null,null,'June',13,'Trent Bridge');
insert into results values(1,8,null,8,'June',14,'Rose Bowl');
insert into results values(5,9,87,null,'June',15,'The Oval');
insert into results values(3,10,null,9,'June',15,'Sophia Gardens');
insert into results values(2,6,89,null,'June',16,'Old Trafford');
insert into results values(8,7,null,null,'June',17,'Taunton');
insert into results values(1,10,null,null,'June',18,'Old Trafford');
insert into results values(4,3,null,null,'June',19,'Edgbaston');
insert into results values(5,7,null,null,'June',20,'Trent Bridge');
insert into results values(1,9,null,null,'June',21,'Headingley');
insert into results values(2,10,null,null,'June',22,'Rose Bowl');
insert into results values(8,4,null,null,'June',22,'Old Trafford');
insert into results values(6,3,null,null,'June',23,"Lords");
insert into results values(7,10,null,null,'June',24,'Rose Bowl');
insert into results values(1,5,null,null,'June',25,"Lords");


#3.1
select distinct Place from results;
#3.3
select count(Team1) as NO_OF_MATCHES from results where Place="Lords";
#3.5
select avg(Marginruns) from results;
#3.6
select count(Team1) as NO_OF_MATCHES ,Place  from results group by Place;
#3.7
select Team2 from results order by Marginwickets desc limit 1;
#3.9 incomplete
select Results.Team1 from Results, ODI_rankings  order by (Team1,Team2);
#3.10
select * from Results where Place in ('Lords', 'The Oval', 'Trent Bridge','Old Trafford') order by field(Place,'Lords', 'The Oval', 'Trent Bridge','Old Trafford')  ;
#3.11
select distinct(o.Tname),p.points from ODI_rankings o,points p,Results r where o.Tid=p.Tid and (p.Tid=r.Team1 or p.Tid=r.Team2) order by points desc;
#3.12
select o.Tname,p.points,p.won from ODI_rankings o,points p,Results r where o.Tid=p.Tid and (p.Tid=r.Team1 or p.Tid=r.Team2) ;
#3.14
select distinct(o.Tname),p.played,p.won,p.lost  from ODI_rankings o,points p,Results r 
where o.Tid=p.Tid and (p.Tid=r.Team1 or p.Tid=r.Team2) and 
r.Place in ('Lords', 'The Oval', 'Trent Bridge','Old Trafford') 
order by field(Place,'Lords', 'The Oval', 'Trent Bridge','Old Trafford');