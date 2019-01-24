set -vx
python3 -m venv venv
venv/bin/python -m pip install --upgrade pip==19.0.1 setuptools==40.6.3
rm pyproject.toml
venv/bin/python -m pip install --ignore-installed .
touch pyproject.toml
venv/bin/python -m pip install --ignore-installed .
