[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Django Moneybox [under developing]

Django Moneybox is a REST API service for tracking and managing personal finances. It provides endpoints for creating,
updating, and deleting income and expense transactions, as well as for retrieving reports on financial activity.

### Installation

To run Django Moneybox, you must have Python 3 installed on your system. Clone the repository and create a virtual
environment:

```bash
git clone https://github.com/moneybox-ai/django-moneybox.git
cd django-moneybox
python3 -m venv env
source env/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create the database tables:

```bash
python manage.py migrate
```

Start the development server:

```bash
python runserver
```

You can now access the API at http://localhost:8000.

### Installing redis in container

```bash
docker run -p 127.0.0.1:16379:6379 --name redis-celery -d redis
```

### Launch Celery

Open new bash window

Starting Celery

```bash
celery -A moneybox worker -l info
```

Open new bash window

Starting Celery periodic task

```bash
celery -A moneybox beat -l info
```

### Contributing

Contributions to Django Moneybox are welcome! Please refer to the CONTRIBUTING.md file for guidelines.

### License

Django Moneybox is released under the MIT License. See the LICENSE file for details.
