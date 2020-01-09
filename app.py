from flask import Flask, flash, g, redirect, render_template, request, url_for, send_from_directory
import models
import os

app = Flask(__name__)


@app.route('/')
def top_page():
    # top page
    return render_template('top_page.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='img/favicon.ico')


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
    result = {
        "item_id": f"{item[1]}-{item[0]}",
        "img_path": f"{item[1]}-{item[0]}.jpg",
        "category": models.translate_catogory_name(item[1]),
    }
    return render_template("view.html")


@app.route("/items/view/test")
def view_test():
    return render_template("view.html", img_name="test.png")


if __name__ == '__main__':
    app.run(debug=True)