from flask import render_template
from app import app
from models.book_shop import orders


@app.route("/orders")
def index():
    return render_template("index.html", title="Glasgow Books Orders", orders=orders)


@app.route("/order/<id>")
def single_order(id):
    return render_template(
        "order.html", title="Glasgow Books Single Order", order=orders[int(id)]
    )
