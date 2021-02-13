import csv

csvDbHeader = ['id', 'name', 'date', 'time', 'type', 'notes']


def load():
    all_events = []
    with open('event_getter_db.csv', newline='') as csvfile:
        for row in csvfile:
            all_events.append(row)
    all_events.pop(0)
    return all_events


def write(data):
    with open('event_getter_db.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csvDbHeader)
        for row in data:
            writer.writerow(row)
    return True

def get_event_type(event_type, all_events):
    selected_event_list = []
    for event in range(len(all_events)):
        all_events[event] = all_events[event].split(",")
    for event in all_events:
        if event[4] == event_type:
            selected_event_list.append(event)
    return selected_event_list
