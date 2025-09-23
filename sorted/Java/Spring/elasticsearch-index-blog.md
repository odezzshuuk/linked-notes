# What is ElasticSearch Index

## What it is

- one index corresponds to one database in ElasticSearch

## RelationShip between Index and Data

MySQL VS elasticSearch

- MySQL $\rightarrow$ database $\rightarrow$ Tables $\rightarrow$ Rows $\rightarrow$ Columns
- elasticSearch $\rightarrow$ **index** $\rightarrow$ **type** $\rightarrow$ **document** $\rightarrow$ **field**

- cluster can contain several index
- index can contain several type(table)
- type can contain several document(column)
- document can contain several fields

for example, in truck order scenario, **truck_order** index can contain several types:

- start
- end
- truck

a document in type `start` will contain all the details of the order

search statement: http://localhost:9200/truck_order/start/order_1

## Using Index to Store Logs

One index corresponds to one log file, possible index names are:

- logs-2013-02-22
- logs-2013-02-21
- logs-2013-02-20

Query multiple indices at the same time

```
curl -XGET localhost:9200/logs-2013-02-22,logs-2013-02-21/Errors/_search?query="q:ErrorMessage"
```

- Search logs from these two days

