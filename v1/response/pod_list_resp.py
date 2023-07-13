from pydantic import BaseModel
from models.k8s import Pod

class PodListResponse(BaseModel):
    error: bool
    msg: list[Pod]