# 🏏 Cricket Web Application (Flask)

This is a simple and fun Flask-based web application that allows users to register, log in, and explore cricket players, match schedules, and the latest news.

---

## 🚀 Features

- ✅ User Registration
- ✅ User Login
- ✅ Home Page with Welcome Message
- ✅ View Player Profiles
- ✅ Match Schedule Page
- ✅ News Page
- ✅ Basic CSS Styling

---

## 🛠️ Tech Stack

- **Backend**: Python 3, Flask
- **Frontend**: HTML, CSS
- **Templating Engine**: Jinja2

---

## 📁 Project Structure

Flask-App/
│
├── app.py # Main Flask app
├── requirements.txt # List of required packages
├── README.md # This readme file
│
├── static/
│ └── styles.css # Styling file
│
├── templates/
│ ├── base.html # Layout template
│ ├── home.html # Home page
│ ├── login.html # Login page
│ ├── register.html # Registration page
│ ├── players.html # Players list page
│ ├── schedules.html # Match schedule page
│ └── news.html # News page
│
└── myenv/ (optional) # Your virtual environment folder


---

## 🧑‍💻 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/cricket-flask-app.git
cd cricket-flask-app

python -m venv myenv
myenv\Scripts\activate     # Windows
# OR
source myenv/bin/activate  # macOS/Linux


pip install -r requirements.txt

python app.py

