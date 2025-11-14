

import os
import boto3
import json
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '.env'))

class Settings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Settings, cls).__new__(cls)
            cls._instance.env = os.getenv('APP_ENV', 'dev')
            cls._instance.db_uri = cls._instance._get_db_uri()
        return cls._instance

    def _get_db_uri(self):
        if self.env == 'dev':
            # Use SQLite for dev, path from .env or default to processed/dev.db
            db_file = os.getenv('SQLITE_DB_FILE', 'dev.db')
            db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data', 'processed', db_file)
            db_path = os.path.normpath(db_path)
            return f'sqlite:///{db_path}'
        elif self.env == 'prod':
            # Use MySQL for prod, fetch credentials from AWS Secrets Manager
            secret_name = os.getenv('MYSQL_SECRET_NAME', 'prod/mysql/credentials')
            region_name = os.getenv('AWS_REGION')
            if not region_name:
                raise Exception('AWS_REGION environment variable must be set for production')
            creds = self._get_mysql_credentials_from_aws(secret_name, region_name)
            if creds:
                return f"mysql+pymysql://{creds['username']}:{creds['password']}@{creds['host']}:{creds['port']}/{creds['dbname']}"
            else:
                raise Exception('Could not fetch MySQL credentials from AWS Secrets Manager')
        else:
            raise ValueError(f"Unknown environment: {self.env}")

    def _get_mysql_credentials_from_aws(self, secret_name, region_name):
        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=region_name
        )
        try:
            get_secret_value_response = client.get_secret_value(SecretId=secret_name)
            secret = get_secret_value_response['SecretString']
            return json.loads(secret)
        except Exception as e:
            print(f"Error fetching secret from AWS: {e}")
            return None

settings = Settings()
