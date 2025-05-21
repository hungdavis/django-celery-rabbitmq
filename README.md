# django-celery-rabbitmq

🚀 **Supercharged Django App for Heavy Processing Tasks such as Sending Email, File Uploads, Huge Report Generation... with Celery and RabbitMQ**

## 📋 Overview

Django-celery-rabbitmq is a demo project for high-performance Django project template optimized for handling heavy background processing, and fast response from backend using Celery and RabbitMQ (here CloudAMQP for easy setup).

### ✨ Key Features

* Quick response from view with background processing
* Efficient task distribution using Celery and RabbitMQ
* Scalable, high-performance architecture
* Secure, SSL/TLS-enabled message broker
* Real-time status updates for long-running tasks (future)
* Built-in task monitoring and logging (future)
* Dockerized setup for easy deployment (future)

## 📂 Project Structure

```
myproject/
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── celery.py
├── myapp/
│   ├── tasks.py
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── forms.py
├── templates/
│   └── registration/
│   └── users/
├── static/
│   └── images/
│   └── style.css
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
├── .env
├── README.md
└── LICENSE
```

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/hungdavis/django-celery-rabbitmq.git
cd django-celery-rabbitmq
```

### 2. Set Up the Environment

Create a `.env` file:

```
DJANGO_SECRET_KEY=your-secret-key
DATABASE_URL=postgres://user:password@localhost/dbname
CELERY_BROKER_URL=amqps://username:password@your-rabbitmq-host/vhost
CELERY_RESULT_BACKEND=rpc://
UPLOAD_FOLDER=/uploads/files/
MAX_UPLOAD_SIZE=100MB
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

### 6. Start Celery Worker

```bash
celery -A myproject worker --loglevel=info
```

### 7. Start Celery Beat

```bash
celery -A myproject beat --loglevel=info -S django
```
Note: -S means --schedule 

### 8. Run Django

```bash
cd myproject
python manage.py runserver
```
### 9. Test with user register 
Open http://localhost:8000/register-user
to test user form registration 


## 📦 Docker Setup (Recommended)

### Build and Run with Docker Compose

```bash
docker compose up -d --build
```

## 📊 Monitoring and Logging

* Use Flower for real-time task monitoring
* Integrate Prometheus and Grafana for in-depth performance analysis

## 📚 Learn More

* [Django Documentation](https://docs.djangoproject.com/)
* [Celery Documentation](https://docs.celeryproject.org/)
* [RabbitMQ Documentation](https://www.rabbitmq.com/)

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License.
