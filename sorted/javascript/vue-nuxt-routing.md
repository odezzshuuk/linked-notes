# Nuxt - Routing

Directory structure 1

```
.
├── app.vue
└── pages
    ├── [slug].vue
    ├── index.vue
    └── abc.vue
```

- Url path `/` mapped to `app/pages/index.vue`
- While Url path `/index`  not map to `app/pages/index.vue`
  - But mapped to `app/pages/[slug].vue` with `slug` parameter value `index`

Directory structure 2

```
.
├── app.vue
└── pages
    ├── [slug].vue
    ├── index.vue
    ├── abc.vue
    └── users
        ├── abc.vue
        └── index.vue
```


- Url path `/abc` mapped to `app/pages/abc.vue`
- Url path `/def` mapped to `app/pages/[slug].vue` with `slug` parameter value `def`
- Url path `/users/abc` mapped to `app/pages/users/abc.vue`

Directory structure 3

```
.
├── app.vue
└── pages
    ├── [...slug].vue
    ├── index.vue
    └── users
        ├── abc.vue
        └── index.vue
```

- Url path `/users/abc` mapped to `app/pages/users/abc.vue`
- Url path `/users/def` mapped to `app/pages/[...slug].vue` with `slug` parameter value `['users', 'def']`
  - Not `app/pages/users/[slug].vue` because it doesn't exist

Directory structure 4

```
.
├── app.vue
└── pages
    ├── [...slug].vue
    ├── index.vue
    └── users
        ├── [...slug].vue
        └── index.vue
```

- Url path `/users/abc` mapped to `app/pages/users/[...slug].vue` with `slug` parameter value `['abc']`

