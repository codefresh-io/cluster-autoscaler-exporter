# Prometheus exporter for cluster-autoscaler-status

k8s provides a `cluster-autoscaler-status` configmap. sadly there was no way to easily export this data to Prometheus.  
now there is.

we export three metrics per pool:
* number of `ready` nodes
* `cloudProviderTarget` number
* `maxSize` number

## Example output
```
# HELP cluster_autoscaler_pool ready
# TYPE cluster_autoscaler_pool gauge
cluster_autoscaler_pool{name="csi"} 0.0
cluster_autoscaler_pool{name="engines"} 1.0
# HELP cluster_autoscaler_pool_target cloudProviderTarget
# TYPE cluster_autoscaler_pool_target gauge
cluster_autoscaler_pool_target{name="csi"} 0.0
cluster_autoscaler_pool_target{name="engines"} 1.0
# HELP cluster_autoscaler_pool_max maxSize
# TYPE cluster_autoscaler_pool_max gauge
cluster_autoscaler_pool_max{name="csi"} 10.0
cluster_autoscaler_pool_max{name="engines"} 50.0
```

## Usage

it can be run in-cluster or out of cluster. metrics exporter runs on port `9100`

there's a ready to use [Docker image](https://hub.docker.com/r/codefresh/cluster-autoscaler-exporter)

## Limitations

currently the querying interval is hardcoded at `10s`
