import os
import pandas as pd

# CSV Extractor implementation
class CSVExtractor:
    def extract(self, file_path):
        # Construct the full path to the data/raw folder
        base_dir = os.path.dirname(os.path.abspath(__file__))
        raw_data_dir = os.path.join(base_dir, '..', '..', '..', 'data', 'raw')
        raw_data_dir = os.path.normpath(raw_data_dir)
        csv_path = os.path.join(raw_data_dir, file_path)

        import pandas as pd
        try:
            if not os.path.exists(csv_path):
                return None
            # Check if file is empty
            if os.path.getsize(csv_path) == 0:
                return pd.DataFrame()
            data = pd.read_csv(csv_path)
            # Replace NaN with empty string for compatibility with tests
            data = data.where(pd.notnull(data), "")
            return data
        except Exception as e:
            print(f"Error reading {csv_path}: {e}")
            return None
