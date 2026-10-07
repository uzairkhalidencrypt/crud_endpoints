# let's say we are given a JSON payload
# {
# "name": "Wireless Mouse",
# "price": 45.0,
# "stock": 12
# } let's say we want to create an endpoint that accepts this JSON payload
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

Inventory = [
    {
        "name": "Wireless Mouse",
        "price": 45.0,
        "stock": 12
    }

]


class Product(BaseModel):
    name: str
    price: float
    stock: int


class ProductResponse(BaseModel):
    name: str
    price: float
    stock: int


@app.post("/products/")
def create_product(product: Product):
    Inventory.append(product.dict())
    return product

# let's create a get endpoint that returns a list of products


@app.get("/products/", response_model=list[ProductResponse])
def get_products():
    # for the sake of this example, let's return a dynamic list of products
    return [ProductResponse(**product) for product in Inventory]
# let create an update endpoint that updates the stock and price of a product based on its name


@app.put("/products/{product_name}/")
def update_product(product_name: str, stock: int, price: float):
    for product in Inventory:
        if product["name"] == product_name:
            product["stock"] = stock
            product["price"] = price
            return {"message": f"Product {product_name} updated successfully "}
    return {"message": f"Product {product_name} not found"}

# let's create a delete endpoint that deletes a product based on its name


@app.delete("/products/{product_name}/")
def delete_product(product_name: str):
    for product in Inventory:
        if product["name"] == product_name:
            Inventory.remove(product)
            return {"message": f"Product {product_name} deleted successfully "}
    return {"message": f"Product {product_name} not found"}


@app.post("/orders")
def process_order(item_name: str, quantity: int, price: float):

    # === 1. DEFENSIVE GUARDS (Validation Logic) ===
    # Rule: A user cannot order zero or negative items.
    if quantity <= 0:
        return {"error": "Invalid order. Quantity must be at least 1."}

    # Rule: We don't sell items that cost zero rupees.
    if price <= 0:
        return {"error": "Invalid order. Price must be greater than 0."}

    # === 2. DATA MANIPULATION (Calculation Logic) ===
    # Rule: Calculate the base cost, then apply a discount if they buy in bulk.
    total_cost = quantity * price

    if quantity >= 10:
        print("[Logic] Apply 10% bulk discount!")
        total_cost = total_cost * 0.90

    # === 3. PERSISTENCE OR RETURN LOGIC ===
    # Hand the finalized result back to the user
    return {
        "status": "Order Success",
        "item": item_name,
        "quantity_ordered": quantity,
        "final_bill": total_cost
    }
