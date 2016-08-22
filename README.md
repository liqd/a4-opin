# CMS for EUTH Project

## Requires

 * nodejs (+ npm)
 * python 3.x (+ virtualenv + pip)
 * libmagic


## Setup and development

Use the provided Makefile to start development. It comes with a help command
`make help` . The initials steps to get the software running should be:

```
git clone https://github.com/liqd/euth_wagtail.git  # clone repository
cd euth_wagtail
make install
make fixtures
make watch
```
