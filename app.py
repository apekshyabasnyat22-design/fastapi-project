from fastapi import FastAPI, Depends
from typing import Optional
from databases import engine, Base, get_db
from sqlalchemy.orm import Session
from  schemas import ProductCreate
from models import ProductModel

app = FastAPI()

# Create the tables (just in case you add models later)
Base.metadata.create_all(bind=engine)


# A simple dependency function
async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/products/")
async def read_products(
    db: Session = Depends(get_db)
):
    # You can now use 'db' to query the database
    # products = db.query(ProductModel).all()
   
    return {
        "message": "Products retrieved",
        "params": "",
        "db_status": "Database session is active"
    }

@app.post("/products")
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    new_product = ProductModel(
        name=product.name,
        description=product.description,
        price=product.price,
        quantity=product.quantity
    )

    db.add(new_product)      # stage the object
    db.commit()              # save to DB
    db.refresh(new_product)  # get generated ID

    return new_product



@app.get("/orders/")
async def read_orders(
    db: Session = Depends(get_db)
):
    return {
        "message": "Orders retrieved",
        "params": "",
        "db_status": "Database session is active"
    }

print("Routes using Dependency Injection and SQLite added.")

@app.post("/orders")
def create_product
(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    new_product = ProductModel(
        name=product.name,
        description=product.description,
        price=product.price,
        quantity=product.quantity
    )

    db.add(new_product)      # stage the object
    db.commit()              # save to DB
    db.refresh(new_product)  # get generated ID

    return new_product  

        