## Commands 

`now` - gets all events within an hour of now, and says what event you're on <br/>
`today` - gets all events today <br/>
`ldall` - gets all events expired and future <br/>
`write` - allows you to modify/write events <br/>

***

the program will have 2 types of events - weekly and singular
weekly repeat each week
singular happen once

each program run all expired singular events are to be removed from the database, or moved to a secondary database

functions:
get_events() depending if 'now' or 'today' displays different events

***

## DB structure
`id`<br/>
`name`<br/>
`date` - if event type is weekly, instead of date here is written weekday<br/>
`time` - time of event<br/>
`notes` - weekly notes get deleted after an occurrance<br/>
`type` - type of event - singular (gets deleted after occurrence) or weekly (gets repeated each weak)<br/>

***

##Todo
1)A write `CsvDb.write():success` function, that writes new or modifies existing events. <br/>
2)D write `CsvDb.load():all_events`returns all events in DB
3)D write `CsvDb.get_event_type(event_type, all_events):selected_event_list` function that returns events of a wanted type 
in a list. <br/>
4)D write `evaluate(console_command, current_time, all_events):events_list` function that depending on console command will limit events to `now`, `today` or
   `ldall`. Returns list of evaluated weeklys and singulars.<br/>
5)D write `display(events_list)` function that display evaluated events.
6)A write `CsvDb.remove_expired(current_time)` removes 