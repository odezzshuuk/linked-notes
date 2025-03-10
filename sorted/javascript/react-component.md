# React - Components

* [They Are Components](#they-are-components)
* [This Is Not A Component](#this-is-not-a-component)
* [Curly Braces](#curly-braces)
* [Props](#props)
* [State](#state)
* [Use A Component](#use-a-component)
* [Component Compose of other Component](#component-compose-of-other-component)
* [render](#render)
* [inline style](#inline-style)
* [keep component pure](#keep-component-pure)
* [class properties](#class-properties)
* [lifecycle](#lifecycle)
* [handling events](#handling-events)
* [React Server Component(RSC)](#react-server-component(rsc))

## They Are Components

- component is a [javascript function](javascript-function.md)

> you use `class` create a component, but class essentially is a function

**function component**

- `props` are read-only, function body must not change `props`

```jsx
function Welecom(props) {
    return <h1>Hello, {props.name}</h1>;
}
```

[**class component**](react-class-component.md)

```jsx
class Welcom extends React.Component {
    render() {
        return <h1>Hello, {this.props.name}</h1>;
    }
}
```

## This Is Not A Component

`<h1> hello </h1>` is **Jsx literal**

```jsx
const element = <h1>Hello, world!</h1>;
export default element; // this is not a component
```

## Curly Braces

> window to javascript expression

```js
function TodoList(user) {

    const name = 'Gergorio Y. Zara';
    return (
        <h1>{name}'s To Do List</h1>
    )
}
```

double curlies for **object** attribute value

```jsx
function TodoList() {
  return (
    <div>
      <h1
        styles={{
          color: 'red',
          fontSize: '20px'
        }}
      >
        To Do List
      </h1>
    </div>
  )
}
```

## Props

[Props](react-component-props.md)

- as component attribute
- use nest Children Component or HTML tag inside a **JSX tag**

## State

[State](react-component-state.md)

- a data can be changed

## Use A Component

- lowercase tag name: html tag, `<section>, <div>`
- to separate with html tag, react component demand start with capital, like `<Welcome />`

```js
function Welcome(props) {
    return <h1> Hello, {props.name}</h1>;
}
export default function threeWelcome() {
    return (
        <div>
            <Welcome name="Sara" />
            <Welcome name="Cahal" />
            <Welcome name="Edite" />
        </div>
    );
}
```

## Component Compose of other Component

component-a.jsx

```jsx
const componentA = () => {
    return <h1>Hello, world!</h1>;
};
```

component-b.jsx

```jsx
import A from "./component-a.jsx";

function B() {
  return (
    <div>
      <A />
    </div>
  );
}
```

## render

- re-render on state change

## inline style

> css property value is string

```jsx
const element = (
    <div
        styles={{
            color: 'red',
            fontSize: '20px'
        }}
    >
        To Do List
    </div>
);
```

## keep component pure

*pure* function

```js
function sum(a, b) {
  return a + b;
}
```

*impure* function

- change its input

```js
function withdraw(account, amount) {
  account.total -= amount;
}
```

## class properties

- defaultProps
- displayName

## lifecycle

[Lifecycle](react-component-lifecycle.md)

## handling events

```jsx
function Button({ handleClick }) {
    return <button onClick={handleClick}>Click me</button>;
}
export default function Toolbar() {
    return (
        <div>
            <Button handleClick={() => alert("clicked")} />
        </div>
    );
}
```

event propagation

event propagation direction from a children, up to the tree

```js
const element = (
    <div className="Toolbar" onClick={() => alert("from children")}>
        <Button onClick={() => alert("click button")}>click me</Button>
    </div>
);
```

prevent event propagation, use `e.stopPropagation()`

```js
<Button
    onClick={(e) => {
        e.stopPropagation();
        onClick();
    }}
>
    click me
</Button>
```

prevent default event, use `e.preventDefault()`

-   use form as example, default behavior send request to server and refresh page
-   `e.preventDefault()` to pervent refresh page

```js
return (
  <form
      onClick={(e) => {
          e.preventDefault();
          onClick();
      }}
  >
      <input />
      <button>send</button>
  </form>
)
```

## React Server Component(RSC)

## React Error Boundaries

[React Error Boundary](react-error-boundary.md)



