now - gets all events within an hour of now, and says what event you're on
today - gets all events today
ldall - gets all events expired and future
write - allows you to modify/write events

the program will have 2 types of events - weekly and singular
weekly repeat each week
singular happen once

each program run all expired singular events are to be removed from the database, or moved to a secondary database

functions:
get_events() depending if 'now' or 'today' displays different events

DB structure
event id
name
date - if event type is weekly, instead of date here is written weekday
time - time of event
notes - weekly notes get deleted after an occurrance
type - type of event - singular (gets deleted after occurrence) or weekly (gets repeated each weak)