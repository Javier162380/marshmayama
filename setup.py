from setuptools import setup

meta = {}
exec(open('./marshmayama/version.py').read(), meta)

setup(
    name="Marshmayama",
    description="Fancy library to generate marshmallow.schemas(), dinamically from a yaml file",
    
)
