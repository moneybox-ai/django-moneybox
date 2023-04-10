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

### Credits

This project was created by Moneybox AI with the assistance of Chat GPT.

### Contributing

Contributions to Django Moneybox are welcome! Please refer to the CONTRIBUTING.md file for guidelines.

### License

Django Moneybox is released under the MIT License. See the LICENSE file for details.
