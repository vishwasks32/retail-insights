from setuptools import setup, find_packages

setup(
    name='retail_insights',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'streamlit',
        'pandas',
        'sqlalchemy',
        'boto3',
        'python-dotenv',
        'python-decouple',
    ],
    entry_points={
        'console_scripts': [
            'retail-insights=app.streamlit_app:main',
        ],
    },
)
