from setuptools import setup

meta = {}
exec(open('./marshmayama/version.py').read(), meta)
libraries = open('requiremets.txt').read().split()

setup(
    name="Marshmayama",
    description="Fancy library to generate marshmallow.schemas(), dinamically from a yaml file",
    version=meta['__version__'],
    author="@Javier162380",
    packages="marshmayama",
    install_requires=libraries,
    url="https://github.com/javier162380/marshmayama",
    python_requires='>=3.6'
)
