from flask import (
    Flask,
    request,
    redirect,
    url_for,
    render_template,
    make_response,
    session,
)


app = Flask(__name__)
app.secret_key = "ASDASDASDASDASD"


# domen.kz/
@app.route("/")
def welcome():
    session["token"] = "my_token"
    print(session)
    return "Teacher`s Welcome Page"


# domen.kz/some-page
@app.route("/some-page")
def some_page():
    return "Some page"


@app.route("/students/<name>/<age>")
def find_student(name, age):
    random_dict = {"phy": 50, "che": 60, "maths": 70}
    return render_template(
        "user.html",
        name=name,
        age=1,
        random_dict=random_dict,
        session=session,
    )


# domen.kz/reviews/4.0
# domen.kz/reviews/1.0
# domen.kz/reviews/2.0
@app.route("/reviews/<float:rating>")
def find_reviews(rating):
    return f"Поиск отзывов с рейтингом - {rating}"


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        # request.form - получают параметры из тела запроса вида x-www-form-urlencoded
        username = request.form.get("username")
        password = request.form.get("password")

        return f"Отправился POST запрос. Отправлены данные: {username}, {password}"
    elif request.method == "GET":

        # request.args - получают QUERY PARAMS из ссылки запроса.
        username = request.args.get("username")
        password = request.args.get("password")

        return f"Отправился GET запрос. Отправлены данные: {username}, {password}"


@app.route("/redirect-url")
def redirect_url():
    return redirect("https://google.com")


@app.route("/redirect-url-local")
def redirect_url_local():
    return redirect(url_for("some_page"))


@app.route("/login-page")
def login_page():
    # TEMPLATES
    return render_template("login.html")


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
    app.run(
        debug=True,
        host="0.0.0.0",
    )
