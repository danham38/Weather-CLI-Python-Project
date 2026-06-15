# Weather CLI Project

A Python command-line weather application that takes latitude and longitude inputs, validates them, and prepares weather data to be fetched and displayed through a clean CLI interface.

This project is being built to practise Python fundamentals, project structure, error handling, testing, and API-based application design.

## Features

* Command-line interface using Python
* Latitude and longitude input validation
* Custom exception classes for invalid coordinates
* Organised project structure using packages and modules
* Unit testing with `pytest`
* Designed for future integration with a weather API provider

## Project Structure

```text
weather-cli-project/
├── src/
│   └── weather_cli/
│       ├── __init__.py
│       ├── cli.py
│       ├── errors.py
│       ├── models.py
│       ├── formatting/
│       ├── providers/
│       └── services/
├── tests/
│   └── test_validation.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/weather-cli-project.git
cd weather-cli-project
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the CLI

Run the application from the project root:

```bash
PYTHONPATH=src python -m weather_cli.cli --lat 51.5072 --lon -0.1276
```

Example coordinates:

```text
London: 51.5072, -0.1276
```

## Running Tests

Run the test suite with:

```bash
pytest
```

## Validation Rules

Latitude must be between:

```text
-90 and 90
```

Longitude must be between:

```text
-180 and 180
```

Invalid values raise custom validation errors.


## Technologies Used

* Python
* pytest
* Git
* GitHub
