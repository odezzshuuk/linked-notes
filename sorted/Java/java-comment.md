# Comments

- Comments are placed before the structure they describe
- Extracted comments are placed between `/**...*/`

Information is mainly extracted from comments in the following structures

- Packages
- Public classes and interfaces
- Public and protected constructors and methods
- Public and protected fields

## Class Comments

## Comment Extraction

Single package

```shell
javadoc -d docDirectory package_name
```

Multiple packages

```shell
javadoc -d docDirectory package_name1 package_name2
```

> docDirectory is the directory where extracted documentation is saved