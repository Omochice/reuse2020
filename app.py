from flask import Flask, flash, g, redirect, render_template, request, url_for, send_from_directory
import models
import os
import json

app = Flask(__name__)

with open("category.json", "r") as f:
    categories = [{"en": item[0], "jp": item[1]} for item in json.load(f)]


@app.route('/')
def top_page():
    # top page
    return render_template('top_page.html', categories=categories)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='img/favicon.ico')


@app.route("/about")
def about():
    # about page
    return render_template("about.html", categories=categories)


@app.route("/items/<category>")
def view_catogory(category):
    results = models.get_category(category)
    items = [{
        "item_id": f"{result[1]}-{result[0]}",
        "img_path": f"img/{result[1]}-{result[0]}.jpg",
        "key": result[0]
    } for result in results]
    return render_template("list.html", items=items, categories=categories)


@app.route("/items/view/<key>")
def view_item(key):
    item = models.get_item(key)
    print(item)
    result = {
        "item_id": f"{item[1]}-{item[0]}",
        "img_path": f"img/{item[1]}-{item[0]}.jpg",
        "category": f"{item[1]}: {models.translate_catogory_name(item[1])}",
        "model_number": item[2],
        "price": item[3],
        "guide": item[4],
        "remarks": item[5]
    }
    return render_template("view.html", item=result, categories=categories)


@app.route("/items/view/test")
def view_test():
    return render_template("view_test.html", img_name="test.png", categories=categories)


if __name__ == '__main__':
    app.run(debug=True)