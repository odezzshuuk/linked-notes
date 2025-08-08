# Tailwindcss

- [Install](#install)
- [`@apply`](#apply)
- [arbitray values](#arbitray-values)
- [Responsive Design](#responsive-design)

## Install

Installation method when not using in a Node.js environment

```shell
npm install -D tailwindcss
npx tailwindcss init
```

By installing as a postcss plugin, integrated with build tools such as webpack, Rollup, Vite, Parcel

```shell
npm install -D tailwindcss postcss autoprefixer
```

## `@apply`

Extracting classing with `@apply`

index.html

```html
<div>
  <button>Primary</button>
</div>
```

style.css

- use `@apply` to use tailwind classes on css selectors

```css
button {
  @apply bg-blue-500 text-white font-bold py-2 px-4 rounded;
}
```

## arbitray values

if you want to use arbitray values

```html
<div class="top-[117px]">
  <!-- ... -->
</div>
```

## Responsive Design

[Responsive Design](css-tailwind-responsive-design.md)
