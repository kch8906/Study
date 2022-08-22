/**************************************

	조인 실습 - Non Equi 조인과 cross 조인
***************************************/

select * from hr.salgrade;

-- 직원정보와 급여등급 정보를 추출.
select a.*, b.grade as salgrade, b.losal, b.hisal
from hr.emp a
	join hr.salgrade b on a.sal between b.losal and b.hisal;
	

select * from hr.emp where empno=7369;
-- 직원 급여의 이력정보를 나타내며, 해당 급여를 가졌던 시작 시점에서의 부서번호도 함께 가져올 것.
select a.*, b.*
from hr.emp_salary_hist a
	join hr.emp_dept_hist b on a.empno = b.empno and a.fromdate between b.fromdate and b.todate;

select *
from hr.emp_dept_hist where empno=7369;

select *
from hr.emp_salary_hist esh where empno=7369;

-- Cross 조인
with
temp_01 as
(
select 1 as rnum
union all
select 2 as rnum
)
select a.*, b.*
from hr.dept a
	cross join temp_01 b;