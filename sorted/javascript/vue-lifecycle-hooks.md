# Vue - Lifecycle Hooks


* [onMounted()](#onmounted())
* [onUpdated()](#onupdated())
* [onUnmounted()](#onunmounted())
* [onBeforeMount()](#onbeforemount())
* [Other Hooks](#other-hooks)
* [What's Mounted](#what's-mounted)

[Lifecycle Demonstration](https://vuejs.org/guide/essentials/lifecycle.html)

## onMounted()

When is called

- After the component is [mounted](#what's-mounted) to the DOM

Used For:

- Effect that need to acess the rendered DOM
- Limit client related code in [server-rendered]() application

## onUpdated()

When is called

- When DOM is updated due to [reactive state change](vue-reactivity.md)

Features

- Not called on [server-side rendering](nextjs-rendering.md#server-side-rendering)
- parent's is called after child's
- Multiple state changes can trigger one call

Used For:

- 

## onUnmounted()

Usage:

- Cleanup side effects (e.g., remove event listeners, server connections, etc.)

## onBeforeMount()

When is called:

- Before the component is mounted to the DOM

Usage:

- Fetching data before rendering

## Other Hooks

- onBeforeUpdate()
- onBeforeUnmount()
- onErrorCaptured()
- onRenderTracked()
- ...

## What's Mounted

- All of its **synchronous** child components are mounted
