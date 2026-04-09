# 🛡 Elastic Defend – Endpoint Detection & Incident Investigation

## 📌 Overview

This lab focused on deploying and investigating endpoint telemetry using **Elastic Defend** within the Elastic Security platform. The objective was to simulate attacker behavior, generate alerts, and perform structured SOC-style investigations using SIEM queries and the Analyzer process graph.

Elastic Defend was configured in **Prevent mode**, enabling both telemetry collection and active malware prevention.

Version deployed: **9.2.0**

---

# 🔧 Environment Configuration

## Elastic Defend Policy Review

Elastic Defend was verified on the Linux host with the following configurations:

- Malware protection mode: **Prevent**
- Session data collection: Enabled
- Terminal output capture: Enabled
- File, network, and process telemetry: Enabled

This configuration ensured complete visibility into process trees, command-line execution, file modifications, and network activity.

---

# 📊 Telemetry Investigation in Discover

## Custom Data View Creation

To isolate endpoint telemetry, a custom Data View was created:

Index Pattern:
```
logs-endpoint.events*
```

This enabled focused investigation of:

- `event.category: process`
- `event.category: network`
- `event.category: file`

### Process Telemetry Findings

Filtering:

```kql
event.category: process
```

Identified active Python process execution:
```
python3.12
```

### Network Telemetry Findings

Filtering:

```kql
event.category: network
```

Primary network type observed:
```
ipv4
```

---

# 🔍 Script-Based Enumeration Investigation

## Execution of enum.sh

Command-line enumeration activity was initiated using a script.

Query used:

```kql
process.args: *enum.sh*
```

Three lifecycle events were identified:

- `fork`
- `exec`
- `end`

Additionally, `uid_change` indicated temporary privilege elevation.

## Process Chain Reconstruction

Using the unique `process.entity_id`, child processes were reconstructed:

```kql
process.parent.entity_id: "<entity_id>" AND event.action: exec
```

This allowed full reconstruction of the process tree.

---

# 🔎 Credential Discovery Simulation

Execution of `discovery.sh` simulated credential hunting activity.

Query:

```kql
process.args: *discovery.sh*
```

Findings:

- Parent executable: `/usr/bin/bash`
- First command executed:
  ```
  find /home -name *creds*
  ```
- Temporary directory created:
  ```
  /tmp/creds
  ```

### MITRE ATT&CK Mapping

- T1083 – File and Directory Discovery
- T1059 – Command and Scripting Interpreter

---

# 🚨 Malware Prevention Validation (EICAR Test)

To validate NGAV functionality, the EICAR test string was written to disk.

Elastic Defend immediately quarantined the file.

Alert Details:

- Risk Score: **73**
- Event Code: `malicious_file`
- Prevention confirmed (Prevent mode active)

Investigation performed in:

- Discover (alert documents)
- Security Alerts Dashboard
- Analyzer process graph

---

# 🔐 Sensitive File Access Detection – /etc/shadow

Simulated privileged file access:

```bash
sudo su
cat /etc/shadow > shadow_copy
```

Detection triggered:

- Risk Score: **47**
- MITRE Tactic: **Privilege Escalation**

Alert analyzed via:

- Alert flyout panel
- Field pinning for investigation
- Analyzer graph for process visualization

---

# 🧠 Persistence & Reverse Shell Simulation

## Cron-Based Persistence

Executed `persist.sh` to simulate attacker persistence.

Alert triggered:
**Cron Job Created or Modified**

### Investigation Steps

Pinned key fields:

- `@timestamp`
- `file.name`
- `file.path`
- `process.name`
- `user.name`

Using Analyzer graph:

- Identified bash execution chain
- Child process: `/usr/bin/printf`
- Observed permission changes:
  ```
  chmod +x /opt/.sysupdate.sh
  ```
- Cron job identified:
  ```
  system-update
  ```

### Reverse Shell Attempt

Detected outbound connection attempt to:

```
10.10.10.100:4444
```

---

# 🎯 MITRE ATT&CK Coverage

The Cron Job alert mapped to **3 MITRE tactics**, including:

- Privilege Escalation
- Persistence
- Command and Control

---

# 📈 Skills Demonstrated

- Elastic Defend configuration & policy validation
- Endpoint Detection & Response (EDR) investigation
- SIEM log correlation in Kibana Discover
- Process lifecycle analysis (`fork`, `exec`, `end`)
- Entity ID–based process chain reconstruction
- Alert triage & risk score interpretation
- MITRE ATT&CK mapping
- Malware prevention validation
- Privilege abuse detection
- Persistence mechanism investigation
- Reverse shell behavior identification

---

# 🏁 Conclusion

This investigation demonstrated end-to-end SOC workflow:

1. Telemetry collection
2. Alert generation
3. Triage and validation
4. Process tree reconstruction
5. Threat classification using MITRE ATT&CK
6. Behavioral analysis of persistence and command-and-control activity

The lab strengthened hands-on experience in:

- Endpoint monitoring
- Behavioral detection
- Incident response investigation
- Elastic SIEM operations

---

🔐 This case study reflects real-world SOC investigation methodology using Elastic Security and Elastic Defend.
