# Parse Markdown with Nodejs

to parse a file path is `/posts/first-post.md`

```
---
title: hello markdown
slug: home
---

# First Post

```

```js
import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';

const filePath = path.join(process.cwd(), 'posts', 'first-post.md');
const fileContent = fs.readFileSync(filePath, 'utf-8');
const result = matter(fileContent);
console.log(result)
```

output

```
{
  content: '\r\n# First Post\r\n',
  data: { title: 'hello', slug: 'home' },
  isEmpty: false,
  excerpt: ''
}
```

## convert markdown to html

## parse markdown ast

```js
import unified from 'unified';
import remarkPares from 'remark-parse';

const text = `# Hello, *World*!`;

const root = unified()
  .use(remarkPares);
  .parse(markdown);

console.log(root)
```

## walk ast

```js
import { visiParents } from 'unist-util-visit-parents';

const root = unified()
  .use(remarkPares);
  .parse(markdown);

visiParents(root, 'link', (node, parents) => {
  node.url = node.url.replace('.md', '')
}
```

- this code will remove `.md` suffix from all links in markdown file
