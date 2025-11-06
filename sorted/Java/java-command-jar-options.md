# Java - Jar Options

## main operating mode

> Parameters that must be specified when using jar, usually the first parameter
> whene use jar must specify this option, usually the first option


`-c` or `--create`

- create a new archive

`-i=FILE` or `--generate-index=FILE`

- Generate index information for the specified JAR file.

`-t` or `--list`

- List archive directory

`-u` or `--update`

- Update existing JAR file

`-x` or `--extract`

- Extract specified files from archive

`-d` or `--describe-module`

- Print document descriptor or automatic module name

## Operation modification parameters that can be used in any situation

`-C DIR files`

- Change to specified directory and add files to archive.

`-f=FILE` or `--file=FILE`

- Specify archive file name

`--release VERSION`

- Create a multi-version JAR file. Place all files specified after the option in the version directory of the JAR file
- The file name is `META-INF/versions/VERSION/`
  - Where VERSION must be a positive integer greater than or equal to 9
- At runtime, when multiple versions of a class exist in the JAR, the JDK will use the first version it finds
  - Search order
      1. First, search for version numbers in the directory tree that match the JDK major version number
      2. Then, search directories with lower version numbers in order,
      3. Finally, search the root directory of the JAR.

`-v` or `--verbose`

- Send or print verbose output to standard output.


## Operation modification parameters that can be used when creating and updating

`-e=CLASSNAME` or  `--main-class=CLASSNAME`

- Specify the application entry point for standalone applications bundled into <font color="red">modular</font> or <font color="red">executable modular</font> JAR files

`-m=FILE` or `--mainfest=FILE`

- Include manifest information from manifest file
- FILE: manifest file

`-M` or ``--no-manifest`

- Do not create manifest information for jar file

`--module-version=VERSION`

- Specify version when creating or updating

`--hash-modules=PATTERN`

`-p` or `--module-path`

Specify hash generation

`@file`

- Load arguments from text file