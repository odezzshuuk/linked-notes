# getStaticPaths

- [what's for](#whats-for)
- [take a look](#take-a-look)
- [return value](#return-value)
  - [paths](#paths)
    - [params: an object of match route pararmeters](#params-an-object-of-match-route-pararmeters)
  - [fallback](#fallback)
    - [when `fallback: ture`](#when-fallback-ture)
    - [fallback page](#fallback-page)

## what's for

- for page with [dynamic routes](nextjs-dynamic-route.md)
- generate pages with **dynamic routes** at **build time**
- generate static [pages](nextjs-terminology.md#pages) represent by [dynamic routes](nextjs-dynamic-route.md) at build time

## feature

- must be used with [`getStaticProps`](nextjs-datafetching-getstaticprops.md)
- cannot use with `getServerSideProps`
- cannot exort getStaticpaths from non-page file(e.g. components folder)

## when to use

## take a look

```js
export async function getStaticPaths() {
  return {
    paths: [
      { params: { id: 1 } },
      { params: { id: 2 } }
    ],
    fallback: true;
  }
}
```

- called from a page use [Dynamic routes](nextjs-dynamic-route.md)

## return value

### paths

`paths` is an array of objects

every element in `paths` array represent a path, the page represent by path will be **pre-rendered**

properties of `paths` element:

```js
paths: [
  {
    params: {
      id: '1',
      locale: 'en'
    }
  },
]
```

- params
- locale

#### params: an object of match route pararmeters

for path `pages/posts/[postId]/[commentId]`

- params should contain `postId` and `commentId`
- code follows specified path is `pages/posts/1/2` and `pages/posts/2/3`

```js
{
  paths: [
    params: { postId: '1', commentId: '2' },
    params: { postId: '2', commentId: '3' },
  ]
}
```

for path `pages/[...slug]`

- params should contain `slug`
- code follows specified path is `pages/foo/bar` and `pages/foo/baz`

```js
{
  paths: [
    params: { slug: ['foo', 'bar'] },
    params: { slug: ['foo', 'baz'] },
  ]
}
```

render root path `/`:

- slug is `null, undefined, false, or []`, root path will be rendered

```js
{
  paths: [
    params: {slug: null },
  ]
}
```

### fallback

`fallback: false`: 404 page will be rendered if the path is not in `paths`

`fallback: true`: function [getStaticProps()](nextjs-datafetching-getstaticprops.md) behavior changes in following ways:

1. The paths property returned by `getStaticPaths()` will be pre-rendered at build time by [getStaticProps()]
2. Paths not in `paths` will not result in a 404 page; Next.js will provide a [fallback page] for the first visit to such a path
3. Next.js will statically generate the requested page in the background, including running getStaticProps()
4. When completed, the browser will render a page based on [props]()

> For point 4, from the user's perspective, the page will switch from the **fallback page** to the fully rendered page

5. Pages navigated by `next/link` or `next/router` will not provide a fallback page; behavior is the same as `fallback: blocking`

`fallback: blocking`: function [getStaticProps()]() behavior changes in following ways

1. The paths property returned by `getStaticPaths()` will be pre-rendered at build time by [getStaticProps()]
2. 不在`paths`中的路径, 不会导致 404 page, Next.js会为首次访问的路径面开始SSR

> Next.js will not **provide a fallback page**

3. Users will only see a complete page, without a transition process

#### when `fallback: ture`

your app have a very large number of **static pages** that **depend on data**, and the builds would take a very long time

You can provide a small number of static pages, and use `fallback: true` for the rest

#### fallback page

- page [props](nextjs-datafetching-getstaticprops.md) will be empty
- [router.isFallback](nextjs-parse-routes.md#routerisfallback) can be used to detect whether to render a fallback page

```js
import { useRouter } from 'next/router'

function Post({ post }) {
  const router = useRouter();
  if (router.isFallback) {
    return <div>Loading...</div> // fallback page
  }
  return (
    <>
      <h1>hello, { post.name }</h1>
      <h1>age, { post.age}</h1>
    </>
  )
}

export async function getStaticPaths() {
  return {
    paths: [
      { params: { id: '1' } },
    ],
    fallback: true
  }
}

export async function getStaticProps({ params }) {
  const post = await new Promise((resolve) => {
    setTimeout(() => {
      resolve({
        name: 'second',
        age: 19
      })
    }, 2000)
  })

  return {
    props: { post },
    revalidate: 1,
  }
}

export default Post;
```
