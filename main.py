from fastapi import FastAPI
from routers import even, matrix, nth_largest, auth, register

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Cloud App! Visit /docs for the API interface."}



app = FastAPI(
    title="Cloud Computing LAB PAAS",
    description="ID: 20701026 Name: Sayma Siddiqua Simu"
)


app.include_router(even.router)
app.include_router(matrix.router)
app.include_router(nth_largest.router)
app.include_router(auth.router)
app.include_router(register.router)