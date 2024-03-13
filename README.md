
# Summary
Orange County Lettings website.

## Local Development

### Prerequisites
- GitHub account with read access to this repository.
- Git CLI.
- SQLite3 CLI.
- Python interpreter, version 3.9 or higher.
- Django secret key.
- The DSN for Sentry.

It's necessary to configure some environment variables before starting the project. These variables are required for the correct functioning and execution of the application in your local environment.

```bash
# Copy the following code to set up the environment variables
export SENTRY_DSN='your_sentry_dsn'
export SECRET_KEY='your_django_secret_key'
```
Replace 'your_sentry_dsn' with your Sentry DSN and 'your_django_secret_key' with your Django secret key.

### Clone the repository
```bash
cd /path/to/project
git clone https://github.com/ErnestoAquino/Python-OC-Lettings-FR.git
```

### Create and activate the virtual environment
```bash
cd /path/to/Python-OC-Lettings-FR
python -m venv env
source env/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the site
Activate the virtual environment and install dependencies if not done already. Declare the environment variables for Django and Sentry, then collect the static files and launch the server:

```bash
export SECRET_KEY='your_secret_key'
export SENTRY_DSN='dsn_for_sentry'
python manage.py collectstatic --noinput
python manage.py runserver
```
Go to http://localhost:8000 in a browser to confirm that the site is working correctly.

### Linting
```bash
flake8
```

### Unit tests
```bash
pytest
```
To see test coverage:
```bash
pytest --cov
```

### Admin panel
Go to http://localhost:8000/admin and log in with the user `admin`, password `Abc1234!`.
