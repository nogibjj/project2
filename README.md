[![CI](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml)
## Kubernetes based Continuous Delivery

1. First, install.

* `Install kubectl`

* `Install aws cli tools `

2. Connect to aws eks and config kubernates

* `aws eks update-kubeconfig --name [clustername] [region] `
 
* `ls -l ~/.kube `

* `kubectl config use-context arn:aws:eks:us-east-2:954946645007:cluster/kubernates`

* `kubectl cluster-info`

3. Deploy

* `kubectl apply -f eks/deployment.yaml`

* `kubectl get deployments`

* `kubectl apply -f eks/service.yaml`

* `kubectl get service` 

