'''
Train Classfier loads the data from the database file and tokenizes them. Model is build using cross validation. Finally the model is being saved to a pickle File.  
'''
import pickle
import re
import sys
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.metrics import classification_report
from sqlalchemy import create_engine
import pandas as pd

from sklearn.pipeline import FeatureUnion, Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.utils import parallel_backend


from sklearn.model_selection import train_test_split

import nltk


nltk.download(['punkt', 'wordnet', 'stopwords', 'omw-1.4'])
lemmatizer = WordNetLemmatizer()


def load_data(database_filepath):
    '''reads sqlite data from the database_filepath and loads it into an pandas dataframe'''
    engine = create_engine("sqlite:///"+database_filepath)
    df = pd.read_sql_table(
        'drp',
        con=engine)
    X = df.message
    y = df[df.columns[4:]]
    category_names = y.columns
    return X, y, category_names


def tokenize(text):
    ''''extract only text remove points and whitespace and to lower'''
    text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
    # tokenize
    words = word_tokenize(text)
    # remove stopwords
    words = [w for w in words if w not in stopwords.words("english")]
    # lemmatize

    clean_tokens = [lemmatizer.lemmatize(word) for word in words]
    return clean_tokens


def build_model():
    '''builds the pipeline and optimizes the hyperparamater'''

    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(RandomForestClassifier()))])

    parameters = {'vect__min_df': [1, 5],
                  'tfidf__use_idf': [True, False],
                  'clf__estimator__n_estimators': [10, 25],
                  'clf__estimator__min_samples_split': [2, 4]}

    cv = GridSearchCV(pipeline, param_grid=parameters, n_jobs=-1, verbose=2)

    return cv


def evaluate_model(model, X_test, Y_test, category_names):
    '''evaluates the model and prints a classiifcation report'''

    y_pred = model.predict(X_test)
    report = classification_report(Y_test, y_pred, target_names=category_names)
    print(report)


def save_model(model, model_filepath):
    """
    Save model to a pickle file
    """
    with open(model_filepath, 'wb') as file:
        pickle.dump(model, file)


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(
            X, Y, test_size=0.2)

        with parallel_backend('multiprocessing'):

            print('Building model...')
            model = build_model()

            print('Training model...')
            model.fit(X_train, Y_train)

            print('Evaluating model...')
            evaluate_model(model, X_test, Y_test, category_names)

            print('Saving model...\n    MODEL: {}'.format(model_filepath))
            save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '
              'as the first argument and the filepath of the pickle file to '
              'save the model to as the second argument. \n\nExample: python '
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()
