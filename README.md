[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Actions Status](https://github.com/moneybox-ai/django-moneybox/workflows/CI/badge.svg)](https://github.com/moneybox-ai/django-moneybox/actions)
[![Language](https://img.shields.io/badge/language-Python-blue)](https://www.python.org/)
[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/downloads/release/python-380/)
[![Framework](https://img.shields.io/badge/framework-Django-green)](https://www.djangoproject.com/)
![Contributors](https://img.shields.io/badge/Contributors-6-blue)

## Django Moneybox [under developing]

Django Moneybox is a REST API service for tracking and managing personal finances. It provides endpoints for creating, updating, and deleting income and expense transactions, as well as for retrieving reports on financial activity. The application is secured with encryption key handling and employs Celery for task management.

> [More details](https://github.com/moneybox-ai/django-moneybox/docs/description.md)


### Installation

Django Moneybox can be effortlessly set up using Docker and Docker Compose. Follow these steps to get your application running quickly:

1. Ensure you have Docker and Docker Compose installed on your system.

2. Clone the repository:

   ```bash
   git clone https://github.com/moneybox-ai/django-moneybox.git
   cd django-moneybox
   ```

3. Run the following command to start the application and its dependencies in detached mode:

    ```bash
    docker-compose up -d
    ```

This command will launch Django Moneybox, a PostgreSQL database, and other services defined in the docker-compose.yml file.

### Contributing

Contributions to Django Moneybox are welcome! Please refer to the CONTRIBUTING.md file for guidelines.

### License

Django Moneybox is released under the MIT License. See the LICENSE file for details.
