Integration of Logging and Sentry in the Project
================================================

The logging system configured in this project ensures that all errors and critical issues are captured, logged, and managed efficiently, thus facilitating the monitoring and analysis of incidents in the application.

Logging Configuration
----------------------

The logging system configuration is defined with a dictionary in Python, specifying formats, handlers, and loggers to capture and process logs in detail:

- **Formatters:** Define how log messages are formatted. The ``verbose`` formatter includes the severity level, the date and time of the event, the source module, and the log message, providing a wealth of detail for analysis.

- **Handlers:** Two handlers have been configured to manage the logs of errors (``level: 'ERROR'``):

    - **Log File:** Error messages are written to a file called ``django_errors.log``, using the ``verbose`` formatter to detail each entry.

    - **Sentry:** In addition, errors are sent to Sentry, an external error management service, using a special handler (``sentry_sdk.integrations.logging.EventHandler``). This allows for real-time monitoring of issues and swift resolution of incidents.

- **Loggers:** A logger for Django is specified, configured to use both handlers (``file`` and ``sentry``) for errors and more serious issues. This means that any error within Django will be recorded in the log file and sent to Sentry, offering a dual layer of error tracking.

This configuration of the logging system and integration with Sentry are essential for maintaining the health and stability of the application, allowing developers to proactively respond to any issues that may arise.
