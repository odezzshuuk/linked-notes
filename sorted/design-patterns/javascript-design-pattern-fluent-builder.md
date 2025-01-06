# JavaScript Design Pattern - Fluent Builder

## Code

```ts
class CarBuilder {
    private: Car

    constructor() {
        this.car = new Car();
    }

    setColor(color: string): CarBuilder {
        this.car.color = color;
        return this
    }

    setWheels(wheels: number): CarBuilder {
        this.car.wheels = wheels;
        return this
    }

    build(): Car {
        return this.car
    }
}

class Car {
    color: string
    wheels: number
}

const carBuilder = new CarBuilder();
const car = carBuilder.setColor("red").setWheels(4).build()
```
