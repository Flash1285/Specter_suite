<div align="center">
  <h1>👻 Spectre Suite 👻</h1>
  <p>
    <b>A web-based OSINT & Cybersecurity Reconnaissance Dashboard.</b>
  </p>
  <p>
    <a href="https://www.python.org/"><img alt="Python 3.10+" src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white"></a>
    <a href="https://flask.palletsprojects.com/"><img alt="Flask" src="https://img.shields.io/badge/Flask-2.0%2B-black?logo=flask&logoColor=white"></a>
    <img alt="Status" src="https://img.shields.io/badge/Status-Active-success?logo=github&logoColor=white">
  </p>
</div>

---

## 🚀 Why Spectre Suite?

**Spectre Suite** is a centralized web dashboard designed for security professionals, researchers, and hobbyists. It replaces the need to run dozens of separate command-line scripts by integrating a powerful suite of OSINT and reconnaissance tools into a single, clean "glassmorphism" UI.

This dashboard allows you to gather intelligence on networks, domains, users, and websites, and then automatically cross-references your findings with live threat data.

> **Note:** This project is a collaborative effort, combining expertise in cybersecurity, web development, and OSINT techniques to create a comprehensive reconnaissance platform.

## 📸 Project Gallery

| Main Dashboard | Scans Menu | Port Scanner (with CVEs) |
| :---: | :---: | :---: |
| ![Dashboard Screenshot](https://i.imgur.com/3mkc3Wf.png) | ![Scans Menu Screenshot](https://i.imgur.com/FKIcVDg.png) | ![Port Scan Screenshot](https://i.imgur.com/sauuXiu.png) |
| **Domain Recon** | **Directory Scan** | **Reports Page** |
| ![Domain Recon Screenshot](https://i.imgur.com/4hFClDy.png) | ![Directory Scan Screenshot](https://i.imgur.com/MmWyaoe.png) | ![Reports Page Screenshot](https://i.imgur.com/DtQvKma.png) |


---

## ✨ Features in Detail

| Tool | Icon | Function |
| :--- | :---: | :--- |
| **Live Threat Feed** | 🛡️ | Displays the latest Known Exploited Vulnerabilities (KEV) from the **CISA** feed on its own page. |
| **Port Scanner** | 💥 | Scans a target for open ports (top 100 or custom range) and identifies running services. |
| **Live CVE Intel** | 🤖 | **Automatically** cross-references found services (e.g., "Apache 2.4.41") with the CISA KEV database and flags active threats in the results. |
| **Domain Recon** | 🗺️ | Gathers full `WHOIS` data, enumerates all major `DNS` records, and finds active subdomains from a built-in wordlist. |
| **Social Media Scout** | 👥 | Finds user profiles across 20+ major social and tech sites (GitHub, Twitter, TryHackMe, etc.). |
| **Email Breach Check** | 📧 | Checks an email address against the **XposedOrNot** breach database (100% free, no API key required). |
| **Website Tech Scan** | ⚙️ | Identifies a website's technology stack (e.g., Nginx, React) and extracts interesting security headers. |
| **Directory Scan** | 📁 | Scans a web server for common hidden files and directories (e.g., `/admin`, `.env`). |
| **Report Generation** | 📜 | **Automatically** saves a detailed `.txt` report for every scan, available to view and download from the "Reports" page. |

---

## 🛠️ Tech Stack

* **Backend:** Python 3, Flask
* **Frontend:** HTML5, CSS3 (Glassmorphism), JavaScript (Fetch API)
* **Core Libraries:** `requests`, `whois`, `dnspython`, `builtwith`
* **Wordlists:** All wordlists (`subdomains.txt`, `common_paths.txt`, `social_sites.json`) are externalized for easy modification.

---

## 🚀 How to Run

Follow these steps to get the project running on your local machine.

### 1. Prerequisites

Make sure you have [Python 3](https://www.python.org/downloads/) and [Git](https://git-scm.com/downloads) installed.

### 2. Installation & Setup

* **1. Clone the Repository:**
```bash
git clone https://github.com/Flash1285/Specter_suite.git
cd Specter_suite
```
* **2. Set up a Virtual Environment (Recommended):**
```bash
# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```
* **3. Install Dependencies:**
```bash
pip install -r requirements.txt
```
* **4. Run the Application:**
```bash
# Navigate into the dashboard directory
cd Dashboard

# Run the Flask app
python app.py
```
* **5. Access the Dashboard: Open your browser and go to: http://127.0.0.1:5000**

---

## 📂 Repository Structure
```
Spectre-Suite/   
|
├── .gitignore
├── README.md
├── requirements.txt
│
├── Dashboard/    
│   ├── app.py
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── app.js
│   │   ├── img/
│   │   │   └── aot_logo.png
│   │   └── reports/
│   │       ├──  Reports will be saved here...
│   │       └── .gitkeep       
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── live_feed.html
│       ├── reports.html
│       ├── scans.html
│       ├── scan_directory.html
│       ├── scan_domain.html
│       ├── scan_email.html
│       ├── scan_port.html
│       ├── scan_social.html
│       └── scan_tech.html
│
└── titan-intel/             
    ├── directory_scanner.py
    ├── domain_recon.py
    ├── email_intel.py
    ├── port_scanner.py
    ├── social_scout.py
    ├── tech_enumerator.py
    ├── threat_intel.py
    └── wordlists/
        ├── common_paths.txt
        ├── social_sites.json
        └── subdomains.txt
```

---

## 🤝 Collaborative Project

This project is a collaborative effort developed by a team of cybersecurity enthusiasts passionate about OSINT and reconnaissance tools. We believe in open-source development and continuous improvement.

## 📞 Support & Contributions

If you encounter any issues or have suggestions for improvements:
- Open an issue on GitHub
- Submit a pull request with enhancements
- Share your feedback and use cases

## ⚠️ Disclaimer

This tool is intended for **educational purposes** and **authorized security testing only**. Always ensure you have explicit permission before scanning or gathering intelligence on any target. Unauthorized use may violate local, state, or federal laws.

---


<div align="center">
  <p><b>Built with 💀 for the cybersecurity community</b></p>
</div>
