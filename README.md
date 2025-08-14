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

1. [Overview](#overview)  
2. [Features](#features)  
3. [Architecture & Modularity](#architecture--modularity)  
4. [Future Improvements](#future-improvements)  
5. [Quick Start](#quick-start)  
6. [Installation & Run](#installation--run)  
7. [Dependency Auto-Check (Optional)](#dependency-auto-check-optional)  
8. [Usage Demo & Screenshots](#usage-demo--screenshots)  
9. [Sample Output](#sample-output)  
10. [License](#license)  
11. [Notes](#notes)  
12. [Disclaimer](#disclaimer-use-this-framework-only-for-ethical-purposes)
---

## 🚀 Overview

Ye **OSINT Framework** Python me bana ek modular tool hai jo cyber intelligence aur reconnaissance tasks ke liye use hota hai.  
Framework menu-based interface provide karta hai jisse user easily different modules access kar sakta hai.

---

## 🎯 Features

1. **Domain Lookup**  
   - Retrieve WHOIS information for any domain.  
   - API/Library: [python-whois](https://pypi.org/project/python-whois/)  

2. **IP Information**  
   - Obtain geolocation and ISP details for an IP address.  
   - API: [ipinfo.io](https://ipinfo.io/)  

3. **Email Search**  
   - Check if an email has been involved in any data breaches.  
   - API: [Have I Been Pwned](https://haveibeenpwned.com/API/Key)  

4. **Social Media Search by Username**  
   - Search for a username across Instagram, Twitter, Facebook, LinkedIn.  
   - No official API used; basic HTTP requests to profile URLs.  
   - Advanced: Use [SocialSearcher](https://www.social-searcher.com/)  

5. **Indian Phone Number Search**  
   - Lookup Indian phone numbers using public directories or APIs.  
   - Suggested API: [PhoneInfoga](https://github.com/PhoneInfoga/PhoneInfoga)  

6. **Data Breach Search**  
   - Checks if email appears in known data breaches.  
   - API: [Have I Been Pwned](https://haveibeenpwned.com/API/Key)  

7. **People Search by Name and Email**  
   - Search for people by name and optionally email.  
   - Suggested API: [PeopleDB](https://peopledb.io/)  

8. **Image Lookup (Reverse Image Search)**  
   - Find where an image appears on the web.  
   - API: [TinEye](https://services.tineye.com/developers/)  

9. **Image Metadata Lookup**  
   - Extract EXIF data from images.  
   - Library: [Pillow](https://pillow.readthedocs.io/)  

10. **Where Email is Used on the Internet**  
    - Search where an email address appears online.  
    - API: [EmailRep](https://emailrep.io/)  

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