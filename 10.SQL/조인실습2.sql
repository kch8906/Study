/*********************************
	조인 실습 - 2
**********************************/
select * from customers;
select * from categories;
select * from order_items;
select * from orders;
select * from employees;
select * from shippers;
select * from suppliers;
select * from products;
-- 고객명 Antonio Moreno가 1997년에 주문한 주문 정보를 주문 아이디, 주문일자, 배송일자, 배송 주소를 고객 주소와 함께 구할 것.
select b.contact_name,a.order_id, a.order_date, a.shipped_date, a.ship_address, b.address
from orders a
	join customers b on a.customer_id = b.customer_id
where b.contact_name = 'Antonio Moreno'
and a.order_date between to_date('19970101', 'yyyymmdd') and to_date('19971231', 'yyyymmdd'); 

-- Berlin에 살고 있는 고객이 주문한 주문 정보를 구할 것
select a.city, b.order_id, b.order_date, b.shipped_date
from customers a
	join orders b on a.customer_id = b.customer_id
where a.city = 'Berlin';

-- 고객명 주문id, 주문일자, 주문접수 직원명, 배송업체명을 구할 것
select a.customer_id, a.contact_name , b.order_id, b.order_date
	, c.first_name ||' '||c.last_name as employee_name, d.company_name as shipper_name
from customers a
	join orders b on a.customer_id = b.customer_id
	join employees c on b.employee_id = c.employee_id 
	join shippers d on b.ship_via = d.shipper_id 
where a.city = 'Berlin';

--Beverages 카테고리에 속하는 모든 상품아이디와 상품명, 그리고 이들 상품을 제공하는 supplier 회사명 정보 구할 것
select a.product_id, a.product_name, b.category_name, c.company_name 
from products a
	join categories b on a.category_id = b.category_id
	join suppliers c on a.supplier_id = c.supplier_id 
where b.category_name = 'Beverages'
order by 1, 2, 4;


/* 고객명 Antonio Moreno가 1997년에 주문한 주문 상품정보를 고객 주소, 주문아이디, 주문일자, 배송일자, 배송주소 및
   주문 상품아이디, 주문 상품명, 주문 상품별 금액, 주문 상품이 속한 카테고리명, supplier명을 구할 것. */

select a.contact_name, a.address, b.order_id, b.order_date, b.shipped_date, b.ship_address
	, c.product_id, d.product_name, c.amount , e.category_name, f.company_name as supplier_name
from customers a
	join orders b on a.customer_id = b.customer_id	
	join order_items c on b.order_id = c.order_id 
	join products d on c.product_id = d.product_id
	join categories e on d.category_id = e.category_id 
	join suppliers f on b.ship_via = f.supplier_id 
where a.contact_name = 'Antonio Moreno';




