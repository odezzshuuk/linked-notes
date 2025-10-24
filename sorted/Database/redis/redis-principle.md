# Principle

- [Principle](#principle)
  - [Cache Eviction Policy](#cache-eviction-policy)
  - [Redis Cache Breakdown](#redis-cache-breakdown)
  - [Redis Cache Penetration](#redis-cache-penetration)
  - [Redis Cache Avalanche](#redis-cache-avalanche)
  - [Redis Persistence](#redis-persistence)
  - [Redis Storage Principle](#redis-storage-principle)
  - [Redis Cluster](#redis-cluster)


## Cache Eviction Policy

- When memory is insufficient, new write operations will report an error: noeviction
- Data deletion strategies:
  - allkeys-random: randomly delete
  - volatile-random: randomly delete expired data
  - volatile-ttl: most recently expired data
  - allkeys-lru: least recently used data
  - volatile-lru: data with time limit, longest since last use
  - allkeys-lfu: all data, least frequently used
  - volatile-lfu: data with time limit, least frequently used

## Redis Cache Breakdown

- **Redis cache breakdown**: When the requested key does not exist in Redis, it will be looked up in the database
- Usually needs to be synchronized from the database to Redis

## Redis Cache Penetration

- When a requested key is not in Redis, it will be queried in the database
- Can be exploited by malicious requests: a large number of queries for non-existent keys, causing excessive database pressure
  - Use Bloom filter to solve

## Redis Cache Avalanche

- Refers to the situation where a large amount of data in Redis expires at the same time in a short period

## Redis Persistence

- Since Redis is an in-memory database, data will be lost when the Redis service restarts
- Strategies:
  - RDB: Save a snapshot of the data in memory to disk, backup to dump.rdb file
    - Advantage: fast recovery
    - Disadvantage: some data may be lost
  - AOF: Record each write operation to disk
    - Advantage: no data loss
    - Disadvantage: takes up a lot of space

## Redis Storage Principle

- hash table

## Redis Cluster

**Master-Slave Replication**

- Master-slave replication is a common data backup method
- The master is responsible for read and write operations, the slave is responsible for backing up the master's data
- If the master fails, the slave will be promoted to master

**Read-Write Separation**

- The master performs **read and write** operations
- The slave performs **read** operations
- [ ] TODO

**Sentinel Mode**

- Detects the running status of master and slave to complete master-slave switch
- [ ] TODO

**Sentinel Cluster**

- Multiple sentinels monitor master and slave, preventing misjudgment
- [ ] TODO

**Sharded Cluster**

- Redis has 0-16383 slots, each slot stores a key-value pair
- Deploy multiple Redis instances, each instance is responsible for a portion of the slots, these Redis instances are called **nodes**
- Each node is responsible for a portion of the slots, for example:
  - Node 1: 0-5460
  - Node 2: 5461-10922
  - Node 3: 10923-16383
- A key is located on a specific server using the CRC algorithm
- [ ] TODO


**哨兵模式**

- 检测主备机运行状态完成主备机切换
- [ ] TODO

**哨兵集群**

- 多个哨兵监控主备机, 防止误判
- [ ] TODO

**分片集群**

- Redis有0-16383个槽位, 每个槽位存储一个键值对
- 部署多个Redis实例, 每个实例负责一部分槽位, 这些Redis实例称为**节点**
- 每个节点负责一部分槽位如: 
  - 节点1: 0-5460
  - 节点2: 5461-10922
  - 节点3: 10923-16383
- 一个key通过CRC算法在指定服务器上查找数据
- [ ] TODO
