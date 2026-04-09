# Resume Skill Extractor & Job Matcher 🚀

## About the Project

This project is a simple web application that helps in analyzing a resume and matching it with a job description. It extracts important skills from the resume and calculates how well the resume fits the job using basic machine learning techniques.

I built this project to understand how NLP (Natural Language Processing) can be applied in real-world problems like resume screening.

---

## Features

* Extracts skills from resume text
* Matches resume with job description
* Shows a match percentage
* Simple and clean user interface
* Real-time analysis

---

## Tech Stack

* Python
* Flask
* spaCy (for NLP)
* scikit-learn (TF-IDF + Cosine Similarity)
* HTML, CSS

---

## How It Works

1. User enters resume text and job description
2. The system extracts skills from the resume
3. Both texts are converted into vectors using TF-IDF
4. Cosine similarity is used to calculate the match score
5. Results are displayed on the web page

---

## Project Structure

```
resume-matcher/
│
├── app.py
├── requirements.txt
│
├── model/
│   ├── skill_extractor.py
│   ├── matcher.py
│
├── utils/
│   ├── resume_parser.py
│
├── templates/
│   ├── index.html
│
├── static/
│   ├── style.css
│
└── data/
    ├── skills.txt
```

---



## Why I Built This

I wanted to create a project that is useful in real life and also helps me understand backend + machine learning concepts together. This project combines both in a simple way.

---

Anushka Verma
