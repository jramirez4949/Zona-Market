from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hola():
    return "hola mundo"


@app.get("/health")
def health():
    return {"status": "ok"}