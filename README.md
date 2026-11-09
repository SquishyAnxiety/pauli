<p align="center">
  <img src="static/cat.svg" alt="pauli logo" width="40">
</p>

**pauli** turns any text into a random (and funny) german word. The dictionary currently has `~5k` adjectives and `~50k` nouns.

Usage:

```sh
pip install -r requirements.txt
python app.py    # http://localhost:8000

# or use Docker
docker build -t pauli . && docker run -p 8000:8000 pauli
```

## API

```sh
curl -X POST -H "Content-Type: application/json" -d '{ "content": "john pork" }' localhost:8000/api
```

`content` must be a valid string, max. 1000 characters.