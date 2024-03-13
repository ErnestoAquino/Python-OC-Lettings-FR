Docker Usage
=============

This segment of the documentation explains how to work with Docker to handle the application. To start, it's necessary to prepare a ``.env`` file that contains the essential environment variables for the application's configuration. Make sure to create a ``.env`` file with the following content:

.. code-block:: bash

    # Content of the .env file
    SENTRY_DSN=your_sentry_dsn
    SECRET_KEY='your_secret_key'

Creation of the Docker Image
----------------------------

Once the ``.env`` file is prepared, you can proceed to create a Docker image of the application by executing the following command in the terminal:

.. code-block:: bash

    docker build -t oc-lettings .

This command builds a Docker image labeled as ``oc-lettings`` based on the Dockerfile present in the current directory.

Running the Docker Container
----------------------------

To start a container based on the created image, use the command:

.. code-block:: bash

    docker run -p 8000:8000 --env-file .env oc-lettings

This command launches the container, maps the host's port 8000 to the container's port 8000, and uses the ``.env`` file to configure the necessary environment variables for the application.

Accessing the Application
-------------------------

With the container running, the application will be accessible through the browser at `http://localhost:8000`. Here you can interact with the application's user interface and use its functionalities.

This process facilitates the management of the application in a Docker environment, ensuring consistent configuration and deployment.
