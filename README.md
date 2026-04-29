# 🔐 Smart Secret Scanner with CI/CD

A Python-based security tool that scans code repositories for exposed secrets like API keys and passwords, assigns risk levels, and prevents insecure code from being pushed using CI/CD.

---

## 🚀 Features

- 🔍 Detects secrets using regex patterns  
- 📁 Scans entire project directory  
- ⚠️ Classifies risk (HIGH / MEDIUM)  
- 💡 Provides fix suggestions  
- 📄 Generates JSON report  
- 🔁 Integrated with GitHub Actions (CI/CD)  
- ❌ Fails pipeline if high-risk secrets are found  

---

## 🧠 How It Works

```text
Code → Scan → Detect → Risk Analysis → JSON Report → CI/CD Decision
