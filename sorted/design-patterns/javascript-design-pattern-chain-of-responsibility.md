# Javascript Design Patterns - Chain Of Responsibility

## Feature

- kind of behavioral pattern

## What Problem To Solve

- decouple the different steps involved in handling a request

## Structure

- [handler](#handler)
- [concrete handler](#concrete-handler)

## handler

- a abstract class or interface
- define a method for handling request, like `handleRequest()`
  - this method should check if it can handle the request
  - if it can, perform the processing, return the result
  - if it can't, pass the request to the next handler
- define a method for setting the next handler, like `setNext()`
  - this method should take a handler as parameter
  - this method should return the [handler]() itself
  - this method should be called before perform a request handling
- hold a field reference to the next handler

## concrete handler

- implement the methods in handler

## Code

```ts
// base handler
abstract class ExpenseHandler {
  protected nextHandler: ExpenseHandler;
  protected limit: number;

  setNextHandler(handler: ExpenseHandler): void {
    this.nextHandler = handler;
  }

  handleExpense(expense: number): void {
    if (expense <= this.limit) {
      console.log(`Expense of $${expense} approved by ${this.constructor.name}`);
    } else if (this.nextHandler) {
      console.log(`${this.constructor.name} cannot approve expense of $${expense}. Passing it on to ${this.nextHandler.constructor.name}.`);
      this.nextHandler.handleExpense(expense);
    } else {
      console.log(`No one can approve expense of $${expense}.`);
    }
  }
}

// concrete handler
class ManagerHandler extends ExpenseHandler {
  constructor() {
    super();
    this.limit = 1000;
  }
}

// concrete handler
class DirectorHandler extends ExpenseHandler {
  constructor() {
    super();
    this.limit = 5000;
  }
}

// concrete handler
class CEOHandler extends ExpenseHandler {
  constructor() {
    super();
    this.limit = 10000;
  }
}

// client
class ExpenseApprover {
  private managerHandler: ManagerHandler;

  constructor() {
    this.managerHandler = new ManagerHandler();
    const directorHandler = new DirectorHandler();
    const ceoHandler = new CEOHandler();
    this.managerHandler.setNextHandler(directorHandler);
    directorHandler.setNextHandler(ceoHandler);
  }

  approveExpense(expense: number): void {
    console.log(`Approving expense of $${expense}`);
    this.managerHandler.handleExpense(expense);
  }
}

const expenseApprover = new ExpenseApprover();

expenseApprover.approveExpense(500); // Expense of $500 approved by ManagerHandler
expenseApprover.approveExpense(1500); // Expense of $1500 approved by DirectorHandler
expenseApprover.approveExpense(7000); // Expense of $7000 approved by CEOHandler
expenseApprover.approveExpense(15000); // No one can approve expense of $15000.
```
