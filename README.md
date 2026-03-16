# Django URL Shortener 

This is a **URL Shortener application** built using the Django web framework.  
It allows users to input long, unwieldy URLs and quickly transform them into short, easy-to-share links.  

The project integrates with the **Bitly API**, which is a popular and reliable service for link shortening.  
On top of shortening, the app also focuses on a clean and minimal interface with a user-friendly workflow.

---

## Features

- **URL Shortening:** Enter any valid URL and get a shortened version instantly.  
- **Clickable Links:** The shortened link is clickable and opens in a new tab.  
- **Reset Button:** Quickly clear the form and result to start from scratch.  
- **Form Validations:** Prevents empty or invalid URL submissions.  
- **Error Handling:** Displays messages when a URL cannot be shortened (e.g., invalid URL format or API error).  
- **Responsive UI:** The interface adapts to different screen sizes for better accessibility.  
- **Simple & Minimal Design:** Clean, distraction-free layout to focus on the main task — shortening links.  

---

## Tech Stack

- **Backend:**  
  - Django 5.2.4 as the main web framework  
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
## QA Testing

This project was manually tested against 21 test cases covering all major 
features and edge cases.

### Test Summary
| Metric | Result |
|---|---|
| Total Test Cases | 21 |
| Passed | 19 |
| Failed | 2 |
| Pass Rate | 90.4% |
| Bugs Found | 2 |

### Areas Tested
- URL Shortening (valid, invalid, empty, edge cases)
- Clickable link behaviour (opens in new tab, correct redirect)
- Reset button and form state management
- Form validation (empty input, no scheme, special characters, XSS input)
- Error handling and user-friendly messaging
- Responsive UI at mobile (375px) and tablet (768px) breakpoints
- Cross-browser testing — Chrome, Firefox, Edge

### Bugs Found
**BUG_001 — Silent failure on already-shortened URL [Medium]**  
Pasting an existing Bitly link and clicking Shorten produces no output and 
no error message — user gets zero feedback.

**BUG_002 — H1 rendering inconsistency in Firefox [Low]**  
The h1 heading appears slightly brighter in Firefox compared to Chrome and 
Edge, likely due to a CSS font-rendering difference.

### Test Artifacts
- Full test case sheet with results: [`test-cases/qa_test_cases.xlsx`](./test-cases/qa_test_cases.xlsx)

---
