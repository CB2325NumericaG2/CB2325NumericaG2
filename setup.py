from setuptools import setup, find_packages

VERSION =   "0.0.1"
DESCRIPTION = "Biblioteca numérica Python"

setup(
  name = "<nossa-pasta-nome>",
  version = VERSION,
  author = "Grupo 2 do IMPA Tech",
  description = DESCRIPTION,
  author_email="<email-do-autor>",
  packages = find_packages(),
  install_requires=["numpy", "sympy", "matplotlib", "plotly"],
  keywords=["python", "IMPA Tech"],
  classifiers=[
    "Operating System :: Microsoft :: Windows",
    "Programming Language :: Python :: 3"
  ],
)