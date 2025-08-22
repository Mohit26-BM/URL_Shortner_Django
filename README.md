# Django URL Shortener 🔗

This is a **URL Shortener application** built using the Django web framework.  
It allows users to input long, unwieldy URLs and quickly transform them into short, easy-to-share links.  

The project integrates with the **Bitly API**, which is a popular and reliable service for link shortening.  
On top of shortening, the app also focuses on a clean and minimal interface with a user-friendly workflow.

This project is designed not only as a learning tool for Django beginners but also as a fully functional application that can be deployed for personal use or extended into a production-ready system.

---

## ✨ Features

- **URL Shortening:** Enter any valid URL and get a shortened version instantly.  
- **Clickable Links:** The shortened link is clickable and opens in a new tab.  
- **Copy Functionality:** Easily copy the shortened link for sharing purposes.  
- **Reset Button:** Quickly clear the form and result to start from scratch.  
- **Form Validations:** Prevents empty or invalid URL submissions.  
- **Error Handling:** Displays messages when a URL cannot be shortened (e.g., invalid URL format or API error).  
- **Responsive UI:** The interface adapts to different screen sizes for better accessibility.  
- **Simple & Minimal Design:** Clean, distraction-free layout to focus on the main task — shortening links.  
- **Extendable Architecture:** The Django project is structured to allow further development (e.g., user accounts, custom short codes, analytics, etc.).

---

## 🛠️ Tech Stack

- **Backend:**  
  - Django 5.x as the main web framework  
  - Python 3.12 as the programming language  
  - Django’s built-in features for routing, forms, and template rendering  

- **Frontend:**  
  - HTML5 for semantic structure  
  - CSS3 for styling with a responsive design approach  
  - Django Templates for dynamic content rendering  

- **API Integration:**  
  - **Bitly API** used to generate actual shortened links  
  - Secure access token stored in environment variables  

- **Database:**  
  - SQLite (default Django database) is used for local development  
  - Can be swapped with PostgreSQL, MySQL, or any other supported database for production  

- **Other Tools:**  
  - `.env` for environment variable management (Django secret key, Bitly token, etc.)  
  - `.gitignore` to exclude unnecessary files like `__pycache__`, migrations, and `db.sqlite3`  
  - Git & GitHub for version control and project hosting  

---

