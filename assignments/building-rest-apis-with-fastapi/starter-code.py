from fastapi import FastAPI

app = FastAPI(title="Task API")


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task API"}


# TODO: Add endpoints for listing, creating, updating, and deleting tasks
