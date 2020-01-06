from flask import Flask, flash, g, redirect, render_template, request, url_for
import models

app = Flask(__name__)


@app.route('/')
def top_page():
    # top page
    return render_template('top_page.html')


@app.route("/about")
def about():
    # about page
    return render_template("about.html")


@app.route("/items/<category>")
def view_catogory(category):
    items = models.get_category(category)
    return render_template("list.html", items=items)


@app.route("/items/view/<key>")
def view_item(key):
    item = models.get_item(key)
    return render_template("view.html")


if __name__ == '__main__':
    app.run(debug=True)