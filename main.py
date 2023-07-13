import uvicorn
from v1.api import app

if __name__ == "__main__":
    uvicorn.run(app, port=8123)