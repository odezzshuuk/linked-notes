# Web - API Design - GraphQL Style

## What It Is

- A query language based api
- Strongly typed schema
- Allow clients to request exactly the data they need

## Features

- Single endpoint
- Subscription For real time update
- Auto-generated documentation

## How To Define On Server

- Deinfe schema(type, query, mutation) and resolvers
- Frameworks: `Apollo Server`, `Graphene`, `graphql-java`

```ts
// install: npm install apollo-server graphql
import { ApolloServer, gql } from "apollo-server";

// Schema defines data types and queries
const typeDefs = gql`
  type User {
    id: ID!
    name: String!
    email: String!
  }

  type Query {
    getUser(id: ID!): User
  }
`;

// Resolver implements the query logic
const resolvers = {
  Query: {
    getUser: (_: unknown, { id }: { id: string }) => ({
      id,
      name: "Alice",
      email: "alice@example.com",
    }),
  },
};

const server = new ApolloServer({ typeDefs, resolvers });
server.listen({ port: 4000 }).then(({ url }) => console.log(`GraphQL API ready at ${url}`));
```

## How To Access On Client

- Send request to `/graphql` with query string such as `{ user(id: "1") { name, email } }`

```graphql
query {
  getUser(id: "1") {
    id
    name
    email
  }
}
```


## When To Use

- Complex data requirements
- flexible queries requirements
- Blockchain
- Decentralized System

## Design Principles

1. Predictable
2. Detail Error Message

