# Prometheus exporter for cluster-autoscaler-status

k8s provides a `cluster-autoscaler-status` configmap. sadly there was no way to easily export this data to Prometheus.  
now there is.

first version provides only essential information: pool name, and result of `cloudProviderTarget / maxSize`. that is:
* if your pool is at maximum, value will be `1`
* if `cloudProviderTarget` is `0`, you'll get `0`
* if `cloudProviderTarget` is `10` and `maxSize` is `20`, you'll get `0.5`

## Example output
```
# HELP cluster_autoscaler_pool cloudProviderTarget / maxSize
# TYPE cluster_autoscaler_pool gauge
cluster_autoscaler_pool{name="csi-1"} 0.0
cluster_autoscaler_pool{name="dinds-1"} 0.25
cluster_autoscaler_pool{name="engine-1"} 0.1
```

## Usage

it can be run in-cluster or out of cluster. metrics exporter runs on port `9100`

there's a ready to use [Docker image](https://hub.docker.com/r/codefresh/cluster-autoscaler-exporter)

## Limitations

currently the querying interval is hardcoded at `10s`
