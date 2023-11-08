[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Actions Status](https://github.com/moneybox-ai/django-moneybox/workflows/CI/badge.svg)](https://github.com/moneybox-ai/django-moneybox/actions)
[![Language](https://img.shields.io/badge/language-Python-blue)](https://www.python.org/)
[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/downloads/release/python-380/)
[![Framework](https://img.shields.io/badge/framework-Django-green)](https://www.djangoproject.com/)
![Contributors](https://img.shields.io/badge/Contributors-6-blue)

## Django Moneybox [under developing]

Django Moneybox is a REST API service for tracking and managing personal finances. It provides endpoints for creating, updating, and deleting income and expense transactions, as well as for retrieving reports on financial activity. The application is secured with encryption key handling and employs Celery for task management.

- [Description of the project](https://github.com/moneybox-ai/django-moneybox/docs/description.md)


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

### Technical description

- [Documentation](https://github.com/moneybox-ai/django-moneybox/docs/tech_description.md)

### Demo

Explore the functionality of Django Moneybox on our development server. Test, save, and manage your financial activities.
The API documentation can be accessed through Swagger UI.
- [Demo](http://moneybox.ddns.net/api/v1/schema/swagger-ui/)

### Contributing

Contributions to Django Moneybox are welcome!

<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/stanislav-losev"><img src="https://avatars.githubusercontent.com/u/57747493?v=4" width="100px;" alt="stanislav-losev"/><br /><sub><b>stanislav-losev</b></sub></a><br /></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/error0x001"><img src="https://avatars.githubusercontent.com/u/71964062?v=4" width="100px;" alt="error0x001"/><br /><sub><b>error0x001</b></sub></a><br /></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Faithdev21"><img src="https://avatars.githubusercontent.com/u/119350657?v=4" width="100px;" alt="Egor Loskutov"/><br /><sub><b>Egor Loskutov</b></sub></a><br /></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tanja-ovc"><img src="https://avatars.githubusercontent.com/u/85249138?v=4" width="100px;" alt="Таня Овчинникова"/><br /><sub><b>Таня Овчинникова</b></sub></a><br /></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Eugene-Bykovsky"><img src="https://avatars.githubusercontent.com/u/45427494?v=4" width="100px;" alt="Evgenii Bykovskii"/><br /><sub><b>Evgenii Bykovskii</b></sub></a><br /></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ArtemWhiter"><img src="https://avatars.githubusercontent.com/u/95350023?v=4" width="100px;" alt="Артем Гронский"/><br /><sub><b>Артем Гронский</b></sub></a><br /></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/maxahist"><img src="https://avatars.githubusercontent.com/u/97408215?v=4" width="100px;" alt="maxahist"/><br /><sub><b>maxahist</b></sub></a><br /></td>
    </tr>
  </tbody>
</table>

### License

Django Moneybox is released under the MIT License. See the LICENSE file for details.
