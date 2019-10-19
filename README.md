#  Marshmayama

### Introduction

Maybe one day you want to define Marshmallow Schemas dinamically, so you can easily decouple the configuration from your code. This library tryes to help you generating Marshmallow Schemas from a yaml file.

### Usage

This library pretends to be a really easy interface. Just create an instance of Marshmayama passing your yaml file and generate your Marshmallow Schema.

```python
MarshmayamaInstance = Marshmayama('path-to-your-yaml-file.yml')

marshmallow_schema = MarshmayamaInstance.generate_marshmallow_schema()

```
