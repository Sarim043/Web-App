# 🚀 Azure Flask Web Application

![Deployment Status](https://img.shields.io/github/actions/workflow/status/Sarim043/Web-App/main_sarimflaskapp.yml?branch=main&style=for-the-badge)
![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python)
![Framework](https://img.shields.io/badge/Flask-3.0.0-lightgrey?style=for-the-badge&logo=flask)
![Deployment](https://img.shields.io/badge/Azure-App%20Service-informational?style=for-the-badge&logo=microsoft-azure)

A professional, responsive Python web application built with the Flask framework, specifically optimized for seamless deployment on **Azure App Service (Linux)**. This project demonstrates modern UI design principles such as glassmorphism and animations, along with a GitHub Actions–based CI/CD pipeline for Azure App Service.

---

## 🌐 Live Application
The application is live and accessible at the following URL:
**[https://sarimflaskapp-hnbtd5f8grdsc9d7.centralindia-01.azurewebsites.net/](https://sarimflaskapp-hnbtd5f8grdsc9d7.centralindia-01.azurewebsites.net/)**

---

## ✨ Key Features
- **Dynamic Routing**: Handles multiple routes including a personalized greeting via query parameters (`/hello?name=User`).
- **Modern UI/UX**:
  - **Glassmorphism**: Sleek, transparent UI elements with blur effects.
  - **Responsive Design**: Fully functional on mobile, tablet, and desktop.
  - **Animations**: Subtle micro-interactions and transitions for a premium feel.
  - **Dark Mode Aesthetic**: A custom-designed dark theme with vibrant gradients.
- **Production Ready**: Optimized with Gunicorn for scalability on Azure's Linux environment.
- **CI/CD Integrated**: Automated deployments via GitHub Actions on every push to the main branch.

---

## 🛠️ Technology Stack
- **Backend**: Python 3.11+, Flask 3.0.0
- **Frontend**: HTML5, Modern CSS3 (Variables, Flexbox, Grid), Jinja2 Templates
- **Production Server**: Gunicorn (WSGI HTTP Server)
- **Deployment Platform**: Azure App Service (Linux Web App)
- **Version Control & CI/CD**: Git, GitHub, GitHub Actions

---

## 📂 Project Architecture & File Functionality

| File/Folder | Functionality & Purpose |
| :--- | :--- |
| **`app.py`** | **The Core Engine**. Defines the Flask application, manages routes (`/`, `/hello`, `/about`), and renders templates. It acts as the controller of the MVC-like structure. |
| **`templates/`** | **View Layer**. Contains Jinja2 HTML templates. <br> - `index.html`: The landing page with interactive input. <br> - `hello.html`: The dynamic greeting page. <br> - `about.html`: Detailed project information. |
| **`static/css/style.css`** | **Style Layer**. A comprehensive CSS system defining the look and feel, including the design system, layout, and animations. |
| **`requirements.txt`** | **Dependency Management**. Lists all Python packages required to run the app (`Flask`, `gunicorn`, `Werkzeug`, `Jinja2`). |
| **`startup.txt`** | **Azure Configuration**. A critical file that tells Azure's startup script how to launch the Gunicorn server (`gunicorn --bind=0.0.0.0 app:app`). |
| **`.github/workflows/`** | **CI/CD Automation**. Contains the YAML file that defines the automated build and deployment process to Azure. |
| **`.gitignore`** | **Version Control Cleanup**. Prevents sensitive or unnecessary files (like `venv/` or `__pycache__/`) from being committed to GitHub. |

---

## ⚡ Local Development Guide

### 1. Prerequisites
- Python 3.11 or higher installed on your machine.
- Git installed for repository management.

### 2. Setup Procedure
```bash
# Clone the repository
git clone https://github.com/Sarim043/Web-App.git
cd Web-App

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

### 3. Execution
```bash
python app.py
```
Visit `http://127.0.0.1:5000` in your browser.

---

## ☁️ Azure Deployment & CI/CD

### Manual Creation
1. Create a **Web App** in the Azure Portal.
2. Select **Python 3.11** as the runtime and **Linux** as the OS.
3. In the **Deployment Center**, connect your GitHub account and select this repository.

### CI/CD Pipeline (Automated)
The file `.github/workflows/main_sarimflaskapp.yml` handles the deployment:
1. **Build Stage**: Sets up Python, installs dependencies, and packages the app.
2. **Deploy Stage**: Uses Azure Login and WebApps Deploy actions to push the latest code to the production slot.

### Deployment Status
*(Placeholder for Screenshot: Navigate to Azure Portal > App Service > Deployment Center to view logs)*
> **Note**: Successful deployment is indicated by a "Success" flag in both GitHub Actions and the Azure Deployment Center.

---

## 🩺 Monitoring & Troubleshooting
- **Logs**: Access logs via Azure Portal > **Log Stream** to debug runtime errors.
- **SSH**: Use the **SSH** tool in Azure Portal to execute commands directly on the Linux container.
- **Configuration**: Ensure `SCM_DO_BUILD_DURING_DEPLOYMENT` is set to `true` in Azure App Settings for automatic `pip install`.

---

## ✅ Intern Assignment Deliverables Checklist
- [x] Python Source Code (Flask)
- [x] Responsive Frontend (HTML/CSS)
- [x] `requirements.txt` for dependencies
- [x] `README.md` with complete documentation
- [x] Successful Deployment to Azure
- [x] Automated CI/CD via GitHub Actions

---
**Developer**: Sarim | **Assignment**: Azure App Service Deployment 
