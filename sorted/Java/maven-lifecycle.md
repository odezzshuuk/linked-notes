# LifeCycle

## Introduction

- execute when build a project
- Lifecycle consists of different [build phases](#build-phase)
- A build phase represents a stage of the lifecycle

## Three Built-in Lifecycles

[Built-in](maven-built-in-lifecycle.md)

## What Is Build Phase

```bash
mvn verify
```

> `verify` is a build phase
> This command will run all phases in the default lifecycle in order until the verify phase

- phase are executed **sequentially**
- If a Build Phase doesn't bind [goals](#mojogoal), this build phase won't be executed
- build phase will execute all bound goals
- ~~build phase 是一个 core [plugin](maven-plugin.md)~~

## Phase List

default

- ...

clean

- pre-clean
- clean
- post-clean

Site

- pre-site
- site
- post-site
- site-deploy

## Bind Plugin In Project

```xml
<project>
  ...
  <build>
    <plugins>
      <plugin>
        <groupId>org.codehaus.modello</groupId>
        <artifactId>modello-maven-plugin</artifactId>
        <version>1.8.1</version>
        <executions>
          <execution>
            <configuration>
              <phase>process-test-resources</phase>
              <models>
                <model>src/main/mdo/maven.mdo</model>
              </models>
              <version>4.0.0</version>
            </configuration>
            <goals>
              <goal>java</goal>
            </goals>
          </execution>
        </executions>
      </plugin>
    </plugins>
  </build>
  ...
</project>
```

why is `<executions/>`

- you can run the same [goal](maven-terms.md#mojogoal) multiple times with different configurations

`<phase>process-test-resources</phase>`

- bind to a `process-test-resources` phase

## Combining Plugins and Build Phases

```shell
mvn clean dependency:copy-dependencies package
```

1. This command first executes to the `clean` phase
2. Then runs the plugin `dependency:copy-dependencies`
3. Finally runs the `package` phase
