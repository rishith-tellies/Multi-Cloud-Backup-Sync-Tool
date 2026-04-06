# 🌩️ Multi-Cloud Backup Sync Tool

### Automated, Secure & Scalable Cloud Backup Engine

An intelligent Python-based automation tool that syncs local files to cloud storage. The system currently supports **AWS S3** and is designed with a modular architecture to extend to **Google Drive and other cloud providers**.

---

## 🚀 Overview

The **Multi-Cloud Backup Sync Tool** automates file backups from local systems to cloud storage with efficient change detection and secure credential handling.

✔ AWS S3 integration (fully implemented)
✔ Google Drive integration (setup ready & extensible)
✔ Designed for scalability and multi-cloud support

---

## 🏗️ Engineering Highlights

* 🔁 **Idempotent Sync Logic**
  Uploads only new or modified files, preventing duplication.

* 🔐 **Secure Credential Management**
  Uses environment variables instead of hardcoding secrets.

* 📦 **Modular Architecture**
  Separate modules for scanning, syncing, and cloud providers.

* ⚡ **Efficient File Change Detection**
  Uses hashing to detect file modifications.

* ☁️ **Cloud Integration**
  AWS S3 fully implemented; Google Drive integration supported via modular design.

---

## ✨ Features

* 📂 Scan local directories for files
* ☁️ Upload files to AWS S3
* 🔄 Sync only changed files
* 📊 Maintain file state using JSON
* 🌐 Extensible multi-cloud architecture (AWS + Google Drive ready)
* 🔐 Secure handling of credentials

---

## 🛠️ Tech Stack

* **Language:** Python
* **Cloud:** AWS S3 (boto3), Google Drive API (planned/partial)
* **Architecture:** Modular & scalable
* **Version Control:** Git & GitHub

---

## 📁 Project Structure

```text
Multi-Cloud-Backup-Sync-Tool/
│
├── main.py
├── auth.py
├── cloud/
│   ├── s3.py
│   └── drive.py
├── scanner/
│   └── scan.py
├── sync/
│   └── engine.py
├── utils/
│   └── hashing.py
├── state/
│   └── state.json
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/rishith-tellies/Multi-Cloud-Backup-Sync-Tool.git
cd Multi-Cloud-Backup-Sync-Tool
```

### 2. Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ☁️ AWS S3 Setup

### 🔑 Configure AWS Credentials

Set environment variables:

```env
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
```

---

### 📦 Create S3 Bucket

You can create a bucket via AWS Console or programmatically.

Ensure your IAM user has:

* `s3:PutObject`
* `s3:CreateBucket`
* `s3:ListBucket`

---

## ☁️ Google Drive Integration (Optional)

The project includes support for Google Drive and can be extended for full multi-cloud functionality.

---

### 🔑 Setup Steps

1. Go to Google Cloud Console
2. Create a new project
3. Enable **Google Drive API**
4. Configure OAuth Consent Screen
5. Create credentials:

   * Type: **Desktop App**
6. Download credentials JSON

---

### 📂 File Setup

Rename the downloaded file to:

```text
credentials.json
```

Place it in project root:

```text
Multi-Cloud-Backup-Sync-Tool/
├── credentials.json
```

---

### ▶️ First Run Authentication

```bash
python main.py
```

* Opens browser for login
* Generates `token.json` automatically

---

### 🔐 Security Notes

* ❌ Do NOT upload `credentials.json`
* ❌ Do NOT upload `token.json`
* ✔ Both are ignored via `.gitignore`

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 🔐 Security Best Practices

* No hardcoded credentials
* Sensitive files excluded via `.gitignore`
* Follows **Principle of Least Privilege**
* Uses environment variables for AWS

---

## 💡 Future Enhancements

* 🌐 Full Google Drive integration
* ☁️ Azure Blob Storage support
* ⏱️ Scheduled backups (cron jobs)
* 📊 Monitoring dashboard
* 📡 Real-time file sync

---

## 👨‍💻 Author

**Rishith Tellies**
BCA Cloud Computing Student | Aspiring Cloud Engineer ☁️

🔗 GitHub: https://github.com/rishith-tellies
💼 LinkedIn: https://www.linkedin.com/in/rishith-tellies

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
