-- select a.docid, b.docid, sum(a.count * b.count) 
-- from frequency a, frequency b
-- where a.term = b.term and a.docid = "10080_txt_crude" and b.docid = "17035_txt_earn"
-- group by a.docid, b.docid;

-- create view [big table] as 
-- select * from frequency
-- union
-- select 'q' as docid, 'washington' as term, 1 as count
-- union
-- select 'q' as docid, 'taxes' as term, 1 as count
-- UNION 
-- SELECT 'q' as docid, 'treasury' as term, 1 as count;

select a.docid, b.docid, sum(a.count * b.count) as sim
from [big table] a, [big table] b
where a.term = b.term and a.docid = "q"
group by a.docid, b.docid
order by sim desc
limit 10;