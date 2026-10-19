
# Employee Management System

## Project Overview
The Employee Management System is a Python-based application that manages employee records using an SQLite database. It also integrates a weather API to fetch current weather information for Nagpur.

## Features
- Add employee records
- View all employee records
- Update employee salary
- Delete employee records
- Fetch Nagpur weather using a REST API
- Save API response data in JSON format
- Log application activities and errors

## Technologies Used
- Python
- SQLite
- REST API
- JSON
- Requests library
- Logging

## Project Structure
- `main.py` - Main application and menu
- `database/db.py` - Database connection and table creation
- `api/weather_api.py` - Weather API integration
- `api/weather.json` - Saved weather data
- `utils/logger.py` - Logging configuration
- `requirements.txt` - Project dependencies
- `app.log` - Application log file

## Installation
1. Install Python.
2. Create and activate a virtual environment.
3. Install dependencies:

   `pip install -r requirements.txt`

## Run the Project
Run the following command from the project folder:

`python main.py`

## Database
Employee records are stored in the SQLite database file `employees.db`.

## API
The project uses the Open-Meteo API to retrieve current temperature and relative humidity for Nagpur.
