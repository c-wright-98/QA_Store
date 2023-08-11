# QA_Store

This is the documentation for the QA Store project, I have decided to design a store front webpage based on the requirements laid out in the project brief description, creating a shop that sells plants letting users navigate the website pages, view products, add them to cart and checkout

<a href = "/documentation/screenshots"> This is where the backlog screen shots are stored atm </a>

## Identifying Epics and tasks

Using the brief I was able to identify three main users of the site the store admin, customers and visitors. All three have various user stories for the requirements of the website. I broke down the requirements of the site into epics to categories the user stories to be able to create tasks for my KanBan board.

<a href = "/documentation/user_stories.md"> Click here to see the user stories and epics </a>

## The MVP

The minimal viable product for this project is to have a website with a home page that customers can then navigate from to view products all together or in categories, they will be able to select products to view more information about them and add products to their cart on either of these pages, they can also view their cart and increase the quantity of items if they would like too and proceed to checkout which will take them to the payment page where they can enter shipping details and payment details.

## Database creation

To be able to manage the products for the store and create a functioning cart system and categories page a database using MySQL was used. Here I created three tables for storing and managing the data, these were the product table, category table and cart_items table.

The product table has the following attributes:
- product_id (int,Primary key)
- category_id (int, foreign key to the category table)
- name (VAR_CHAR(50))
- description (VAR_CHAR(200))
- price (float)
- image_URL (VAR_CHAR(200))

The category table has the following attributes:
- category_id (int, foreign key to the category table)
- name (VAR_CHAR(50))

The cart_items table has the following attributes:
- cart_id (int,Primary key)
- user_id (int, foreign key to the user table)
- order_id (int, foreign key to the order table)
- product_id (int, foreign key to the product table)
- quantity (int)

In addition to these a user table and an orders table will also be created so orders placed after payment can be accessed by customers using their username and password, this would also mean creating a registration form for customers.

The users table will have the following attributes:

- user_id (int, primary key)
- username (varchar(50))
- email (varchar(100))
- password_hash (varchar(200))

    The hashed password is used for security purposes.

The orders table has the following attributes:

- order_id (int, primary key)
- user_id (int, foreign key referencing users table)
- order_date (DATETIME)
- total_amount (float)
- status (varchar(50)) this will have status of either processing, shipped or delivered
- shipping address (varchar(200))

You can see the SQL query for creating these tables <a href = "/documentation/SQL_Files/table_creation.sql">here</a>
<h3 align="center"> Entity Relationships Diagram </h3>
<p align="center" width="100%">
<img src = "https://github.com/c-wright-98/QA_Store/blob/main/images/ERD.png" alt = "Entity Relationship Diagram for the store database" width = "33%">
</p>