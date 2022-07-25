'''Process data reads the data from a csv file, clean them and wirtes them to a sqlite database.'''

import sys
from sqlalchemy import create_engine
import pandas as pd


def load_data(messages_filepath, categories_filepath):
    '''
    reads the data files in to a pandas dataframe
    '''
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    dataframe = messages.merge(categories, on='id')

    return dataframe


def clean_data(dataframe):
    '''cleans the dataframe and drops dublicate columns'''
    categories = dataframe['categories'].str.split(';', expand=True)
    row = categories.iloc[0]
    category_colnames = row.apply(lambda col: col[:-2])
    categories.columns = category_colnames

    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].apply(
            lambda col: int(col[-1:]))

    dataframe = dataframe.drop(columns='categories')

    dataframe = pd.concat([dataframe, categories], axis=1)

    dataframe = dataframe.drop_duplicates()

    return dataframe


def save_data(dataframe, database_filename):
    ''' stores the dataframe into and sqlite db '''
    # database_filename 'sqlite:///drp.db'
    engine = create_engine(database_filename)
    dataframe.to_sql('drp', engine, index=False)


def main():
    '''main function which is executed when the pyhton will be executed'''
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)

        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)

        print('Cleaned data saved to database!')

    else:
        print('Please provide the filepaths of the messages and categories '
              'datasets as the first and second argument respectively, as '
              'well as the filepath of the database to save the cleaned data '
              'to as the third argument. \n\nExample: python process_data.py '
              'disaster_messages.csv disaster_categories.csv '
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
