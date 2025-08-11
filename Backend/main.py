from fastapi import FastAPI
from routes import users, documents, reminders

app = FastAPI(title="Care App API")

app.include_router(users.router)
app.include_router(documents.router)
app.include_router(reminders.router)

@app.get("/")
def root():
    return {"message": "Care App API is running"}
