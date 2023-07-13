from fastapi import APIRouter, status, Path, HTTPException
from typing import Optional

from models.k8s import Pod
from v1.response import PodListResponse
from k8s import K8SAPIClient

k8s_api = K8SAPIClient("./kube_config")
pod_router = APIRouter(prefix="/pod",tags=["pod"])

@pod_router.get("/list/{namespace}", status_code=status.HTTP_200_OK, response_model=PodListResponse)
async def get_all_pod_list(namespace: Optional[str] = Path(title="namespace", 
                                                           description="the namespace of pod list")) -> PodListResponse:
    pod_list: list[Pod] = k8s_api.get_all_pod(namespace=namespace)
    if pod_list is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": True, "msg": "Bad Request."}
        )
    return PodListResponse(error=False, msg=pod_list)