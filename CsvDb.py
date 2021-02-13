import csv

csvDbHeader = ['id', 'name', 'date', 'time', 'type', 'notes']


def load():
    all_events = []
    with open('event_getter_db.csv', newline='') as csvfile:
        for row in csvfile:
            all_events.append(row)
    all_events.pop(0)
    for event in range(len(all_events)):
        all_events[event] = all_events[event].split(",")
        for item in range(len(all_events[event])):
            all_events[event][item] = {csvDbHeader[item]:all_events[event][item]}
    return all_events





