from fastapi import FastAPI

# FastAPI 객체 생성
app = FastAPI()

# '/'로 접근하면 return을 보여줌
@app.get("/")
def read_root():
    return {"Hello": "World"}
