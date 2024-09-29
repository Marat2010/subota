import uvicorn
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
    # uvicorn.run(app:"main:app", reload=True)
