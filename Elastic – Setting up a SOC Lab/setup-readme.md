# Elastic: Setting up a SOC Lab  
**Platform:** TryHackMe  
**Room Type:** Blue Team / SOC Engineering  
**Focus Areas:** SIEM Deployment, Log Ingestion, Ingest Pipelines, Dashboards, Log Analysis  

---

## 📌 Overview

In this lab, I built a fully functional Security Operations Center (SOC) environment using the Elastic Stack. The objective was to deploy Elasticsearch, Kibana, Fleet Server, and Elastic Agents, ingest logs from multiple sources, parse custom log formats, and build dashboards for security monitoring.

This lab simulates real-world SOC responsibilities including:

- SIEM deployment and configuration  
- Log ingestion and parsing  
- Web server monitoring  
- Custom log pipeline creation  
- Threat investigation using dashboards  

---

# 🏗️ Elastic Stack Architecture

Before deployment, I reviewed the core components of the Elastic Stack.

## Core Components

### 🔎 Elasticsearch
- Core search engine and datastore
- Stores logs, alerts, and telemetry
- Listens on port **9200**
- Enables fast querying and aggregation

### 📊 Kibana
- Web interface for analysts
- Used for dashboards, visualizations, investigations
- Runs on port **5601**
- Communicates with Elasticsearch

### 🛰️ Elastic Agent
- Collects logs, metrics, and security data
- Sends data to Elasticsearch
- Managed centrally via Fleet

### 🎛️ Fleet Server
- Centralized agent management
- Deploys policies and integrations
- Default port: **8220**

---

# ⚙️ Installing Elasticsearch & Kibana

## Installing Elasticsearch

```bash
sudo su
cd Downloads/elastic
dpkg -i elasticsearch.deb
