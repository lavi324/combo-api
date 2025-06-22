***Start:***

1) Open a new GitHub repo, pull the repo into the cloud shell and config the GitHub user for a future Push requests.

2) Enable "Kubernetes Engine API" (for GCP).

3) Set your default region and zone to us-central1 and us-central1-a:
```bash
gcloud config set compute/region us-central1
gcloud config set compute/zone us-central1-a
```
4) Set up a Git ignore file.

5) Apply a Terraform script that will set up a VPC Network, Subnet, GKE Cluster, NGINX Ingress Controller and Kubernetes Apps via Helm (Jenkins, ArgoCD, Mongo).

6) Set up a script that will automate the push of the future new files into this repository.
```bash
#!/bin/bash

USERNAME="lavi324"
TOKEN="${GITHUB_PAT}"

git remote set-url origin https://$USERNAME:$TOKEN@github.com/$USERNAME/sport-tables-ai.git

git add .
git commit -m "Initial commit"
git push origin main
```
```bash
export GITHUB_PAT=your_PAT
```
Make the script executable and run it:
```bash
chmod +x push.sh
./push.sh
```
