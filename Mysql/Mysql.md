<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [3小时Mysql链接](#3%E5%B0%8F%E6%97%B6mysql%E9%93%BE%E6%8E%A5)
  - [sql语句中<>与!=作用一样](#sql%E8%AF%AD%E5%8F%A5%E4%B8%AD%E4%B8%8E%E4%BD%9C%E7%94%A8%E4%B8%80%E6%A0%B7)
  - [REGEXP--正则](#regexp--%E6%AD%A3%E5%88%99)
  - [NULL](#null)
  - [ORDER BY](#order-by)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# [3小时Mysql入门](https://www.bilibili.com/video/BV1iJ411m7Fj)

## sql语句中<>与!=作用一样

## REGEXP--正则

1. REGEXP '[gim]e'----搜索ge ie me

2. REGEXP '[a-h]e'

3. where中，^----beginning    $----end    |----logical or

4. excise

   ```sql
   select *
   from customers
   where first_name REGEXP 'elka|ambur'
   
   select *
   from customers
   where first_name REGEXP 'ey$|on$'
   
   select *
   from customers
   where first_name REGEXP '^my|se'
   
   select *
   from customers
   where first_name REGEXP 'b[ru]'
   # (br|bu)
   ```

## NULL

```sql
select *  
from orders
where shipper_id is null
```

## ORDER BY

```sql
# 按first_name升序排列
select *  
from customers
ORDER BY first_name

# 按first_name降序排列
select *  
from customers
ORDER BY first_name DESC

# 先对state进行排序
select *  
from customers
ORDER BY state first_name

# 使用数字排序会产生不好的结果，应该避免
# 得到按first_name&last_name排序的数据，并新增point字段，且数据全为10
select first_name,last_name,10 AS point
from customers
ORDER BY 1, 2
```

## LIMIT

```sql
# 拿到300条数据，不足则那最大的
select *
from customers
limit 300

# 从第六条数据开始，取3条数据
select *
from customers
limit 6，3

# 积分倒序排列，取前三
select *
from customers
order by points desc
limit 3
```

## JOIN

```sql
# 从orders&customers拿数据
select order_id, orders.customer_id, first_name, last_name
from orders
join customers
	on orders.customer_id = customers.customer_id

equals

select order_id, orders.customer_id, first_name, last_name
from orders
join customers c
	on orders.customer_id = c.customer_id    
```

 