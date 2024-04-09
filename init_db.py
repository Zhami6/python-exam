from db import get_connection
from db import insert_update


def init():
    create_users_table = "CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR(40))"
    create_foods_recipes_table = "CREATE TABLE IF NOT EXISTS foods_recipes (id INTEGER PRIMARY KEY AUTOINCREMENT, recipe_name VARCHAR(40), price NUMERIC)"

    insert_update(
        get_connection(),
        query=create_users_table,
        params=tuple(),
    )
    insert_update(
        get_connection(),
        query=create_foods_recipes_table,
        params=tuple(),
    )
