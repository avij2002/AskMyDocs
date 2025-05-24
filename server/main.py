from fastapi import FastAPI
from routers import upload, query

app = FastAPI()
app.include_router(upload.router)
app.include_router(query.router)

@app.get('/amIAlive')
def amIAlive():
    return {"message": "I am alive!"}
