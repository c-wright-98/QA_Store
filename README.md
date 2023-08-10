# QA_Store

This is the documentation for the QA Store project, I have decided to design a store front webpage based on the requirements laid out in the project brief description, creating a shop that sells plants letting users navigate the website pages, view products, add them to cart and checkout

## Identifying Epics and tasks

Using the brief I was able to identify three main users of the site the store admin, customers and visitors. All three have various user stories for the requirements of the website. I broke down the requirements of the site into epics to categories the user stories to be able to create tasks for my KanBan board.

<a href = "/documentation/user_stories.md"> Click here to see the user stories and epics </a>

## The MVP

The minimal viable product for this project is to have a website with a home page that customers can then navigate from to view products all together or in categories, they will be able to select products to view more information about them and add products to their cart on either of these pages, they can also view their cart and increase the quantity of items if they would like too and proceed to checkout which will take them to the payment page where they can enter shipping details and payment details.

## Database creation

To be able to manage the products for the store and create a functioning cart system and categories page a database using MySQL was used. Here I created three tables for storing and managing the data, these were the product table, category table and cart_items table.

The product table had the following attributes:
- product_id (int,Primary key)
- category_id (int, foreign key to the category table)
- name (VAR_CHAR(50))
- description (VAR_CHAR(200))
- price (float)
- image_URL (VAR_CHAR(200))

The category table had the following attributes:
- category_id (int, foreign key to the category table)
- name (VAR_CHAR(50))

The cart_items table had the following attributes:
- cart_id (int,Primary key)
- product_id (int, foreign key to the product table)
- quantity (int)

### Entity Relationships Diagram
![Entity Relationships Diagram of store database ](/path/to/image.png "ERD of store database")