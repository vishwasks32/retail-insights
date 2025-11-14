import sqlite3
import pandas as pd

try:
    from sqlalchemy import create_engine
except ImportError:
    create_engine = None

# Database loader
class DBLoader:
    def load(self, df, connection_string, table_name):
        """
        Load a pandas DataFrame into a SQLite3 database.

        Args:
            df (pd.DataFrame): DataFrame to load.
            connection_string (str): Path to the SQLite3 database file.
            table_name (str): Name of the table to write data into.
        """
        with sqlite3.connect(connection_string) as conn:
            df.to_sql(table_name, conn, if_exists='replace', index=False)

    def load_mysql(self, df, connection_params, table_name):
        """
        Load a pandas DataFrame into a MySQL database.

        Args:
            df (pd.DataFrame): DataFrame to load.
            connection_params (dict): Dictionary with MySQL connection parameters (host, user, password, database). If any are missing, will use environment variables.
            table_name (str): Name of the table to write data into.
        """
        import os
        if create_engine is None:
            raise ImportError("sqlalchemy is not installed. Please install it to use this method.")

        user = connection_params.get('user') or os.getenv('MYSQL_USER')
        password = connection_params.get('password') or os.getenv('MYSQL_PASSWORD')
        host = connection_params.get('host') or os.getenv('MYSQL_HOST', 'localhost')
        port = connection_params.get('port') or int(os.getenv('MYSQL_PORT', 3306))
        database = connection_params.get('database') or os.getenv('MYSQL_DATABASE')

        if not all([user, password, host, port, database]):
            raise ValueError("Missing MySQL connection parameters. Please provide them in connection_params or as environment variables.")

        engine_str = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        engine = create_engine(engine_str)
        df.to_sql(table_name, engine, if_exists='replace', index=False)