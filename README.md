# py2py3-demo-repo

Minimal repository that runs tests on **Python 3.12** and **Python 2.7** via GitHub Actions.

## Contents
- `.github/workflows/ci.yml` – CI workflow (Py3 on ubuntu-latest + Py2.7 in Docker)
- `mypkg/` – tiny cross-version package
- `tests/` – pytest tests
- `requirements/test_requirements.txt` – shared test dependency: `six`

## Local run (Py3)
```bash
python -m pip install -U pip pytest -r requirements/test_requirements.txt
pytest -q test/
```

## Local run (Py2.7 in Docker)
```bash
docker run --rm -it -v "$PWD":/repo -w /repo python:2.7-slim       bash -lc 'python -V &&                 python -m pip install -U "pip==20.3.4" "setuptools<45" "wheel<1.0" &&                 pip install "pytest<5" -r requirements/test_requirements.txt &&                 pytest -q test/'
```
