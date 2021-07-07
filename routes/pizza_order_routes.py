from flask import render_template, request


class PizzaOrderRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/size", methods=["GET", "POST"])
        def size():
            if request.method == "GET":
                return render_template("size.html")
            elif request.method == "POST":
                return "posted"
