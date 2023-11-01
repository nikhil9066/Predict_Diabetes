# Flask Application with Docker
This is a basic Flask application containerized using Docker.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Building the Docker Image](#building-the-docker-image)
- [Running the Docker Container](#running-the-docker-container)
- [Repository](#repository)
- [Deploying to Kubernetes](#deploying-to-kubernetes)
- [Kube Status](#kube-status)


## Getting Started

### Prerequisites

- Docker installed on your system

### Building the Docker Image

Inorder to start the flask application pull the docker image from the hub
```
docker pull nikhilprao/flaskapp:v2
```
To build the Docker image for this Flask application, navigate to the project directory and run the following command:
```
docker build -t nikhilprao/flaskapp:v2 .
```
## Running the Docker Container
After building the Docker image, you can run a container from it using the following command:

```
docker run -p 8000:8000 nikhilprao/flaskapp:v2
```
The Flask application will be accessible at
```
http://localhost:8000
```
## Repository
The Docker image is hosted on Docker Hub at nikhilprao/flaskapp:v2.
[Docker repo](https://hub.docker.com/repositories/nikhilprao)

## Deploying to Kubernetes

After building and testing your Flask application, you can deploy it to a Kubernetes cluster. Here are the steps to deploy your application:

1. **Set Up a Kubernetes Cluster**: Ensure you have a Kubernetes cluster available. You can use Minikube for local development or a cloud-managed Kubernetes service like Google Kubernetes Engine (GKE), Amazon EKS, or Azure AKS for production deployments.

2. **Push Your Docker Image**: Make sure you've pushed your Flask application's Docker image to a container registry (e.g., Docker Hub). You'll need the image accessible to your Kubernetes cluster.

3. **Create Kubernetes Deployment and Service**: Use the following commands to deploy your application to Kubernetes:

```shell
   kubectl apply -f flask-app-deployment.yaml
   kubectl apply -f flask-app-service.yaml
```

These commands create the necessary resources for your Flask application on the cluster.

### Access Your Application
After a few minutes, an external IP will be allocated to the LoadBalancer service. You can access your Flask application by opening a web browser and navigating to the external IP address. Alternatively, you can use curl or kubectl proxy to access your application from the command line.
```
curl http://<external-ip>
```
Replace <external-ip> with the actual external IP address.

## Kube Status

### Checking Kubernetes Cluster Status

You can use the `kubectl get all` command to retrieve an overview of the following commonly used resource types in your Kubernetes cluster:

- **Pods**: This shows the status of all pods in your cluster, including their readiness, status, restart counts, and age.

- **Services**: It lists the services in your cluster, displaying their types (e.g., LoadBalancer, ClusterIP), cluster IP addresses, external IP addresses, and the port configurations.

- **Deployments**: This provides information about the status of deployments, including the number of replicas desired, the number of replicas currently available, and their readiness.

- **ReplicaSets**: Similar to deployments, it shows the number of replicas for each replica set, how many are currently running, and their readiness.

To check the status of these resource types, run the following command:

```shell
kubectl get all
```
#### Output:
```console
nikhilprao@Nikhils-MacBook-Air flaskwork % kubectl get all
NAME                                        READY   STATUS    RESTARTS   AGE
pod/flask-app-deployment-5f65686d4b-7nhd6   1/1     Running   0          4m48s
pod/flask-app-deployment-5f65686d4b-kp8j8   1/1     Running   0          4m48s
pod/flask-app-deployment-5f65686d4b-xpzqq   1/1     Running   0          4m48s

NAME                        TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
service/flask-app-service   LoadBalancer   10.101.147.61   <pending>     80:32377/TCP   34s
service/kubernetes          ClusterIP      10.96.0.1       <none>        443/TCP        10m

NAME                                   READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/flask-app-deployment   3/3     3            3           4m48s

NAME                                              DESIRED   CURRENT   READY   AGE
replicaset.apps/flask-app-deployment-5f65686d4b   3         3         3       4m48s

```
#### Output when Kube is running:
<img width="782" alt="Screenshot 2023-11-01 at 5 59 11 PM" src="https://github.com/nikhil9066/flaskwork/assets/36182930/993e5825-118d-4ead-b795-4e238d3c42e7">
