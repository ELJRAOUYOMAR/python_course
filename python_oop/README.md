# Object-Oriented Programming in Python

This repository contains examples and explanations of Object-Oriented Programming (OOP) concepts in Python, ranging from basic class definitions to advanced topics.

## Table of Contents

1. [Introduction](#introduction)
2. [Defining a Class](#defining-a-class)
3. [Class Attributes and Methods](#class-attributes-and-methods)
4. [Inheritance](#inheritance)
5. [Polymorphism](#polymorphism)
6. [Encapsulation](#encapsulation)
7. [Advanced Topics](#advanced-topics)
    - [Abstract Classes](#abstract-classes)
    - [Method Overriding](#method-overriding)
    - [Class Methods and Static Methods](#class-methods-and-static-methods)
    - [Property Decorators](#property-decorators)
    - [Magic Methods](#magic-methods)
    - [Multiple Inheritance](#multiple-inheritance)
8. [Conclusion](#conclusion)

## Introduction

Object-Oriented Programming (OOP) is a programming paradigm that revolves around the concept of "objects," which can contain data (attributes) and code (methods). Python is a powerful and flexible language for implementing OOP principles.

## Defining a Class

In Python, a class is defined using the `class` keyword followed by the class name. Here's a simple example:

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Car: {self.make} {self.model}")
