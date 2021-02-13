import InputQualifier as iq
import datetime as dt
import CsvDb as cda


def event_getter():
    action_type = iq.input_compare_w_string("Type in action or ask help (help): ",
                                            '', ['now', 'today', 'exit', 'ldall', 'write', 'help'])

    current_date = dt.date.today()
    current_week_day = current_date.weekday()
    current_time = dt.datetime.now().time()


    # responding to exit and help
    if action_type == 'help':
        print("'now' - gets all events within an hour of now, and says what event you're on \n"
              "'ldall' - gets all events expired and future \n"
              "'write' - modify/write events \n"
              "'exit' - ends  script \n"
              "'today' - gets all events today \n")
        event_getter()
        return
    if action_type == 'exit':
        return

    cda.display_event(cda.evaluate(action_type, current_time, current_date, cda.load(), current_week_day))

data = cda.load();
res = cda.write(data);
a = 1

event_getter()

