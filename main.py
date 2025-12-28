from fastapi import FastAPI
app = FastAPI()

@app.get("/welcome")
def welcome():
    return "Welcome to Mini-RAG"

