
# Retail Insights

A modular ETL and analytics platform for retail data, featuring extraction, transformation, loading, and a Streamlit dashboard.

## Project Structure

```
.
├── data/
│   ├── raw/         # Raw input data (CSV files)
│   └── processed/   # Processed/cleaned data
├── src/
│   ├── app/         # Streamlit app and UI components
│   ├── config/      # Configuration and settings
│   ├── extract/     # Data extraction modules (CSV, API, DB)
│   ├── load/        # Data loading modules (file, database)
│   ├── pipeline/    # ETL pipeline runner
│   ├── transform/   # Data cleaning, validation, feature engineering
│   └── retail_insights.egg-info/ # Packaging metadata
├── tests/           # Unit and integration tests
├── requirements.txt # Python dependencies
├── setup.py         # Python package setup
├── Dockerfile       # Containerization
└── .env             # Environment variables
```

## Quick Start

1. **Install dependencies:**
	```sh
	pip install -r requirements.txt
	```

2. **Run the ETL pipeline:**
	```sh
	python src/pipeline/etl_runner.py
	```

3. **Launch the Streamlit dashboard:**
	```sh
	streamlit run src/app/streamlit_app.py
	```

## Configuration

- Copy `.env.example` to `.env` and update values as needed.
- Key environment variables:
  - `APP_ENV` (dev/prod)
  - `SQLITE_DB_FILE` (for dev)
  - `DB_CONNECTION_STRING`, `API_KEY` (as needed)

## Testing

Run all unit tests with:
```sh
pytest
```

## Features

- Modular ETL pipeline (extract, transform, load)
- Data extraction from CSV, API, or database
- Data cleaning, validation, and feature engineering
- Streamlit dashboard for data visualization and quality reporting
- Configurable for development and production environments

## Docker

Build and run the app in a container:
```sh
docker build -t retail-insights .
docker run -p 8501:8501 --env-file .env retail-insights
```

---

For more details, see the source code in `src/` and example data in `data/`.
