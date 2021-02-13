import csv


def load():

    with open('event_getter_db.csv', newline='') as csvfile:
        for row in csvfile:
            print(row)

