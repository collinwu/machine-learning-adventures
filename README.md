# machine-learning-adventures
Machine Learning Adventures

# Getting started

Make sure you have Python 3 and Pip

```bash
$ python --version
$ pip --version
```

Install Pipenv

```bash
$ pip install --user pipenv
```


Make sure the binary is available in your `PATH`

```bash
$ python -m site --user-base
```
For more details, visit [Hitchhiker's Guide to Python](https://docs.python-guide.org/dev/virtualenvs/#installing-pipenv)

### Installing dependencies

Example:

```bash
$ cd project_folder
$ pipenv install requests
```

To run a script - use `pipenv run`:

```bash
$ pipenv run python getting_started/main.py
```

## Notes

if leveraging `spaCy`, it might be helpful to use one of their models.

Example:

```bash
$ python -m spacy download en_core_web_lg
```
