from flask import Flask
from routes.main_routes import MainRoutes
from routes.pizza_order_routes import PizzaOrderRoutes

app = Flask(__name__)
MainRoutes.configure_routes(app)
PizzaOrderRoutes.configure_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
