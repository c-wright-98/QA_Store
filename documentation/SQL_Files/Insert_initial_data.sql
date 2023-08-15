insert into category (category_id, name)
values (101, 'indoors');

insert into category (category_id, name)
values (102, 'outdoors');

insert into category (category_idcategory, name)
values (103, 'pots');

insert into products (product_id,category_id,name,description,image_URL,price)
values (1001,101,'test','This is a test', 'static/images/plants/test-plant.png',9.99);

select * from category;

select * from products;

alter table products
add stock int;

UPDATE products
SET stock = 100
WHERE product_id = 1001;