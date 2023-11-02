# Shop Manager Project

## Introduction
During week 5 of the Makers Academy bootcamp, I embarked on my introductory project involving PostgreSQL. The objective was to design an app for shop owners to efficiently manage their inventory and orders. At that juncture, I was still navigating the intricacies of Classes and OOP. Regrettably, I couldn't complete the CLI aspect of the project due to the progression into the subsequent phase of the bootcamp. Given the knowledge I've acquired since then, revisiting such a task would be met with enhanced precision and strategy.

<em>This is a test driven development where I wrote extensive tests for the model and repository classes before writing the code to pass those tests.</em>

## Features

- When an order is placed, the details are added to the database:
    - The stock is adjusted.
    - A record of how many of each item in the order is added to the join table 'items_orders'.
- Shop owners/workers can get a list of all the items and sort them in numerous different ways.
    - (This part of the CLI is working.)
    - (To see how I've coded this, see the 'get_all' method in '[item_repository.py](./lib/item_repository.py)')
- Shop owners/workers can find an item by its ID and either delete it, change its price or update its stock.
- Shop owners/workers can add new items.
- Shop owners/workers can find an order by its ID and view the details of it.
- Orders can be partially or fully refunded (in the case of a full refund the order is deleted.)
    - When this happens the stock is adjusted.
- All the CRUD operations are available to the shop owners/workers.

## Database Tables

**Main Tables** - The id in each of these tables is the primary key.

- **items** (id, name, price, stock, amount_sold) - <em>many-to-many with orders through items_orders</em>
- **orders** (id, customer_name, date) - <em>many-to-many with items through items_orders</em>

**Join Table** - The item_id joins the items table, and the order_id joins the orders table.

- **items_orders** (item_id, quantity, order_id) - This keeps track of which items were sold in which orders and how many of each specific item in each order.

## Installation & Setup

Run the following command to clone the repo:
```bash
git clone https://github.com/shakey0/ShopManager
cd ShopManager
```

Create your virtual environment:
```bash
pipenv install
pipenv shell
```

Run the following commands to create the dev and test databases:
```bash
createdb items_orders
```

Run the tests:
```bash
pytest
```

Start the app: (I didn't finished the CLI, but did start it, so you can get a basic idea of how things work.)
```bash
python app.py
```