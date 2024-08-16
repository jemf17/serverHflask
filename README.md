# Administrative Server API

server where all queries are made, works, requests, profiles, etc. are added, deleted and modified...

## Installation

* Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

#### Linux:
```bash
python -m ensurepip --upgrade
```
#### Windows:
```bash
C:> py -m ensurepip --upgrade
```

* install virtualenv

```bash
python -m pip install --user virtualenv
```

* Create a virtual environment

```
virtualenv env_name
```

## activate env

#### Linux:
```
source env_name/bin/activate
```

#### Windows:
```
.\env_name\Scripts\activate
```

## deactivate

```
deactivate
```

* Install requerimientos.txt
> within the already activated virtual environment
```
pip install requerimientos.txt
```

## What to do when I install another library with pip?

In that case you have to transfer the new installed libraries to requirements.txt with pip freeze

```
pip freeze > requerimientos.txt
```

## Architecture

It is divided into 
* routes 
* models 
* DB 
> for the moment in a DB in SQLite

 Within Models there are entities where classes are defined with one or two methods in which the object data is transformed into a JSON format. Models covers all functions that require passing database queries to objects by calling its to_JSON or to_JSON_view function. All routes are defined in routes and each one is divided according to what the server requests. For example: Obra.py contain the routes that require modifying, consulting, updating or deleting works from the system. in BD it only gives rise to the connection to the database and error handling