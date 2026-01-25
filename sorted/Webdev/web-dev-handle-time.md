# Web Dev - Handle Time


## UTC Time

- is a time standard
- Coordinated Universal Time
- is successor to [Greenwich Mean Time (GMT)](#GMT time)

## GMT Time

## Timestamp


## Standard Time Text Format 

[Standard Time Text Format](web-dev-standard-time-text-format.md)

## Time Programming

Text To Time Object

```py
from datetime import datetime, timezone

tt = "1988-04-13T14:22:39.321+0808"
tf = "%Y-%m-%dT%H:%M:%S.%f%z"
to = datetime.strptime(tt, tf).time()
ut = datetime.strptime(tt, tf).replace(tzinfo=timezone.utc)

print("Time Object: ", to)
print("UTC time: ", ut)
```

Text To Timestamp

```py
```
