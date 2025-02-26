# Sphinx_Test

apt-get install -y python3-sphinx
mkdir docs/
sphinx-quickstart --ext-autodoc --ext-todo --ext-coverag
uncomment conf.py lines
sphinx-apidoc -o . ..
make html


---
pyment -w main.py

sphinx-quickstart

https://eikonomega.medium.com/getting-started-with-sphinx-autodoc-part-1-2cebbbca5365
https://youtu.be/b4iFyrLQQh4?si=p0sYW1x_8ES567oN

reStructuredText

Tópicos:
- [X] sphinx.ext.autodoc;
- [ ] sphinx.ext.todo;
- [ ] sphinx.ext.autosummary;
- [ ] sphinx.ext.coverage;