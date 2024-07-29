-- Write your PostgreSQL query statement below
with wf as
(
    select distinct product_id, min(s.year) over(partition by product_id) as first_year
    from sales s
)

select wf.product_id, wf.first_year, s.quantity, s.price
from wf
join sales s
on wf.product_id = s.product_id
where wf.first_year = s.year

