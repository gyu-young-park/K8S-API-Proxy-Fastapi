from typing import Optional
from kubernetes import client, config
from kubernetes.client.models import V1PodList, V1Pod
from kubernetes.client.exceptions import ApiException

from models.k8s import Pod

class K8SAPIClient:
    def __init__(self, config_file: str) -> None:
        config.load_kube_config(config_file)
        
        self._k8s_client = client
        self._k8s_core = client.CoreV1Api()
    
    def get_all_pod(self, namespace: Optional[str]) -> Optional[list[Pod]]:
        try:
            k8s_pod_list: V1PodList = self._k8s_core.list_namespaced_pod(namespace=namespace, pretty=True)
        except(ApiException):
            return None
        
        pod_list: list[Pod] = []
        for k8s_pod in k8s_pod_list.items: 
            k8s_pod: V1Pod = k8s_pod
            pod_list.append(Pod(namespace=k8s_pod.metadata.namespace,
                                name=k8s_pod.metadata.name))
        
        return pod_list