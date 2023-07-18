from flask import Blueprint,render_template
from models.order_list import orders

orders_blueprint=Blueprint("Orders",__name__)

@orders_blueprint.route("/orders")
def index():
    return render_template("index.html",title="Order list",orders_for_jinja=orders)

@orders_blueprint.route("/orders/<order_number>")
def order(order_number):
    return render_template("order.html",title=f"Order number {order_number}",order=orders[int(order_number)])