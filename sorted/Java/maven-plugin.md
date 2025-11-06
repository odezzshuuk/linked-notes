# Plugin

- [Introduction](#introduction)
- [core plugin](#core-plugin)
- [Where Plugins Located](#where-plugins-located)
- [packaging plugin](#packaging-plugin)
- [Tools Plugin](#tools-plugin)
- [Custom A Plugin](#custom-a-plugin)

## Introduction

- plugin is a group of [goals](maven-terms.md#mojogoal)
- Maven is actually a core framework for a collection of maven plugins
- In other words, plugins execute most of the actual operations

Plugins are divided into two types

- build plugin
  - executed during the build lifecycle
  - configured in `<build/>` from [POM]
- reporting plugin
  - execute during site generation
  - configured in `<reporting/>` from [POM]

## Custom A Plugin

[](maven-custom-plugin.md)

## core plugin

- corresponding to default core phases

core plugin list:

- clean
- compiler
- deploy
- failsafe
- install
- resources
- site
- surefire
- verifier

[Core Plugin Detail](maven-core-plugin.md)

## Where Plugins Located

- locate in `~/m2/repository/org/apache/maven/plugins`

## packaging plugin

[Maven Source Plugin](maven-source-plugin.md)

## Tools Plugin

[Maven AntRun Plugin](maven-antrun-plugin.md)
