import csv
import datetime as dt

csvDbHeader = ['id', 'name', 'date', 'time', 'type', 'notes']


def load():
    all_events = []
    with open('event_getter_db.csv', newline='') as csvfile:
        for row in csvfile:
            all_events.append(row)
    all_events.pop(0)
    for event in range(len(all_events)):
        all_events[event] = all_events[event].split(",")
        all_events[event] = {csvDbHeader[i]:all_events[event][i] for i in range(len(csvDbHeader))}
    return all_events


def write(data):
    with open('event_getter_db.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csvDbHeader)
        for row in data:
            writer.writerow(row)
    return True


def get_events_of_type(event_type, all_events):
    selected_event_list = []
    for event in all_events:
        if event['type'] == event_type:
            selected_event_list.append(event)
    return selected_event_list


def display_event(event_list):
    event_list = sort_events(event_list)
    for event in range(len(event_list)):
        for key_index in range(len(event_list[event])):
            print(csvDbHeader[key_index], " : ", event_list[event][csvDbHeader[key_index]])


def sort_events(events_array):
    array_to_sort = []
    for event in events_array:
        array_to_sort.append([event, time_to_secs(event['time'])])
    array_to_sort.sort(key=lambda k: k[1])
    for event in range(len(array_to_sort)):
        array_to_sort[event] = array_to_sort[event][0]
    return array_to_sort


def time_to_secs(time):
    time = time.split(':')
    time = int(time[0])*3600 + int(time[1])*60
    return time
