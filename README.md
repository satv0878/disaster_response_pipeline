# Disaster Response Pipeline Project

## 1. Installations

| Library      | Version | Link                                                 |
| ------------ | ------- | ---------------------------------------------------- |
| Python       | 3.9.0   | https://www.python.org/downloads/release/python-390/ |
| SQLAlchemy   | 1.4.39  | https://www.sqlalchemy.org/                          |
| pandas       | 1.4.3   | https://pandas.pydata.org/                           |
| numpy        | 1.23.1  | https://numpy.org/                                   |
| nltk         | 3.7     | https://www.nltk.org/                                |
| scikit-learn | 1.1.1   | https://scikit-learn.org/stable/                     |
| plotly       | 5.9.0   | https://plotly.com/                                  |
| Flask        | 2.1.3   | https://flask.palletsprojects.com/en/2.1.x/          |

## 2. Project Motivation

This project process actual disaster messgas provided by a comapny called figure8. Response messages shall be categorized to the disaster category in order be able to react on messages sent during a disaster accordingly. That means when a disaster message is sent where a person asks for help because of a fire a only a medial emergency team is send. In order for a human to be able to initiate the appropiate help this project gives an exampole on how an ETL Pipline with NLP and ML can souport by pre-categorzing text messages.

Therefore the messages have been tokeized, lemmatized, removed stopwords using nltk. In order to create a model the tokenized messages the messages are vectorized. Occurence of each word in a tokenized message is counted. In a next step a TFidf Trasformer is used to normalize the occurance of the words. Therefore, the occurences of the word in a message is devided by the occurences of the word in all messages.

The Project follows the ETL Process. In the first step the data is being extracted from csv files, cleaned and stored in a sqlite database. In the next process stept the model is created. Based on the sqlite database the data is split in to the test and the train datasets.

Here the variables, which should be predicted are the desaster categories. The messages shall be categorized and serve as predictor variables. Whatsoever the raw messages cannot be used for predition there for they have to be preprocessed using a NLP pipeline:

1. Whitespaces, dots are being removed as well as all characters are trasformed to lowercases characters.
2. The sentences are tokenized.
3. Stopwords are being removed.
4. Words are transformed to its stem version using lemmatization.

The tokenized messages are then used to build a model. Thereofore the messages are vectorized and normalized based on the occurance of the words in all messages using TFIDF.

## 3. File Descriptions

- **train_classifiers.py:** Train Classfier loads the data from the database file and tokenizes them. Model is build using cross validation. Finally the model is being saved to a pickle File.

- **process_data.py:** Process data reads the data from a csv file, clean them and wirtes them to a sqlite database.

- **run.py:** Flask app which load the data from the db as well as the model from the pickle File. Grpah are created and dosplays on the index page.

- **go.html:** Contains the html after a query for categorizing a messages has been executed

- **master.html:** Contains the html for theindex page. such as nav bar and graphs

- **disaster_categries.csv:** raw data file for catergories
- **disaster_messages.csv:** raw data file with corresponding messages

- **drp.db:** Created sqlite database file

- **classifier.pkl:** Calculated model exported and pickel file

## 4. How to Interact with your project

### Run the app

navigate to app directory and run

```
python .\run.py
```

### Add virtual environment

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

#### Create Database

In the data folder raw data for creating the sqllite database can be found. In order to create the database you have to navigate to the folder and execute the process_data.py with follwoing arguments:

- messages_filepath
- categories_filepath
- database_filepath

```
python .\process_data.py "disaster_messages.csv" "disaster_categories.csv" "sqlite:///drp.db"
```

#### Create Pickle File

- database_filepath
- model_filepath

```
python .\train_classifier.py "../data/drp.db" "classifier.pkl"
```
