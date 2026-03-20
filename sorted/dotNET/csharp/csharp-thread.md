# CSharp - thread

## A Race Condition

```cs
class Program {
  static void Main() {
    int counter = 0;
    Thread[] threads = new Thread[10];

    for (int i = 0; i < 10; i++) {
      threads[i] = new Thread(() => {
        for (int j = 0; j < 100000; j++) {
          counter += 1; // NOT thread-safe
        }
      });

      threads[i].Start();
    }

    foreach (Thread t in threads) {
      t.Join();
    }

    Console.WriteLine($"Final counter value: {counter}");
  }
}
```
