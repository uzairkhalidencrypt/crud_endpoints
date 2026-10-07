from fastapi import FastAPI
from pydantic import BaseModel


class OrderRequest(BaseModel):
    item_name: str
    quantity: int
    price: float


app = FastAPI()


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
