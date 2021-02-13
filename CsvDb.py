import csv


def load():
    all_events = []
    with open('event_getter_db.csv', newline='') as csvfile:
        for row in csvfile:
            all_events.append(row)
    all_events.pop(0)
    return all_events


def get_weekly(all_events):
    weeklys_list = []
    for event in range(len(all_events)):
        all_events[event] = all_events[event].split(",")
    for event in all_events:
        if event[4] == 'weekly':
            weeklys_list.append(event)
    return weeklys_list

