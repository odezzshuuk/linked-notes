# Design Pattern - Dependency Injection Code Illustration

① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳

* [What Is The Problem](#what-is-the-problem)
* [Solve The Problem with Dependency Injection](#solve-the-problem-with-dependency-injection)

## What Is The Problem

Concrete Service

```ts
class EmailService {
  private msg
  private receiver

  sendEmail(msg: string, receiver: string) {
    console.log('Email sent to ' + receiver + ' with message: ' + msg)
  }
}
```

Service Consumer

```ts
//
class MyClient {
    private emailService: EmailService;

    // ①
    public MyClient(emailService: EmailService) {
        this.emailService = emailService;
    }

    public void processMessages(msg: string, recevier: string) {
        this.emailService.sendEmail(msg, recevier);
    }
}
```

Application Code

```ts
let myClientA = new MyClient()
myClient.processMessages('Hi John', 'name@example.com')
```

Look at above code, There are some **BAD PRACTICE**

- the client is responsible for creating the service and setting it
- what if we want to use another service
  - for example a service that send different format of message 

## Solve The Problem with Dependency Injection

[abstract service]

```ts
interface MessageService {
  sendMessage(msg: string, receiver: string): void
}
```

### concrete service

- EmailService

```ts
class EmailService implements MessageService {
  sendEmail(msg: string, receiver: string) {
    console.log('Email sent to ' + receiver + ' with message: ' + msg)
  }
}
```

- SMSService

```ts
class SMSService implements MessageService {
  sendSMS(msg: string, receiver: string) {
    console.log('SMS sent to ' + receiver + ' with message: ' + msg)
  }
}
```

### Consumer Interface

```ts
interface Consumer {
  processMessages(msg: string, receiver: string): void
}
```

[Concrete Consumer]

```ts
class MyDIApplication implements Consumer {
  private service: MessageService

  constructor(service: MessageService) {
    this.service = service
  }

  processMessages(msg: string, receiver: string) {
    this.service.sendMessage(msg, receiver)
  }
}
```

### Injector Class

```ts
class MessageServiceInjector {
  private service: MessageService

  constructor(service: MessageService) {
    this.service = service
  }

  getConsumer(): Consumer {
    return new MyDIApplication(this.service)
  }
}

class EmailServiceInjector extends MessageServiceInjector {
  getConsumer() {
    return new MyDIApplication(new EmailService())
  }
}

class SMSServiceInjector extends MessageServiceInjector {
  getConsumer() {
    return new MyDIApplication(new SMSService())
  }
}
```

### Client Code

```ts
let injector = new EmailServiceInjector()
let consumer = injector.getConsumer()
consumer.processMessages('Hi John', 'name@example.com')
```


