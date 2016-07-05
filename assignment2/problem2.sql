select a.row_num, b.col_num, sum(a.value * b.value)
from a, b
where a.col_num = b.row_num and a.row_num = 2 and b.col_num = 3
group by a.row_num, b.col_num;
