import InputQualifier as iq
import datetime as dt
import json_actions as ja


def todo_manager():
    action_type = iq.input_compare_w_string("Type in action or ask help (help): ",
                                            '', ['now', 'ldall', 'exit', 'lddb', 'write', 'help'])

    current_date = dt.date.today()
    current_week_day = str(current_date.isoweekday())
    current_time = dt.datetime.now().time()
    ja.delete_outdated(current_date)

    # responding to exit lddb and help
    if action_type == 'help':
        print("'now' - load all tasks today \n"
              "'ldall' - load all remaining tasks, excluding repeatables \n"
              "'write' - create or modify task \n"
              "'exit' - ends script \n"
              "'lddb' - prints whole json database \n")
        todo_manager()
        return
    if action_type == 'exit':
        return

    ja.load_db(action_type)
    ja.ldall(action_type, current_date, current_week_day)
    ja.now(action_type, current_time, current_date, current_week_day)

todo_manager()

