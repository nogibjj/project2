[![CI](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml)

![CD](https://github.com/nogibjj/project2/actions/workflows/deploy.yml/badge.svg?branch=main)


## Kubernetes based Continuous Delivery

### Cluster Architecture
![Figure](https://github.com/nogibjj/project2/blob/main/components-of-kubernetes.svg)

### Simple CRUD with FastAPI framework
#### post
![Figure](https://github.com/nogibjj/project2/blob/main/Screen%20Shot%202023-02-28%20at%208.25.07%20PM.png)
#### get
![Figure](https://github.com/nogibjj/project2/blob/main/Screen%20Shot%202023-02-28%20at%208.25.50%20PM.png)
![Figure](https://github.com/nogibjj/project2/blob/main/Screen%20Shot%202023-02-28%20at%208.25.57%20PM.png)

### configure kubernates cluster

![Figure](https://github.com/nogibjj/project2/blob/main/Screen%20Shot%202023-02-28%20at%207.57.50%20PM.png)

![Figure](https://github.com/nogibjj/project2/blob/main/Screen%20Shot%202023-02-28%20at%207.58.02%20PM.png)

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

4. Use k9s. 

![Figure](https://github.com/nogibjj/project2/blob/main/Screen%20Shot%202023-02-20%20at%209.40.56%20PM.png)

![Figure](https://github.com/nogibjj/project2/blob/main/Screen%20Shot%202023-02-20%20at%209.49.15%20PM.png)

