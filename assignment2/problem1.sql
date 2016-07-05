-- part c
select count(*) from(
select term from frequency
where docid = "10398_txt_earn" and count = 1
union
select term from frequency
where docid = "925_txt_trade" and count = 1
);
-- part e
-- select count(*) from ( 
-- select docid from frequency 
-- group by docid
-- having count(term) > 300);

-- -- part f
-- select count(distinct docid) from (
-- select * from frequency a
-- inner JOIN frequency b
-- on a.docid = b.docid
-- where a.term = "transactions" and b.term = "world"
-- )
-- ;