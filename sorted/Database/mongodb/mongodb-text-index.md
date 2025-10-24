# Text Index

## Introdution

- for **text search**, must have a text index on your collection
- to perform text search, you must create a **text index** on collection
- text index can include fields that
  - value is string
  - or an array of string
- A Collection Can Have **At Most One** TextIndex

## Feature

case insensitive

- text does not distinguish between **é, É, e, and E.**

Tokenization Delimiters (tokenization delimiter)

> used to create search keywords

- Dash(-)
- Pattern_Syntax (regular expression)
- White_Space (whitespace character)
- Punctuation (punctuation mark)
- Quotation_Mark (quotation mark)

search language

- language value specify of "none", mongodb will simplify the search process


## create text index

if you want search `title` field text, create text index on `title` field

```js
db.movies.createIndex({ title: "text"})
```

- `"text"` represents the type of index

index multiple fields for text index

```js
db.reviews.createIndex(
  {
    subject: "text",
    comments: "text"
  }
)
```

## Config Field Weight

```js
db.blog.createIndex(
  {
    content: "text",
    keywords: "text",
    about: "text"
  },
  {
    weights: {
      content: 10,
      keywords: 5
    }
    name: "TextIndex"
  }
)
```

- `content` field weight of 10
- `keywords` has a weight of 5
- `about` field has a default weight of 1

## wildcard text index

```js
db.collection.createIndex({ "$**": "text" })
```

- allows for text search on all fields in a document


## Drop a Text Index

first get the index name

```js
db.collection.getIndexes()
```

output like this

```json
[
  {
    "v" : 2,
    "key" : {
       "_id" : 1
    },
    "name" : "_id_"
  },
  {
    "v" : 2,
    "key" : {
       "cat" : -1
    },
    "name" : "catIdx"
  },
  {
    "v" : 2,
    "key" : {
       "cat" : 1,
       "dog" : -1
    },
    "name" : "cat_1_dog_-1"
  }
]
```

drop index by index name

```js
db.collectoin.dropIndex("catIdx");
```

## Performance

- fit RAM will make phrase query more effectively
- impact on insertion performance

## Requirements

- make sure the **high limit** on open [file descriptors](linux-file-descriptor.md), when building a largve text index on collection

## Restriction

- text query in an $or expression, all clauses must use the same text index 
