# 🔐 Smart Secret Scanner (CI/CD + Web App)

A Python-based security tool that detects sensitive information (API keys, passwords, tokens) in code repositories, assigns risk levels, and prevents insecure code deployment using CI/CD pipelines.

🚀 **Live Demo:** https://smart-secret-scanner.onrender.com

---

## 📌 Overview

Sensitive data like API keys and passwords are often accidentally exposed in source code, leading to serious security risks.

This project provides an automated solution that:

* Scans code for secrets
* Classifies risk levels
* Suggests fixes
* Blocks unsafe code via CI/CD

---

## 🚀 Features

* 🔍 Detects secrets using regex patterns
* 📁 Scans entire project directories
* ⚠️ Classifies risk levels (HIGH / MEDIUM)
* 💡 Provides fix suggestions
* 📊 Dashboard with summary stats
* 🌐 Web interface for file upload
* 🔁 CI/CD integration with GitHub Actions
* ❌ Fails pipeline if high-risk secrets are found

---

## 🧠 How It Works

```
Code → Scanner → Detection → Risk Analysis → Report → CI/CD Decision
```

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **CI/CD:** GitHub Actions
* **Frontend:** HTML, CSS
* **Deployment:** Render

---

## 📁 Project Structure

```
smart-secret-scanner/
│
├── app.py                 # Flask web app
├── main.py                # Scanner logic
├── requirements.txt       # Dependencies
│
├── templates/
│   └── index.html         # UI
│
├── uploads/               # Uploaded files
│
└── .github/
    └── workflows/
        └── scan.yml       # CI/CD pipeline
```

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 📊 Sample Output

```json
{
  "file": "test.py",
  "type": "API_KEY",
  "risk": "HIGH",
  "suggestion": "Store API keys in environment variables"
}
```

---

## 🔁 CI/CD Integration

* Runs automatically on every push
* Scans repository for secrets
* ❌ Fails build if HIGH-risk detected
* ✅ Passes if code is secure

---

## 🧪 Demo Scenarios

### ❌ Unsafe Code

```python
API_KEY = "sk-123abc"
```

➡️ Pipeline fails

### ✅ Safe Code

```python
print("Hello World")
```

➡️ Pipeline passes

---

## 💡 Key Highlights

* Real-world security problem
* Automated DevOps pipeline
* Risk-based decision system
* Developer-friendly UI

---

## 🚀 Future Improvements

* 🔗 Scan GitHub repositories directly
* 📊 Add charts and analytics dashboard
* 🔐 Integrate secret vault APIs
* 🌍 Multi-language support

---

## 👨‍💻 Author

Ankit

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share feedback!
