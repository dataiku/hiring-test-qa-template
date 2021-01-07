# hiring-test-qa-template-python

This project is an _incomplete_ template that can be used by a junior developer to implement the technical test for the hiring process for a QA job at Dataiku.

The following tests have been implemented using python + pytest.

## setup

### install the prerequisites

These tests require Python 3 (https://www.python.org/downloads/).

### configure your python environment

```sh
git clone https://github.com/dataiku/hiring-test-qa-template.git
cd hiring-test-qa-template/python
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### run the tests

```sh
pytest -v tests --base-url INSTANCE_URL
````
