set -vx
python3 -m venv venv
venv/bin/python -m pip install --upgrade pip==19.0.3 setuptools==40.8.0
rm pyproject.toml
venv/bin/python -m pip install --ignore-installed .
touch pyproject.toml
venv/bin/python -m pip install --ignore-installed .
