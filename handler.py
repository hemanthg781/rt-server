# Handler for AWS Lambda
import serverless_wsgi
from rt.wsgi import application


def handle(event, context):

    if 'django_command' in event:
        return execute(event['django_command'])

    return serverless_wsgi.handle_request(application, event, context)


def execute(cmd):
    from django.core import management
    management.call_command(cmd)


if __name__ == "__main__":
    execute("migrate")
