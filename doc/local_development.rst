Local Development
=================
Before starting, please make sure you meet the :ref:`prerequisites`.

Clone the repository
~~~~~~~~~~~~~~~~~~~~
.. code:: bash

    cd /path/to/put/project/in
    git clone https://github.com/ErnestoAquino/Python-OC-Lettings-FR.git

Create the virtual environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code:: bash

    cd /path/to/Python-OC-Lettings-FR
    python -m venv env

Activate the virtual environment

.. code:: bash

     source env/bin/activate

Install the requirements

.. code:: bash

     pip install -r requirements.txt

To deactivate the environment

.. code:: bash

    deactivate

Run the site
~~~~~~~~~~~~
Navigate to the folder:

.. code:: bash

    cd /path/to/Python-OC-Lettings-FR

Activate the virtual environment

.. code:: bash

    source env/bin/activate

Install the requirements

.. code:: bash

    pip install -r requirements.txt

Declare the environment variables for Django and Sentry

.. code:: bash

    export SECRET_KEY='your_secret_key'
    export SENTRY_DSN='dsn for sentry'

Collect the static files

.. code:: bash

    python manage.py collecstatic

Run the server

.. code:: bash

    python manage.py runserver

Go to ``http://localhost:8000`` in a browser.
Confirm that the site works and that it is possible to navigate (you should see several profiles ans listings).


Linting
~~~~~~~
.. code:: bash

    cd /path/to/Python-OC-Lettings-FR
    source env/bin/activate
    flake8

The flake8 configuration is available in the ``setup.cfg`` file


Unit Tests
~~~~~~~~~~
.. code:: bash

    cd /path/to/Python-OC-Lettings-FR
    source env/bin/activate
    pytest

The pytest configuration is available in the ``setup.cfg`` file.
You can view the test coverage using the command:

.. code:: bash

    pytest --cov

The configuration is also available int the ``setup.cfg`` file. The test cover the three main applications:
- oc_lettings_site
- profiles
- lettings

The models, views and URLs have been tested.

Admin Panel
~~~~~~~~~~~
.. code:: bash

    Go to ``http://localhost:8000/admin``
    Log in with the user ``admin``, password ``Abc1234!``