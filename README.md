
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


# Deployment
This project uses an automated workflow that includes building Docker images, storing these images on Docker Hub, and automatic deployment on Render. Here's a high-level overview of the deployment process, necessary requirements, and steps for a successful deployment.

## High-Level Overview
- **Docker Image Building**: Each time a push is made to the master branch, GitHub Actions takes charge of building a Docker image based on the current state of the repository. This image is tagged with the corresponding commit hash and also with the latest tag.

- **Storing on Docker Hub**: The built image is uploaded to Docker Hub under the username specified in the repository secrets.

- **Deployment on Render**: Using a webhook provided by Render, the automated system notifies Render about the new image to deploy it automatically. Render is configured to deploy the image tagged as latest.

## Required Configuration
For the deployment to work correctly, the following are required:

- **Docker Hub Account**: Needed to store the Docker images.
- **Render Account**: For deploying the application.
- **GitHub Secrets Configuration**: It's necessary to configure the following secrets in the GitHub repository:
  - `DOCKER_USERNAME`: Your Docker Hub username.
  - `DOCKER_PASSWORD`: Your Docker Hub password.
  - `RENDER_DEPLOY_HOOK`: The webhook provided by Render to trigger the deployment.

## Deployment Steps
1. Ensure all secrets are correctly set up in GitHub.
2. Make changes to your code and push to the master branch. This triggers the GitHub Actions workflow that builds and uploads the Docker image, and then notifies Render to deploy the new image.
3. Monitor the GitHub Actions workflow to ensure it completes successfully.
4. Check the deployment on Render. Once GitHub Actions notifies Render through the webhook, Render will automatically deploy the new image. You can monitor the deployment status directly in your Render dashboard.
