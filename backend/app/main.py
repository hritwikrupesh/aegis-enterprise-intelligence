from fastapi import FastAPI

app = FastAPI(
    title="Aegis API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Aegis"
    }