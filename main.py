from flask import Flask
from flask import request
from flask import render_template
from flask import make_response

from db import get_connection
from db import select_all
from db import select_one
from db import select_many
from db import insert_update

from init_db import init

app = Flask(__name__)


# domen.kz/users
@app.route("/users", methods=["GET", "POST"])  # маршрут
def get_users():  # обработчик
    if request.method == "GET":
        query = "SELECT * FROM users"
        result = select_all(get_connection(), query=query, params=tuple())
        return result

    username = request.form.get("username")
    query = "INSERT INTO users (username) VALUES (?)"
    print(
        insert_update(
            get_connection(),
            query=query,
            params=(username,),
        )
    )
    return "OK"


@app.route("/users/<int:id>")
def get_user(id):
    query = "SELECT * FROM users WHERE user_id = ?"
    user = select_one(
        get_connection(),
        query=query,
        params=(id,),
    )
    return list(user)


# domen.kz/contacts
@app.route("/contacts", methods=["GET", "PUT", "POST"])  # маршрут
def get_contacts():  # обработчик
    if request.method == "POST":
        return "sdkgjskjg"
    elif request.method == "PUT":
        return "123"
    return "Это страница Арсена Бебры"


@app.route("/shop/c/<category>")
def get_items_by_category(category):
    return f"Показываю товары категории: {category}"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        # Чтобы получить данные из GET запроса, ипользуется request.args - возвращает словарь с данными
        return request.args
    elif request.method == "POST":
        # Чтобы получить данные из POST запроса, используется request.form - возвращает словарь с данными
        return request.form


@app.route("/bebra")
def aboba():
    # Вставление данных name, age в template, используя Jinja
    return render_template("users.html", name="Eraly", age=3)


@app.route("/set-cookie")
def set_cookie():
    response = make_response(render_template("cookie.html"))
    response.set_cookie("NAME", "Your Name")
    response.set_cookie("SURNAME", "Your SURNAME")
    response.headers["X-Name"] = "Batyrzhan"
    return response


@app.route("/delete-cookie")
def delete_cookie():
    response = make_response(render_template("cookie.html"))
    response.delete_cookie("NAME")
    return response


@app.route("/get-cookie")
def get_cookie():
    return request.cookies


if __name__ == "__main__":
    init()
    app.run(
        debug=True,
        host="0.0.0.0",
    )
