-- Write your PostgreSQL query statement below
with ranked_employees as
(
    select *, dense_rank() over(partition by departmentid order by salary desc) as ranked
    from Employee
)

select d.name as Department, re.name as Employee, re.salary
from Department d
join ranked_employees re
on d.id = re.departmentid
where ranked < 4