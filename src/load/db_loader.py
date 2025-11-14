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
            connection_params (dict): Dictionary with MySQL connection parameters (host, user, password, database).
            table_name (str): Name of the table to write data into.
        """
        if create_engine is None:
            raise ImportError("sqlalchemy is not installed. Please install it to use this method.")

        user = connection_params.get('user')
        password = connection_params.get('password')
        host = connection_params.get('host', 'localhost')
        port = connection_params.get('port', 3306)
        database = connection_params.get('database')

        engine_str = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        engine = create_engine(engine_str)
        df.to_sql(table_name, engine, if_exists='replace', index=False)