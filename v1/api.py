from fastapi import FastAPI
from k8s import K8SAPIClient
from v1.router import pod_router

k8s_api = K8SAPIClient("./kube_config")

app = FastAPI()
app.include_router(pod_router)

@app.get("")
async def hello() -> dict:
    return {
        "error": False,
        "msg": "hello world"
    }