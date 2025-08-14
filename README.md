# 🧩 OSINT Framework - Python

**Author:** SAMZZZUI  
**License:** MIT  
**Year:** 2025  

---

## 🏷️ Badges

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)  
![License](https://img.shields.io/badge/license-MIT-green.svg)  
![GitHub Stars](https://img.shields.io/github/stars/SamzZzui/OSINT?style=social)  

---

## 📑 Table of Contents

1. [Overview](#🚀-overview)  
2. [Features](#🎯-features)  
3. [Architecture & Modularity](#🛠️-architecture--modularity)  
4. [Future Improvements](#🔮-future-improvements)  
5. [Quick Start](#⚡-quick-start)  
6. [Installation & Run](#💻-installation--run)  
7. [Dependency Auto-Check](#⚙️-dependency-auto-check-optional)  
8. [Usage Demo & Screenshots](#📸-usage-demo--screenshots)  
9. [Sample Output](#🔹-sample-output)  
10. [License](#📜-license)  
11. [Notes](#⚡-notes)  
12. [Disclaimer](#-disclaimer-use-this-framework-only-for-ethical-purposes)  

---

## 🚀 Overview

Ye **OSINT Framework** Python me bana ek modular tool hai jo cyber intelligence aur reconnaissance tasks ke liye use hota hai.  
Framework menu-based interface provide karta hai jisse user easily different modules access kar sakta hai.

---

## 🎯 Features

- **Domain Lookup** – Domain ke bare me detail information.
- **IP Information** – IP address ka location, ISP aur aur details.
- **Email Search** – Email ke existence aur associated data check karein.
- **Social Media Search by Username** – Usernames se profiles find karein.
- **Indian Phone Number Search** – Mobile numbers ka owner aur location.
- **Data Breach Search** – Email ya username compromised hua ya nahi.
- **People Search by Name and Email** – Individuals ke bare me information.
- **Image Lookup** – Reverse image search.
- **Image Metadata Lookup** – Image ka EXIF aur metadata extract karein.
- **Where Email is Used** – Email internet pe kahaan kahaan use hua check karein.

---

## 🛠️ Architecture & Modularity

- Har functionality **alag module** me implement ki gayi hai.  
- New modules add karna bahut easy hai — bas module create karo aur `main.py` ka menu update karo.  
- Code **readable, organized, scalable** aur professional hai.  
- APIs ya additional tools easily integrate kiye ja sakte hain.

---

## 🔮 Future Improvements

- Real APIs integration for email, phone, domain, and social media searches.  
- Exception handling for invalid inputs.  
- Save results to files (`.txt` or `.csv`) for record keeping.  
- Multi-platform reverse image search.  
- Colored outputs using **Colorama** for better UI.  

---

## ⚡ Quick Start

```bash
# Step 1: Clone the repository
git clone https://github.com/YourUsername/OSINT.git
cd OSINT

# Step 2: Install dependencies using requirements.txt
pip install -r requirements.txt

# Step 3: Optional: Run dependency check script
python check_dependencies.py

# Step 4: Run the OSINT framework
python main.py