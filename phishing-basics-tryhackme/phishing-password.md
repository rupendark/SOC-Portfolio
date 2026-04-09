# Phishing Basics – TryHackMe

## 🧠 Room Overview

This room explored phishing techniques from a penetration tester’s perspective. It covered:

- Social engineering psychology
- URL/domain manipulation (Typosquatting)
- Email spoofing
- Credential harvesting
- Phishing campaign lifecycle
- Hands-on spear phishing attack simulation

The final task demonstrated a full credential harvesting attack using the Social Engineering Toolkit (SET).

---

# 🎯 Key Learning Outcomes

- Understanding phishing types (Phishing, Spear Phishing, Whaling)
- Applying psychological triggers (Urgency, Authority, Fear, Curiosity)
- Performing URL manipulation (Typosquatting)
- Bypassing basic email security via alias spoofing
- Building and deploying a credential harvester
- Capturing credentials in real-time

---

# 🔥 Task 6 – Password Retrieval via Phishing (Hands-On Attack)

## 🎯 Objective

Harvest Bob’s credentials (Head of Finance) using a spear phishing campaign.

Target:
```
bob@tryaccounting.thm
```

---

## Step 1: Launch Social Engineering Toolkit (SET)

SSH into the attacker machine:

```bash
ssh attacker@MACHINE_IP
```

Run SET:

```bash
SET
```

Navigation path:

```
1) Social-Engineering Attacks
2) Website Attack Vectors
3) Credential Harvester Attack Method
3) Custom Import
```

Configuration:
- POST back IP = MACHINE_IP
- Imported custom HTML login page
- Hosted phishing site at:

```
http://tryacounting.thm
```

⚠ Notice the typo (missing “c”) — this is **Typosquatting**

---

## Step 2: Credential Harvester Running

SET launched the credential harvester:

```
[*] Credential Harvester is running on port 80
```

This server captures POST requests containing usernames and passwords.

---

## Step 3: Email Spoofing via Rainloop

Accessed webmail client:

```
http://MACHINE_IP:8080
```

Logged in as:

```
attacker@phisher.thm
```

To bypass filtering:

- Used alias:
```
support@tryaccounting.thm
```

This allowed the email to appear as an internal message.

---

## Step 4: Crafting the Phishing Email

Subject:
```
Action Required: Password Expiration Notice
```

The email included:
- Authority trigger (IT security policy)
- Urgency trigger (must update before Friday)
- Link to typosquatted internal portal

---

## 🚨 Step 5: Credential Capture

After the victim submitted credentials, SET displayed:

```bash
[*] WE GOT A HIT! Printing the output:
POSSIBLE USERNAME FIELD FOUND: username=bob.wilkinson
POSSIBLE PASSWORD FIELD FOUND: password=***************
```

Final Flag:
```
THM{you_just_got_phished!}
```

---

# 🔍 Why Task 6 Is Important

This task demonstrates:

- Real-world spear phishing workflow
- Social engineering + technical exploitation
- Credential harvesting infrastructure setup
- Email spoofing bypass technique
- Typosquatting attack method
- Real-time credential interception

This mirrors how real attackers gain **initial access** before:

- Privilege escalation
- Lateral movement
- Ransomware deployment
- Data exfiltration

---

# 🛡 Defensive Takeaways

To prevent similar attacks:

- Enforce SPF, DKIM, and DMARC
- Use phishing-resistant MFA
- Monitor domain typosquatting
- Implement email security gateways
- Conduct regular phishing awareness training
- Enable email header inspection

---

# 🧠 MITRE ATT&CK Mapping

- T1566 – Phishing
- T1566.002 – Spearphishing Link
- T1557 – Adversary-in-the-Middle (Conceptual)
- T1110 – Credential Access
- T1585 – Domain Registration (Typosquatting)

---

# 🏆 Skills Demonstrated

- Social Engineering
- Phishing Infrastructure Setup
- Credential Harvesting
- Email Spoofing
- OSINT Application
- Attack Simulation
- Understanding Human Attack Surface

---

# 📌 Conclusion

This lab provided hands-on experience in executing a full phishing campaign from reconnaissance to credential capture. It reinforced how small domain manipulations and psychological triggers can lead to successful credential compromise.

Understanding these offensive techniques is critical for building stronger defensive strategies within Security Operations and Blue Team environments.
