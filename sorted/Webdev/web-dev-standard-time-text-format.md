# Standard Time Text Format

## Time Text

`[Date]T[time][timezone]`

> T allows to be omitted when there is no risk of confusion

Date

| format     | example    |
| ---------- | ---------- |
| YYYY-MM-DD | 2021-10-01 |
| YYYY-MM    | 2021-10    |

- YYYY: 0000-9999
- MM: 01-12
- DD: 01-31

Time

| format       | example       |
| ------------ | ------------- |
| hh:mm:ss.sss | T13:47:30.123 |
| hh:mm:ss     | T13:47:30     |
| hh:mm        | T13:47        |
| hh           | T13           |
| hhmmss.sss   | 134730.123    |
| hhmmss       | 134730        |
| hhmm         | 1347          |

- hh: 00-23
- mm: 00-59
- ss: 00-59
- sss: 000-999 

Timezone

| format | description                                    |
| ------ | ---------------------------------------------- |
| Z      | zero UTC offset                                |
| ±hh:mm | + describe east of UTC, - describe west of UTC |
| ±hh    | + describe east of UTC, - describe west of UTC |
