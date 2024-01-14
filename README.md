## Introduction
This is an example project for ML deployment consisting of a FastAPI serving ML model predictions in both single and batch requests.
FastAPI is the ideal framework for serving ML models because of its overall performance and asynch functionality with Uvicorn.  It is also a personal favorite of mine given its simplicity, allowing for very quick deployment of API endpoints.

<b>*Will use in a blog post explaining the process in more detail.... eventually.</b>

## Project Structure
- App: The data models, routes, and services required to serve the API endpoint
- Config: Configuration settings including necessary file paths or env variables
- Kube: Deployment and service configuration files for scaling with Kubernetes
- Pickles: Pkl files for the model, model variables, and scaler
- Tests: Unit tests for data models and endpoints
- Training: Script that covers the steps used during training, and usable for preprocessing request data
- Dockerfile: The file for turning the API into a Docker image
- requirements.txt: The dependencies used provided by a pip freeze
- run_api.sh: A shell script for building and running the docker image

## Scaling With Kubernetes
Requirements:
1. deployment file, sets the container/image to use, number of replicas to create, min/max resources
2. metric server, metrics are the basis for other service functions like autoscaling and load balancing. cpu utiliz, mem utiliz, # requests
3. horizontal pod autoscaler, allows your deployment to automatically scale up if a metric threshold is met
4. load balancer, manages the workloads across the cluster to efficiently utilize the different instances
5. set up prometheus for continuous collection of metrics over time
6. link the prometheus data to grafna to visualize deployment metrics

## Scaling With EKS
Requirements:
1. Create an EKS cluster in the console, with the CLI, or with Teraform/CloudFormation 
2. A ELB (elastic load balancer) is automatically created but you can select between a classic, network, or application load balancer 
3. You can also use the Cluster Autoscaler for EKS
4. Set up any needed storage for persistence
5. Amazon CloudWatch for logging and monitoring



## Other Considerations
- CI/CD and deployment strategies
- Security of the network 
