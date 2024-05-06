# Unity - Animation Controller

## What It IS

- Act as state machine
- Including multiple animation clips

## Animation States

- [Animtion states]() are the basic building blocks of an Animator Controller
- Animation State maybe
  - Single animation clip
  - [Blend tree](#Blend-Tree)

Properties

- Motion: Animation clip or blend tree
- Speed: Speed of Motion

## Blend Tree

What is this

- One state with multiple animation clips

What's for

- A common task is to blend between multiple animation clips
- For example, blend between walking and running

Features

- The motions must be of similar "nature" and timing
- For Example, walking and running can be aligned so that the moments of contact of foot to the floor take place at the same points in normalized time
- Take one **[numeric animator parameter](#animator-parameter)** as input, numeric parameter is used to blend between the motions

## Animator parameter


