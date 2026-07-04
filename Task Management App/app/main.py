from fastapi import FastAPI

app = FastAPI()

print("Server Started")

@app.get("/")
def root():
    print("Inside Server")
    return {"message": "Welcome To Task Manager App"}

