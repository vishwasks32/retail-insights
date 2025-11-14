# DB Extractor implementation
import pandas as pd
from sqlalchemy import create_engine

class DBExtractor:
    def extract(self, connection_string, table_name, query=None):
        """
        Extract data from a database using a SQLAlchemy connection string.
        If query is provided, it will be executed; otherwise, all rows from table_name are fetched.
        Returns a pandas DataFrame or None on failure.
        """
        try:
            engine = create_engine(connection_string)
            with engine.connect() as conn:
                if query:
                    df = pd.read_sql_query(query, conn)
                else:
                    df = pd.read_sql_table(table_name, conn)
            return df
        except Exception as e:
            print(f"Error extracting from DB: {e}")
            return None
