Continuous Integration and Deployment (CI/CD) with GitHub Actions
==================================================================

In this project, Continuous Integration (CI) and Continuous Deployment (CD) are managed through GitHub Actions, configured in the file located at ``.github/workflows/django.yml``. This setup allows for the automation of testing, building, and deployment of the project each time a push or a pull request is made to the ``master`` branch.

CI/CD Configuration
---------------------

The YAML file specifies the steps that are followed to ensure that each code change maintains quality and is deployable.

Workflow Steps
---------------

1. **Dependency Installation:** Initially, pip is updated, and the project's required dependencies, specified in ``requirements.txt``, are installed.

2. **Linter with flake8:** To ensure code quality, flake8 is run. This step checks for compliance with Python's style guides.

3. **Tests and Coverage:** Automated tests are run with pytest, and a coverage report is generated. It's essential for the test coverage to be at 80% or above; otherwise, this step will fail, indicating a need to improve tests.

4. **Login to Docker Hub:** This step involves authentication to Docker Hub using secure credentials stored in GitHub's secret settings, allowing Docker images to be pushed.

5. **Docker Image Building:** A Docker image of the project is built, tagging it with the current commit's SHA. This facilitates the traceability of container versions.

6. **Image Tagging:** Subsequently, the image is tagged as ``latest``, indicating that it is the most recent version available.

7. **Docker Images Push:** The Docker images, both the specific commit version and the one tagged as ``latest``, are pushed to Docker Hub, making them accessible for deployment.

8. **Deployment:** If the changes come from the ``master`` branch, an automatic deployment is performed through a webhook on Render, previously set up in the GitHub secrets.

This CI/CD setup ensures that the project is rigorously tested and automatically deployed under the highest standards of quality and efficiency, facilitating a continuous and uninterrupted workflow for the development team.
