# FastAPI Send Email with Background Tasks

This repository demonstrates how to send emails asynchronously using FastAPI's background tasks. It provides a clean and efficient implementation for handling email sending in the background without blocking the main thread.

## Features

- **FastAPI Framework**: Lightweight and fast Python web framework.
- **Asynchronous Email Sending**: Utilizing FastAPI's `BackgroundTasks` to send emails without affecting the request-response cycle.
- **Ease of Integration**: Simple and modular structure, making it easy to integrate into your projects.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/shahramsamar/FastApi-Send-Email-background-tasks.git
   cd FastApi-Send-Email-background-tasks
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Update the email configuration in `config.py`:

   ```python
   EMAIL_HOST = "smtp.example.com"
   EMAIL_PORT = 587
   EMAIL_USERNAME = "your_email@example.com"
   EMAIL_PASSWORD = "your_password"
   EMAIL_FROM = "your_email@example.com"
   EMAIL_FROM_NAME = "Your Name"
   ```

2. Run the application:

   ```bash
   uvicorn main:app --reload
   ```

3. Send a POST request to the email endpoint. For example, using `curl`:

   ```bash
   curl -X POST "http://127.0.0.1:8000/send-email" \
        -H "Content-Type: application/json" \
        -d '{"email_to": "recipient@example.com", "subject": "Test Email", "body": "Hello, this is a test email!"}'
   ```

4. The email will be sent in the background, and the API will respond immediately.

## File Structure

```
FastApi-Send-Email-background-tasks/
├── main.py         # Entry point of the application
├── config.py       # Configuration settings
├── email_utils.py  # Email sending utility functions
├── requirements.txt # Dependencies
└── README.md       # Documentation
```

## Dependencies

- **FastAPI**: High-performance web framework for building APIs.
- **Jinja2**: For email templates.
- **aiofiles**: Async file operations.
- **aiosmtplib**: Async SMTP client for sending emails.

Install dependencies with:

```bash
pip install fastapi jinja2 aiofiles aiosmtplib
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

---

### Author

[Shahram Samar](https://github.com/shahramsamar)

![Alt](https://repobeats.axiom.co/api/embed/eabe6508a91fa38b4ace0060919094363916f544.svg "Repobeats analytics image")
