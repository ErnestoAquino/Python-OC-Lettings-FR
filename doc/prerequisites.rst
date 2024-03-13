.. _prerequisites:

Prerequisites
=============


- A GitHub account with read access to this repository
- Git CLI
- SQLite3 CLI
- Python interpreter, version 3.9 or higher
- The Django secret key
- The DSN for Sentry

In the rest of the documentation on local development, it is assumed that the ``python`` command in your OS shell executes the above Python interpreter (unless a virtual environment is activated).
It's necessary to set up some environment variables before starting the project. These variables are required for the proper execution and operation of the application in your local environment.

.. code-block:: bash

    export SENTRY_DSN='your_sentry_dsn'
    export SECRET_KEY='your_django_secret_key'

Remember to replace 'your_sentry_dsn' with your Sentry DSN and 'your_django_secret_key' with your Django secret key. These environment variables are critical for the application's configuration.