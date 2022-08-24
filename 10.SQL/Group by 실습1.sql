/***************************************
	Group by 실습 - 01
***************************************/

-- emp 테이블에서 부서별 최대 급여, 최소 급여, 평균 급여를 구할 것
select a.deptno, max(sal) as max_sal, min(sal) as min_sal, round(avg(sal), 2) as avg_sal
from hr.emp a
group by a.deptno;

-- emp 테이블에서 부서별 최대 급여, 최소 급여, 평균 급여를 구하되 평균 급여가 2000이상인 경우만 추출
select a.deptno, max(sal) as max_sal, min(sal) as min_sal, round(avg(sal), 2) as avg_sal
from hr.emp a
group by a.deptno
having avg(sal) >= 2000;


-- emp 테이블에서 부서별 최대 급여, 최소 급여, 평균 급여를 구하되 평균 급여가 2000이상인 경우만 추출(with 절 이용)
with 
temp_01 as (
select a.deptno, max(sal) as max_sal, min(sal) as min_sal, round(avg(sal), 2) as avg_sal
from hr.emp a
group by deptno
)
select * from temp_01 where avg_sal >= 2000

-- 부서명 SALES와 RESEARCH 소속 직원별로 과거부터 현재까지 모든 급여를 취합한 평균 급여
select b.empno, max(ename) as ename, avg(c.sal) as avg_sal
from hr.dept a
	join hr.emp b on a.deptno = b.deptno 
	join hr.emp_salary_hist c on b.empno = c.empno 
where a.dname in ('SALES', 'RESEARCH')
group by b.empno


-- 부서명 SALES와 RESEARCH 소속 직원별로 과거부터 현재까지 모든 급여를 취합한 평균 급여(with 절 이용)
with 
temp_01 as (
select a.dname, b.empno, b.ename, b.job, c.fromdate, c.todate, c.sal
from hr.dept a
	join hr.emp b on a.deptno = b.deptno 
	join hr.emp_salary_hist c on b.empno = c.empno 
where a.dname in ('SALES', 'RESEARCH')
order by a.dname, b.empno, c.fromdate 
)
select empno, max(ename) as ename, avg(sal) as avg_sal
from temp_01
group by empno;


-- 부서명 SALES와 RESEARCH 부서별 평균 급여를 소속 지원들의 과거부터 현재까지 모든 급여를 취합하여 구할 것.
select a.deptno, max(dname) as dname, avg(c.sal) as avg_sal, count(*) as cnt 
from hr.dept a
	join hr.emp b on a.deptno = b.deptno 
	join hr.emp_salary_hist c on b.empno = c.empno 
where a.dname in ('SALES', 'RESEARCH')
group by a.deptno 
order by 1;

-- 부서명 SALES와 RESEARCH 부서별 평균 급여를 소속 지원들의 과거부터 현재까지 모든 급여를 취합하여 구할 것 (with 절 이용)
with
temp_01 as(
select a.deptno, a.dname, b.empno, b.ename, b.job, c.fromdate, c.todate, c.sal 
from hr.dept a
	join hr.emp b on a.deptno = b.deptno 
	join hr.emp_salary_hist c on b.empno = c.empno 
where a.dname in ('SALES', 'RESEARCH')
order by a.dname, b.empno, c.fromdate 
)
select deptno, max(dname) as dname, avg(sal) as avg_sal
from temp_01
group by deptno 
order by 1;




