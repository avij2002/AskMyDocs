from fastapi import FastAPI
from routers import upload

app = FastAPI()
app.include_router(upload.router)

@app.get('/amIAlive')
def amIAlive():
    return {"message": "I am alive!"}
