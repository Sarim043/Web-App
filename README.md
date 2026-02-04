# Azure Flask Web App

A modern, responsive Python web application built with [Flask](https://flask.palletsprojects.com/) and designed for deployment on Azure App Service. This project demonstrates a production-ready Web App structure with a focus on UI/UX and ease of deployment.

## 🚀 Features

- **Personalized Experience**: A dynamic homepage that accepts user input to generate personalized greetings.
- **Modern UI/UX**: Built with a custom CSS design system featuring:
  - Responsive layout (Mobile & Desktop)
  - Glassmorphism effects
  - Smooth animations and transitions
  - Dark mode aesthetic with vibrant gradients
- **Robust Routing**: Clean URL structure handling multiple routes (`/`, `/hello`, `/about`).
- **Production Ready**: Configured with `gunicorn` for robust production deployment on Linux-based Azure App Service.

## 🛠️ Technology Stack

- **Backend**: Python 3.10+, Flask 3.0.0
- **Frontend**: HTML5, Modern CSS3 (Variables, Flexbox, Grid), Jinja2 Templates
- **Production Server**: Gunicorn 21.2.0
- **Deployment**: Azure App Service (Linux)

## 📂 Project Structure

```
web-app/
├── app.py              # Main Flask application entry point
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── static/
│   └── css/
│       └── style.css   # Main stylesheet (Modern UI design)
└── templates/
    ├── index.html      # Homepage with input form
    ├── hello.html      # Personalized greeting page
    └── about.html      # Project information page
```

## ⚡ Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository** (or download source):
   ```bash
   git clone <repository-url>
   cd "web app"
   ```

2. **Create a Virtual Environment**:
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running Locally

Start the development server:

```bash
python app.py
```

The application will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

- **Home**: `http://127.0.0.1:5000/`
- **About**: `http://127.0.0.1:5000/about`

## ☁️ Deployment to Azure

This application is properly configured for Azure App Service.

1. **Create an Azure App Service** (Linux plan recommended).
2. **Deploy via GitHub Actions** or Local Git.
3. **Startup Command**: Azure automatically detects `requirements.txt` and uses `gunicorn`:
   ```bash
   gunicorn --bind=0.0.0.0 --timeout 600 app:app
   ```

## 📝 License

This project is an Intern Assignment Project 2026.
