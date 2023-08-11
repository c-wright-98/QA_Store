CREATE TABLE category (
	category_id int PRIMARY KEY NOT NULL,
	name varchar(50) NOT NULL
);

CREATE TABLE products (
	product_id int PRIMARY KEY NOT NULL,
	category_id int,
	name varchar(50) NOT NULL,
	description varchar(200),
	image_URL varchar(200),
	price float,
    FOREIGN KEY (category_id) REFERENCES category(category_id)
);

CREATE TABLE users (
	user_id int primary key,
	username varchar(50) NOT NULL,
	email varchar(100),
	password_hash varchar(200) NOT NULL
);

CREATE TABLE orders (
	order_id int primary key,
	user_id int,
	order_date DATETIME,
	total_amount float,
	status varchar(50),
	shipping_address varchar(200),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

create table cart_items (
	cart_id int PRIMARY KEY NOT NULL,
    user_id int,
    order_id  int,
    product_id int,
    quantity int,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
)
    
