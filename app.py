import re
from time import sleep
from kubernetes import client, config
from kubernetes.client.rest import ApiException
from prometheus_client import start_http_server, Gauge


def query_metrics():
    try:
        config_map = v1.read_namespaced_config_map('cluster-autoscaler-status', 'kube-system').data['status']
        pools = re.findall(r"Name:\s+(\S+)\n\s+Health:.+\(ready=(\d+) .+ cloudProviderTarget=(\d+) .+ maxSize=(\d+)\)\)\n",
                           config_map, flags=re.M)
        for i in pools:
            ready.labels(i[0]).set(int(i[1]))
            target.labels(i[0]).set(int(i[2]))
            maxsize.labels(i[0]).set(int(i[3]))

    except ApiException as e:
        if e.status != 404:  # no config map is not an error, it just means autoscaling is not enabled
            raise e


try:
    config.load_incluster_config()
except config.ConfigException:
    config.load_kube_config()

v1 = client.CoreV1Api()
ready = Gauge('cluster_autoscaler_pool', 'ready', ['name'])
target = Gauge('cluster_autoscaler_pool_target', 'cloudProviderTarget', ['name'])
maxsize = Gauge('cluster_autoscaler_pool_max', 'maxSize', ['name'])

start_http_server(9100)
while True:
    query_metrics()
    sleep(10)
