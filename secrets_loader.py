import json
from django.core.exceptions import FieldDoesNotExist, ImproperlyConfigured

SECRETS_FILE_NAME = 'secrets.json'


def load_secrets(base_dir):
    try:
        with open(base_dir / SECRETS_FILE_NAME) as f:
            secrets = json.loads(f.read())
        return secrets
    except FileNotFoundError:
        error_msg = f"'{SECRETS_FILE_NAME}' file does not exist!"
        raise FieldDoesNotExist(error_msg)


def get_secret(secrets, setting):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = f"Set the '{setting}' in the '{SECRETS_FILE_NAME}' file!"
        raise ImproperlyConfigured(error_msg)