from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ['http://localhost:3000'],
    allow_methods = ['*'],
    allow_headers = ['*']
)

redis = get_redis_connection(
    host = "redis-16641.c73.us-east-1-2.ec2.cloud.redislabs.com",
    port = 16641,
    password = "jDzbYTO8nsx1kxMLlapajN9aMUIldHdr"
)

class Product(HashModel):
    name: str
    price: float
    quantity: int
    class Meta:
        detabase = redis
# @app.get("/")
# async def root():
#     return {"message":"Hello World"}



@app.get("/products")
def all():
    return Product.all_pks()

@app.post("/products")
def create(product: Product):
    return product.save()