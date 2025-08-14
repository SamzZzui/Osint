# Purpose:
Ye script OSINT framework ka entry point hai. Jab tum ise run karoge, ye menu-based interface show karta hai aur user ke choice ke hisaab se proper module call karta hai.

# Key Features:

ASCII banner with author info

Menu with 10 OSINT functionalities + Exit option

Input prompts for user data (email, domain, IP, phone, image path, etc.)

Calls respective functions from modules folder

---

# How the Code is Modular & Scalable:

Each functionality is separated into a module → easy to maintain.

New features can be added by just creating new module + updating menu in main.py.

Makes code readable, organized, and professional.

Can easily integrate APIs or tools inside each module later.



---

# Future Improvements:

Integrate real APIs for email, phone, domain, and social media searches.

Add exception handling for invalid inputs.

Save results to files (.txt or .csv) for record keeping.

Add multi-platform reverse image search.

Add colored outputs for better UI using colorama.

---

# How to Run:

1. Open terminal/command prompt.


2. Navigate to folder:



$ cd OSINT

3. Run main script:



$ python main.py

4. Follow menu prompts.