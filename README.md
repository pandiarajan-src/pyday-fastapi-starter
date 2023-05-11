This repository includes a very simple Python FastAPI HTTP API, made for demonstration purposes only.

## Local development

1. Open this repository in Github Codespaces or VS Code with Remote Dev Containers extension.

2. Use [uvicorn](https://www.uvicorn.org/) to run the FastAPI app:

```console
uvicorn api.main:app --reload --port=8000
```

3. Click 'http://127.0.0.1:8000' in the terminal, which should open the website in a new tab.
4. Append `/docs` or `/generate_name` to the end of the URL.
5. Use '$ pip install -r requirements-dev.txt" to run install requirements
6. Use '$ pytest -k test_api" or "python3 -m pytest" to run your own test case
7. Use '$ pytest tests/property_based.py' to run the property based test
8. Use "$ python3 -m gunicorn api.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000" to run unicorn without unicorn.conf.py file
9. Use "$ python3 -m gunicorn main:app" to run gunicorn with gunicorn.conf.py file
