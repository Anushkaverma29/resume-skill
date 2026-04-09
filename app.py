import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import pdfplumber
# Ensure your model folder and skill_extractor.py exist
from model.skill_extractor import extract_skills

app = Flask(__name__)
app.secret_key = "supersecretkey"

# --- Authentication Setup ---
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Mock Database (Email: Password)
users_db = {"admin@gmail.com": "password123"}

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id) if user_id in users_db else None

# --- Skill Matcher Config ---
skills_list = [
    "python", "java", "sql", "machine learning",
    "html", "css", "javascript", "data structures",
    "flask", "react", "node.js", "mongodb", "aws", "docker"
]

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# --- Routes ---

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email in users_db:
            flash('This Email is already registered! Please Login.')
        else:
            users_db[email] = password
            flash('Account created successfully! Now you can Login.')
            return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email in users_db and users_db[email] == password:
            user = User(email)
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid Email or Password!')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    score = None
    matched = []
    recommendations = []
    resume_text = ""
    job_desc = ""

    if request.method == "POST":
        job_desc = request.form.get("job", "").strip()
        file = request.files.get("resume_file")
        
        if file and file.filename != '' and allowed_file(file.filename):
            try:
                with pdfplumber.open(file) as pdf:
                    resume_text = " ".join([page.extract_text() for page in pdf.pages if page.extract_text()])
            except Exception as e:
                flash("Error reading PDF file.")
        else:
            resume_text = request.form.get("resume", "").strip()

        if resume_text and job_desc:
            resume_skills = set(extract_skills(resume_text, skills_list))
            job_skills = set(extract_skills(job_desc, skills_list))
            matched = list(resume_skills & job_skills)
            recommendations = list(job_skills - resume_skills)
            score = round((len(matched) / len(job_skills)) * 100, 2) if job_skills else 0

    return render_template(
        "index.html",
        score=score,
        skills=matched,
        recommendations=recommendations,
        resume_text=resume_text,
        job_desc=job_desc,
        name=current_user.id
    )

if __name__ == "__main__":
    app.run(debug=True)