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
1) write `CsvDb.write():success` function, that writes new or modifies existing events. <br/>
2) write `CsvDb.load():all_events`returns all events in DB
3) write `CsvDb.get_singular():singulars_list` function that returns singular events in a list. <br/>
4) write `CsvDb.get_weekly():weeklys_list` function that returns weekly events in a list.<br/>
5) write `evaluate(console_command, current_time):events_list` function that depending on console command will limit events to `now`, `today` or
   `ldall`. Returns list of evaluated weeklys and singulars.<br/>
6) write `display(events_list)` function that display evaluated events.