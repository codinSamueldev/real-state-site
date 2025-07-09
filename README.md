<h1 align="center">
	Real Estate Web App
</h1>

<h3 align="center">
	Fake Real Estate Site!
</h3>

<p align="center">
	<img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square"/>
	<img src="https://img.shields.io/github/languages/count/codinsamueldev/real-state-site?color=green"/>
</p>

<h4 align="center">
	Status: ✔️ Available
</h4>

<p align="center">
	<a href="#about">About</a> •
	<a href="#tech-stack">Tech Stack</a> •
	<a href="#installation">Installation</a> •
	<a href="#usage">Usage</a> • 
	<a href="#contact">Contact</a> 
</p>

## About
Developed my Django skills by building this fake real estate web application. The challenges I faced were several, setting up Gmail SMTP in order to send/receive emails, listing properties plus included a filter search bar and some deployment settings. Overall, I had quite fun building it. This is because I have not worked before with any LLM API to integrate it in a website, so it was very interesting how much work can be done if more web apps include in a way this models to help customers/users. The main purpose for this project were purely educational, meaning, I wanted to build something robust I can get a piece of pride on. Of course, it is not a perfect, or completed project. More features and improvements can be added, but, I am grateful with God for let me achieve this cool improvement in my skills.

## Tech Stack
<img src="https://img.shields.io/badge/Python-05122A?style=flat&logo=python" alt="python Badge" height="25">&nbsp;
<img src="https://img.shields.io/badge/Django-05122A?style=flat&logo=django" alt="django Badge" height="25">&nbsp;
<img src="https://img.shields.io/badge/Html5-05122A?style=flat&logo=html5" alt="html5 Badge" height="25">&nbsp;

## Installation
To Install this project, follow the steps above:
```bash
# This project can be run in any bash terminal, but it also can be hosted live as is on services like PythonAnywhere
# It is recommended to test this in a virtual environment
# Python 3.10 is REQUIRED
# Django 5.0.8 is REQUIRED

# Clone this repository
$ git clone https://github.com/codinsamueldev/real-state-site.git

# Change directory to the correct folder
$ cd real_state/

# Create a virtual environment:
$ python3 -m venv venv

# Activating the virtual environment:
$ source venv/bin/activate

# Install dependencies:
$ pip install -r requirements.txt

# Generate DJANGO_SECRET_KEY:
# Run: python manage.py shell
# Then.
$ from django.core.management.utils import get_random_secret_key
$ get_random_secret_key() # After this, copy the value to put it in an environment variable.

# Create .env file:
$ touch .env 

# Edit .env file and give values to the following environment variables:
$ SECRET_KEY='' # Paste secret key generated.
$ HOST_PASSWORD='' # For this one, go to https://support.google.com/mail/answer/185833?hl=en
$ GEMINI_API_KEY='' # https://ai.google.dev/gemini-api/docs/api-key

# Now you are ready to go.

```

## Usage
To use this project, follow the steps above:
```bash
# Running the Application

$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

## Contact
<img align="left" src="https://avatars.githubusercontent.com/codinsamueldev?size=100">

Made with ❤️ by [Samuel H.](https://github.com/codinsamueldev)!

<a href="https://www.linkedin.com/in/codinsamueldev/" target="_blank"><img src="https://img.shields.io/badge/Contact-LinkedIn-blue" alt="LinkedIn Badge" height="25"></a>&nbsp;

<br clear="left"/>
