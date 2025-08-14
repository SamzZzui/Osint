<p align="center">
  <a href="https://github.com/SamzZzui/readme-typing-svg" style="text-decoration:none;">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&width=600&height=60&lines=%F0%9F%A7%9E+OSINT+Framework+-+Python&center=true&color=00fff7" 
         alt="Typing SVG" 
         style="background:linear-gradient(135deg,#0f172a,#1e293b); 
                padding:12px 16px; 
                border-radius:15px; 
                box-shadow:0 12px 30px rgba(0,255,255,0.2); 
                display:inline-block;"/>
  </a>
</p>

---

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>OSINT Tools Banner</title>
<style>
  body {
    font-family: 'Arial', sans-serif;
    background: #f5f5f5;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }

  .banner {
    background: #ffffff;
    border-radius: 15px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    padding: 30px 50px;
    text-align: center;
    max-width: 700px;
  }

  .banner img {
    max-width: 100%;
    height: auto;
    margin-bottom: 20px;
  }

  .banner h1 {
    font-size: 48px;
    color: #4CAF50;
    margin: 0;
  }

  .banner h2 {
    font-size: 28px;
    color: #1A73E8;
    margin: 10px 0 20px;
  }

  .banner p {
    font-size: 14px;
    color: #555;
    margin-top: 0;
  }

  /* Optional: add a glow effect around the magnifying glass icon */
  .icon-glow {
    filter: drop-shadow(0 0 10px #4CAF50);
  }
</style>
</head>
<body>

<div class="banner">
  <!-- OSINT Tools Image -->
  <img src="https://i.imgur.com/5U8b2zZ.png" alt="OSINT Tools" class="icon-glow">

  <h1>OSINT</h1>
  <h2>TOOLS</h2>
  <p>Design & Code by <strong>SamzZzui</strong></p>
</div>

</body>
</html>



---





# 🧩 OSINT Framework - Python

**Author:** SAMZZZUI  
**License:** MIT  
**Year:** 2025  

# ⚠️ Disclaimer

Use this framework only for ethical purposes.
Unauthorized access to data or privacy violations is illegal.

---

## 🏷️ Badges

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)  
![License](https://img.shields.io/badge/license-MIT-green.svg)  
![GitHub Stars](https://img.shields.io/github/stars/SamzZzui/OSINT?style=social)  

---

## ⚡ Notes

Python 3.10+ recommended

Dependencies listed in requirements.txt

Internet connection required for API-based modules

Optional: Use check_dependencies.py for auto-install

---

## 🚀 Overview

 - This OSINT Framework is built in Python as a modular tool, used for cyber intelligence and reconnaissance tasks.

 - The framework provides a menu-based interface, allowing users to easily access different modules.

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

```

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

 - Each functionality is implemented in a separate module.

 - Adding new modules is very easy — just create the module and update the menu in main.py.

 - The code is readable, organized, scalable, and professional.

 - APIs or additional tools can be easily integrated.

---

## 🔮 Future Improvements

- Real API integrations (email, phone, domain, social media).  
- Exception handling for invalid inputs.  
- Save results to `.txt` or `.csv`.  
- Multi-platform reverse image search.  
- Colored terminal outputs using **Colorama**.