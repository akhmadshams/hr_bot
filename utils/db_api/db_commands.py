from typing import Union
import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config

class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
        )

    async def execute(
        self,
        command,
        *args,
        fetch: bool = False,
        fetchval: bool = False,
        fetchrow: bool = False,
        execute: bool = False,
    ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join(
            [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
        )
        return sql, tuple(parameters.values())

# ------------user-----
    async def add_user(self, user_id, name, user_name):
        sql = "INSERT INTO main_users (user_id, name, user_name) VALUES($1, $2, $3) returning *"
        return await self.execute(sql, user_id, name, user_name, fetchrow=True)

# -------yangi anketa ----
    async def add_worker(self, full_name, b_date, phone, region, address, education, old_work, position, additions,create_at):
        sql = "INSERT INTO main_anketa (full_name, b_date, phone, region, address, education, old_work, position, additions,create_at) VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9, $10) returning *"
        return await self.execute(sql, full_name, b_date, phone, region, address, education, old_work, position, additions, create_at, fetchrow=True)

# ------work---
    async def add_work(self, work_title, image, description):
        sql = "INSERT INTO main_work (work_title, image, description) VALUES($1, $2, $3) returning *"
        return await self.execute(sql, work_title, image, description, fetchrow=True)

# --------read word---

    async def read_work(self):
        sql = "SELECT work_title FROM main_work"
        return await self.execute(sql, fetchrow=True)

# ------read all work---

    async def read_work_all(self):
        sql = "SELECT id, work_title, image, description FROM main_work"
        return await self.execute(sql, fetch=True)

# -------delete work---

    async def delete_work(self, title):
        await self.execute("DELETE FROM main_work WHERE work_title=", (title,), execute=True)

# --------------------
    async def select_all_users(self):
        sql = "SELECT * FROM main_users"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM main_users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM main_users"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE main_users SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM main_users WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE main_users", execute=True)


    async def add_product(
        self,
        category_code,
        category_name,
        subcategory_code,
        subcategory_name,
        productname,
        photo=None,
        price=None,
        description="",
    ):
        sql = "INSERT INTO products_product (category_code, category_name, subcategory_code, subcategory_name, productname, photo, price, description) VALUES($1, $2, $3, $4, $5, $6, $7, $8) returning *"
        return await self.execute(
            sql,
            category_code,
            category_name,
            subcategory_code,
            subcategory_name,
            productname,
            photo,
            price,
            description,
            fetchrow=True,
        )

    async def get_categories(self):
        sql = "SELECT DISTINCT category_name, category_code FROM products_product"
        return await self.execute(sql, fetch=True)

    async def get_subcategories(self, category_code):
        sql = f"SELECT DISTINCT subcategory_name, subcategory_code FROM products_product WHERE category_code='{category_code}'"
        return await self.execute(sql, fetch=True)

    async def count_products(self, category_code, subcategory_code=None):
        if subcategory_code:
            sql = f"SELECT COUNT(*) FROM products_product WHERE category_code='{category_code}' AND subcategory_code='{subcategory_code}'"
        else:
            sql = f"SELECT COUNT(*) FROM products_product WHERE category_code='{category_code}'"
        return await self.execute(sql, fetchval=True)

    async def get_products(self, category_code, subcategory_code):
        sql = f"SELECT * FROM products_product WHERE category_code='{category_code}' AND subcategory_code='{subcategory_code}'"
        return await self.execute(sql, fetch=True)

    async def get_product(self, product_id):
        sql = f"SELECT * FROM products_product WHERE id={product_id}"
        return await self.execute(sql, fetchrow=True)

    async def drop_products(self):
        await self.execute("DROP TABLE products_product", execute=True)