# WorkStation Backend

## Setup
- Create a new virtualenv
```
python3 -m venv ~/virtualenvs/workstation
```
- Activate the virtualenv
```
source ~/virtualenvs/workstation/bin/activate
```
- Install the requirements
```
pip install -r requirements.txt
```
- Create `workstation/.env` file for storing secret key locally.

Follow the same structure as `workstation/.env-example`.

**NEVER SAVE OR COMMIT ANY SECRET KEYS IN settings.py**

All secrets should live in your `workstatuon/.env` file.

- Migrate models
```
./manage.py migrate
```

## Updating `requirements.txt`

If you install a new package or dependency through `pip install`, make sure to
update the `requirements.txt` file with:
```
pip freeze > requirements.txt
```

## Linting

To make the format of our files consistent, we should use `black` to lint the
files.
```
black <path to file>
```
