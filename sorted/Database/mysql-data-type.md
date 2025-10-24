# Data Type

## Number

integer

- TINYINT: 1 byte, -128~127
- SMALLINT: 2 byte, -32768~32767
- MEDIUMINT: 3 byte, -8388608~8388607 
- INT: 4 bytes
- BIGINT(m): equilavant Java primitive type [long](java-primitray-type.md)
  - m: length of    
  - zerofill: whether fill with 0
- FLOAT
- DOUBLE(m, d): 
  - m: total length
  - d: decimal length
- DECIMAL

## String Type

- CHAR(m)
  - Fixed length, m is the length
- VARCHAR(m)
  - Variable length, m parameter indicates the maximum available length
  - m can be 0 ~ 65535
  - Bytes used: 
    - 1 + m: m <= 255
    - 2 + m: 256 <= m <= 65535
  - Can be part of an [index]
  - Saves space
- BLOB
- TEXT
  - fixed length is 65535 characters
  - can not be part of [index](mysql-index.md)
- MEDIUMBLOB
- MEDIUMTEXT
- LONGBLOB
- LONGTEXT
- TINYBLOB
- TINYTEXT

## NULL value

- means no data
- compare operations on null value will get null value
- use `is null` or `is not null` to test null value

> `null + 1 is null`

```sql
select 0 is null, 0 is not null;
select 1 = null, 1 <> null, 1 < null, 1 > null
```

```shell
+-----------+---------------+
| 0 is null | 0 is not null |
+-----------+---------------+
|         0 |             1 |
+-----------+---------------+
```

## Date and Time

- DATE: year, month, date, format: yyyy-mm-dd
- TIME: hour, minute, second, format: hh:mm:ss
- YEAR: 
- DATETIME: data + time
- TIMESTAMP: milliseconds from 1970-01-01 00:00:00
  - default value: `CURRENT_TIMESTAMP()`, 
  - default auto update: indicate that the column will be updated to the current timestamp when any other column of the row is changed. [Extra value] is `on update current_timestamp()`

Open auto upate for `timestamp` 

```sql
alter table tbl_name change 
  timestamp_col timestamp_col timestamp 
  default 
    current_timestamp 
    on update current_timestamp;
```

close auto update for `timestamp`

```sql
alter table tbl_name change
  timestamp_col timestamp_col timestamp
  default 
    current_timestamp;
```

## enum

- insert value must be one of the enum values

```sql
create table tbl_name(
  col_name enum('val1', 'val2', 'val3')
);
insert into tbl_name(col_name) values('val1');
```

## set - column value type is type, its value can be a subset of the set

```sql
create table tbl_name(
  set_col set('a', 'b', 'c')
);
insert into tbl_name values('a, b');
```

## json

- insert json format text

```sql
create table tbl_name(
  json_col json
);
insert into tbl_name values('{"a": 1}');
```

## Example

### INT

```sql
create database db;
use db;
create table tbl(num int(5) zerofill)
insert into tbl values(81);
select * from tbl;
```

output

```shell
+-------+
| age   |
+-------+
| 00090 |
+-------+
```

### DOUBLE

```sql
create table tbl(num double(5, 3));
insert into tbl values(23.234);
insert into tbl values(23.234567);
insert into tbl values(234.34);  // out of bound
select * from tbl2;
```
output

```shell
+--------+
| num    |
+--------+
| 23.234 |
| 23.234 |
+--------+
```

## MySQL Type Map to Java Type

| MySQL Type             | Java Type     |
| ---------------------- | ------------- |
| tinyint, smallint, int | Integer       |
| bigint                 | long          |
| char/varchar/text      | String        |
| datetime               | LocalDateTime |
| decimal                | BigDecimal    |

## MySQL Type Map to Typescript Type

## MySQL Type Map to Python Type

