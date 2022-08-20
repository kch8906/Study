/******************************************
	조인 실습 - outer 조인
*******************************************/
select * from orders;
select * from customers;
select * from employees;
select * from shippers;
select * from order_items;
-- 주문이 단 한번도 없는 고객 정보 구하기.
select a.customer_id, a.contact_name, b.order_id, b.customer_id 
from nw.customers a
	left outer join nw.orders b on a.customer_id = b.customer_id 
where b.order_id is null;

-- 부서정보와 부서에 소속된 직원명 정보 구하기. 부서가 직원을 가지고 있지 않더라도 부서정보는 표시되어야 함.
select a.*, b.empno, b.ename 
from hr.dept a
	left join hr.emp b on a.deptno = b.deptno;
	
-- Madrid에 살고 있는 고객이 주문한 주문 정보를 구할것.
-- 고객명, 주문id, 주문일자, 주문접수 직원명, 배송업체명을 구하되,
-- 만일 고객이 주문을 한번도 하지 않은 경우라도 고객정보는 빠지면 안됨. 이 경우 주문 정보가 없으면 주문 id를 0으로 나머지는 NULL로 구할것
select a.customer_id ,a.contact_name, coalesce (b.order_id, 0) as order_id, b.order_date
	, c.first_name ||' '|| c.last_name as employee_name, d.company_name as shipper_comp
from customers a
	left join orders b on a.customer_id = b.customer_id
	left join employees c on b.employee_id = c.employee_id 
	left join shippers d on b.ship_via = d.shipper_id 
where a.city = 'Madrid';


-- orders_items에 주문번호(order_id)가 없는 order_id를 가진 orders 데이터 찾기
select * 
from order_items a 
	left join orders b on a.order_id = b.order_id 
where b.order_id is null;