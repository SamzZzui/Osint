

```
   ____      _       _                            
  / __ \    (_)     | |                           
 | |  | |___ _ _ __ | |_ __ _ _ __ __ _ _ __ ___  
 | |  | / __| | '_ \| __/ _` | '__/ _` | '_ ` _ \ 
 | |__| \__ \ | | | | || (_| | | | (_| | | | | | |
  \____/|___/_|_| |_|\__\__, |_|  \__,_|_| |_| |_|
                         __/ |                    
                        |___/                     

```

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




<p align="center">
  <sub>Design by <strong>SamzZzui</strong></sub>
</p>





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