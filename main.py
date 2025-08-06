from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Usman Arif is running the second time...Server of Fast API that is a django Framework"}