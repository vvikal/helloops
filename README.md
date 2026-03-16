# HelloOps

A small hands-on DevOps project where a simple Python app is containerized with Docker, deployed on Kubernetes, managed with Argo CD, and monitored with Prometheus and Grafana.

## Stack

- Docker
- Kubernetes
- Argo CD
- Prometheus
- Grafana
- Flask

## What it includes

- Dockerized Python app
- Kubernetes Deployment and Service
- ConfigMap for non-sensitive config
- Secret for sensitive config
- GitOps with Argo CD
- Prometheus metrics scraping
- Grafana dashboard

## Architecture

```text
GitHub → Argo CD → Kubernetes → HelloOps app → Prometheus → Grafana
