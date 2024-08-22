# MongoDB - Glossary

- [document](#document)
- [collection](#collection)
- [Databases](#databases)
- [Field](#field)
- [mongod](#mongod)
- [namespace](#namespace)
- [server](#server)
- [cluster](#cluster)

## document

- Composed of field and value

```json
{
  "_id": {
    "$oid": "63f58348dd7588f0f61691f6"
  }
  "name": "sue",
  "age": 26,
  "status": "A",
  "groups": [ "news", "sports" ]
}
```

- each document **stored in a collection** *requires* a unique `_id` field as [primary key](#primary-key)

## collection

- store [documents](#document)

## Databases

- hold one or more collection

## Field

- key in a document

## mongod

- primary **daemon process** for the MongoDB

## mongos

## namespace

- canonical name for a collection
- like `[database-name].[collection-or-index-name]`

## server

## cluster

## primary key

- hold by `_id` field
- usually a BSON [ObjectId](mongodb-bson.md#objectid)

```json
{
  "_id": {
    "$oid": "63f58348dd7588f0f61691f6"
  }
}
```

## replica set

- A cluster of MongoDB servers that implements replication and automated failover(自动故障转移)
- a group of mongod processes that maintain the same data set

## replication

- a feature allowing multiple database servers to shared the same data
- ensuring redundancy(冗余) and facilitating load balancing(促进负载均衡)

## shard

- single mongod instance
- or a [replica set](#replica-set) that stores **portion** of a shared cluster's total data

## shard key

- field MongoDB used to distribute documents among members of a [shared cluster](#shard-cluster)

## shard cluster

- shard cluster consists of
  - config servers
  - [shards](#shard)
  - one or more mongos routing processes


