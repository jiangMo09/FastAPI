from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "歡迎來到我的簡單API！"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"你好，{name}！"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)