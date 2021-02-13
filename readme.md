## Commands

`now` - gets all events within an hour of now, and says what event you're on <br/>
`today` - gets all events today <br/>
`ldall` - gets all events expired and future <br/>
`write` - allows you to modify/write events <br/>
---
the program will have 2 types of events - weekly and singular
weekly repeat each week
singular happen once

each program run all expired singular events are to be removed from the database, or moved to a secondary database

functions:
get_events() depending if 'now' or 'today' displays different events
---
## DB structure
`event id`<br/>
`name`<br/>
`date` - if event type is weekly, instead of date here is written weekday<br/>
`time` - time of event<br/>
`notes` - weekly notes get deleted after an occurrance<br/>
`type` - type of event - singular (gets deleted after occurrence) or weekly (gets repeated each weak)<br/>
