import sqlite3


def get_connection():
    connection = sqlite3.connect("./weather.db")
    return connection


def insert_update(
    connection: sqlite3.Connection,
    query: str,
    params: tuple,
) -> None:
    cursor = connection.cursor()
    cursor.execute(query, params)
    connection.commit()
    cursor.close()
    connection.close()


def select_one(
    connection: sqlite3.Connection,
    query: str,
    params: tuple,
) -> any:
    cursor = connection.cursor()
    cursor.execute(query, params)

    res = cursor.fetchone()
    cursor.close()
    connection.close()

    return res


def select_many(
    connection: sqlite3.Connection,
    query: str,
    params: tuple,
    size: int = 1,
) -> any:
    cursor = connection.cursor()
    cursor.execute(query, params)

    res = cursor.fetchmany(size=size)
    cursor.close()
    connection.close()

    return res


def select_all(
    connection: sqlite3.Connection,
    query: str,
    params: tuple,
) -> any:
    cursor = connection.cursor()
    cursor.execute(query, params)

    res = cursor.fetchall()
    cursor.close()
    connection.close()

    return res
