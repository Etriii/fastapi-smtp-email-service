# FastAPI Emailer

This is a simple email sender service built with **FastAPI** and Python's **smtplib** for sending emails. It exposes an API endpoint (`/api/email/send-email`) that allows you to send emails through an SMTP server (e.g., Gmail). 

## Features
- Send custom emails with a subject and body
- Uses **SMTP** (works with Gmail, or other SMTP providers)
- Supports plain text emails
- Configurable with environment variables

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/fastapi-emailer.git
cd fastapi-emailer
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'

(Ensure to enable it during dependency updates and utilize it as an interpreter)
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables (.env file):
```bash
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=youremail@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

5. Run the FastAPI application:
```bash
uvicorn app.main:app --reload
```
6. Access the email endpoint at:
```bash
POST /api/email/send-email
```
7. Example Request using postman
```bash
{
  "to": "recipient@example.com",
  "subject": "Test Email",
  "body": "Hello from Alex!"
}
```
