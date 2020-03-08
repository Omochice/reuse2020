from flask import Flask, flash, g, redirect, render_template, request, url_for, send_from_directory
import models
import os

app = Flask(__name__)

categories = [{"en": item[0], "jp": item[1]} for item in models.load_category_list()]


def my_render(render_target: str, **kwargs):
    return render_template(render_target, categories=categories, **kwargs)


@app.route('/')
def top_page():
    # top page
    return my_render('top_page.html')


@app.route("/status")
def show_status():
    contents = models.get_n_contents()
    n_sum = sum([c["n_content"] for c in contents])
    return my_render("status.html", contents=contents, n_sum=n_sum)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='img/favicon.ico')


@app.route("/about")
def about():
    # about page
    return my_render("about.html")


@app.route("/items/<category>")
def view_catogory(category):
    results = models.get_category(category)
    items = [{
        "item_id": f"{result[1]}-{result[0]}",
        "img_path": f"img/{result[1]}-{result[0]}.jpg",
        "key": result[0],
        "model_number": result[2]
    } for result in results]
    return my_render("list.html", items=items)


@app.route("/items/view/<key>")
def view_item(key):
    item = models.get_item(key)
    result = {
        "item_id": f"{item[1]}-{item[0]}",
        "img_path": [f"img/{item[1]}-{item[0]}.jpg"],
        "category": f"{item[1]}: {models.translate_catogory_name(item[1])}",
        "model_number": item[2],
        "price": item[3],
        "guide": item[4],
        "remarks": item[5]
    }
    for i in range(1, 3):
        p = f"img/{item[1]}-{item[0]}_{i}.jpg"
        if os.path.exists(os.path.join(app.root_path, "static", p)):
            result["img_path"].append(p)
    return my_render("view.html", item=result)


# @app.route("/items/view/test")
# def view_test():
#     return my_render("view_test.html", img_name="test.png")

if __name__ == '__main__':
    app.run(debug=True)