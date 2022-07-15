# Disaster Response Pipeline Project

## 1. Installations

| Library      | Version | Link                                                 |
| ------------ | ------- | ---------------------------------------------------- |
| Python       | 3.9.0   | https://www.python.org/downloads/release/python-390/ |
| virtualenv   |         |                                                      |
| SQLAlchemy   | 1.4.39  |                                                      |
| pandas       | 1.4.3   |                                                      |
| numpy        | 1.23.1  |                                                      |
| nltk         | 3.7     |                                                      |
| scikit-learn | 1.1.1   |                                                      |
| plotly       | 5.9.0   |                                                      |
| Flask        | 2.1.3   |                                                      |

## 2. Project Motivation

## 3. File Descriptions

## 4. How to Interact with your project

### Run the app

navigate to app directory and run

```
python .\run.py
```

### Active the virtual environment

To active the virtual environment use the follwoing command

```
.\venv\Scripts\activate
```

### Deactive the virtual environment

To deactive the virtual environment use the follwoing command

```
deactive
```

### Preprocess data

In the data folder raw data for creating the sqllite database can be found. In order to create the database you have to navigate to the folder and execute the process_data.py with follwoing arguments:

- messages_filepath
- categories_filepath
- database_filepath

```
python .\process_data.py "disaster_messages.csv" "disaster_categories.csv" "sqlite:///drp.db"
```

### Instructions:

1. Run the following commands in the project's root directory to set up your database and model.

   - To run ETL pipeline that cleans data and stores in database
     `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
   - To run ML pipeline that trains classifier and saves
     `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Go to `app` directory: `cd app`

3. Run your web app: `python run.py`

4. Click the `PREVIEW` button to open the homepage
