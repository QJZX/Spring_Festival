import setuptools

import chunjie

setuptools.setup(
  name = "Spring_Festival",
  version = chunjie.__version__,
  description = chunjie.__doc__,
  author = "qjzx",
  url = "https://github.com/QJZX/Spring_Festival",
  packages = setuptools.find_packages( exclude=["venv"])
)

