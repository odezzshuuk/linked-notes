# tailwind responsive design

- [what is Responsive Design](#what-is-responsive-design)
- [how to design a responsive layout](#how-to-design-a-responsive-layout)
- [apply style on no-greater-than view port](#apply-style-on-no-greater-than-view-port)

## what is Responsive Design

- At different breakpoints conditionally apply utility tailwind class
- base on [@media](css-at-media.md)

default breakpoint: inspired by common device

- `sm`: `@media (min-width: 640px)`
- `md`: `@media (min-width: 768px)`
- `lg`: `@media (min-width: 1024px)`
- `xl`: `@media (min-width: 1280px)`
- `2xl`: `@media (min-width: 1536px)`

marked on tailwindcss use `:`

```html
<img class="w-16 md:w-32 lg:w-48" src="..." alt="..."/>
```

- `w-16`: default width
- `md:w-32`: apply `w-32` on device view port width **greater** than 768px
- `lg:w-48`: apply `w-48` on device view port width **greater** than 1024px


## how to design a responsive layout

> people most often style something for mobile

**mobile-first** working

- use default tailwind class for mobile device
- work from small to **large**

**don't think `sm` as meaning "on small screens"**

- think `sm` as at the small breakpoint**

## apply style on no-greater-than view port

use `md:max-*:` as prefix

- `max-sm`: `@media not all and (max-width: 640px)`
- `max-md`: `@media not all and (max-width: 768px)`
- `max-lg`: `@media not all and (max-width: 1024px)`

## custom theme

- config in `tailwind.config.js`

## use arbitrary value

```css
<div class="min-[320px]:text-center max-[600px]:bg-sky-300">

</div>
```