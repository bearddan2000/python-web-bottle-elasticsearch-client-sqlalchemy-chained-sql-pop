import os, csv
from settings import COLUMN_NAME

INDEX_NAME = os.environ["INDEX_NAME"]

def main():
    colums = [
        COLUMN_NAME['col_0']['name'],
        COLUMN_NAME['col_1']['name'],
        COLUMN_NAME['col_2']['name']
    ]    
    with open('{}.csv'.format(INDEX_NAME), "r") as fi:
        reader = csv.DictReader(
            fi, fieldnames=colums, delimiter=",", quotechar='"'
        )

        # This skips the first row which is the header of the CSV file.
        next(reader)

        actions = []
        for row in reader:
            csv_doc = {
                COLUMN_NAME['col_0']['name']: int(row[COLUMN_NAME['col_0']['name']]),
                COLUMN_NAME['col_1']['name']: row[COLUMN_NAME['col_1']['name']],
                COLUMN_NAME['col_2']['name']: row[COLUMN_NAME['col_2']['name']]
            }
            actions.append(csv_doc)

        return actions

DOC = main()