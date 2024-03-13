Deployment on Render
====================

The deployment of the site is carried out on the Render platform, offering an accessible and efficient production environment for the project.

Site Access
-----------

The deployed site is available at the following URL: `https://oclettingspro.onrender.com/ <https://oclettingspro.onrender.com/>`_. Here, users and stakeholders can interact with the most recent version of the application in a production environment.

Deployment Mechanism
--------------------

The deployment process uses a Render webhook, which allows for the automatic triggering of the site's deployment with the latest changes. This mechanism is particularly useful for implementing continuous updates and ensuring that the online version is always up-to-date.

The deployment webhook URL is kept secure and stored as a secret in the project repository under the variable ``RENDER_DEPLOY_HOOK``. This security approach prevents unauthorized access and facilitates the management of deployment configuration.

To trigger a deployment, the CI/CD process configured in GitHub Actions makes use of this secret, sending a request to the Render webhook following the successful completion of the integration and testing steps. This ensures that only site versions that have gone through a rigorous validation process are deployed, maintaining the quality and stability of the application in production.
