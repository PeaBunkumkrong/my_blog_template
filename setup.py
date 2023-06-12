from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in my_blog_template/__init__.py
from my_blog_template import __version__ as version

setup(
	name="my_blog_template",
	version=version,
	description="test blog temp",
	author="nope",
	author_email="nope",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
