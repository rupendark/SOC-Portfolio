# Elastic: Setting up a SOC Lab

**Platform:** TryHackMe\
**Room:** Elastic -- Setting up a SOC Lab\
**Focus:** Elastic Stack Deployment, Fleet, Integrations, Ingest
Pipelines, Dashboards

------------------------------------------------------------------------

# Overview

In this lab, I built a fully functional SOC environment using the
Elastic Stack.\
The objective was to deploy Elasticsearch, Kibana, Fleet Server, and
Elastic Agent, ingest logs from multiple sources, parse custom log
formats, and create dashboards for monitoring.

------------------------------------------------------------------------

# Elastic Stack Architecture

## Core Components

-   **Elasticsearch** -- Stores and indexes logs (Port 9200)\
-   **Kibana** -- Web interface for visualization (Port 5601)\
-   **Elastic Agent** -- Collects telemetry from endpoints\
-   **Fleet Server** -- Centralized agent management (Port 8220)

------------------------------------------------------------------------

# Installing Elasticsearch

``` bash
sudo su
cd Downloads/elastic
dpkg -i elasticsearch.deb
```

During installation: - Authentication enabled\
- TLS enabled\
- Elastic superuser password generated

## Configure Heap Memory

File:

    /etc/elasticsearch/jvm.options.d/heap.options

Add:

    -Xms1g
    -Xmx1g

## Start Elasticsearch

``` bash
systemctl start elasticsearch
systemctl enable elasticsearch
systemctl status elasticsearch
```

------------------------------------------------------------------------

# Installing Kibana

``` bash
dpkg -i kibana.deb
```

## Configure Kibana

File:

    /etc/kibana/kibana.yml

Add:

    xpack.encryptedSavedObjects.encryptionKey: "soc-lab-training-key-32chars-long!"
    xpack.fleet.registryUrl: "http://localhost:8081"

## Start Kibana

``` bash
systemctl start kibana
systemctl enable kibana
systemctl status kibana
```

Access UI:

    http://localhost:5601

------------------------------------------------------------------------

# Fleet Server & Elastic Agent Installation

``` bash
cd /home/ubuntu/Downloads/elastic/elasticagent

./elastic-agent install   --fleet-server-es=https://<VM-IP>:9200   --fleet-server-service-token=<TOKEN>   --fleet-server-policy=fleet-server-policy   --fleet-server-es-ca-trusted-fingerprint=<FINGERPRINT>   --fleet-server-port=8220   --install-servers   --insecure
```

------------------------------------------------------------------------

# System Integration Verification

Create a test user:

``` bash
useradd testuser
```

In Kibana Discover:

Query:

    process.name: "useradd"

Expected dataset:

    system.auth

------------------------------------------------------------------------

# Apache Integration

Query:

    event.module: "apache"

Dataset:

    apache.access

------------------------------------------------------------------------

# Custom VPN Log Ingestion

Generate logs:

``` bash
python3 /home/ubuntu/Downloads/scripts/vpnlog.py
tail /var/log/vpnlog
```

## Ingest Pipeline Name

    vpn.logs.pipeline

### Grok Pattern

    %{TIMESTAMP_ISO8601:event.time_string} %{WORD:event.action} %{USER:user.name} %{IP:source.ip} %{IP:vpn.client.ip} %{NOTSPACE:vpn.server.region}

### Date Processor

-   Field: event.time_string\
-   Format: ISO8601\
-   Target: @timestamp

------------------------------------------------------------------------

# Filestream Integration

Log Path:

    /var/log/vpnlog

Pipeline:

    vpn.logs.pipeline

Discover Query:

    event.module: "filestream"

------------------------------------------------------------------------

# Dashboard & Visualizations

## Pie Chart

Query:

    event.module: "filestream"

Slice by:

    event.action

Metric:

    Count

## Line Graph

-   Horizontal Axis: @timestamp\
-   Vertical Axis: Count\
-   Breakdown: event.action

------------------------------------------------------------------------

# Skills Demonstrated

-   SIEM Deployment\
-   Elasticsearch Configuration\
-   Fleet & Agent Management\
-   Log Ingestion & Parsing\
-   Grok Pattern Creation\
-   Dashboard & Visualization Building

------------------------------------------------------------------------

# Conclusion

This lab demonstrates the deployment of a complete Elastic-based SOC lab
environment capable of ingesting, parsing, and visualizing security
telemetry from multiple sources including Linux systems, Apache web
logs, and custom VPN logs.
