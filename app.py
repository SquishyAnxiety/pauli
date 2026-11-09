import json
import os
import random

from flask import Flask, jsonify, render_template, request

HERE = os.path.dirname(os.path.abspath(__file__))
MAX_LENGTH = 1000

with open(os.path.join(HERE, "dictionary", "nouns.json"), encoding="utf-8") as f:
    NOUNS = [(n["article"], n["noun"]) for n in json.load(f)]
with open(os.path.join(HERE, "dictionary", "adjectives.json"), encoding="utf-8") as f:
    ADJECTIVES = json.load(f)


def convert(content):
    rng = random.Random(content)
    article, noun = rng.choice(NOUNS)
    return f"{article} {rng.choice(ADJECTIVES)} {noun}"


app = Flask(__name__, template_folder=HERE)
app.json.ensure_ascii = False


@app.get("/")
def index():
    return render_template("index.html", max_length=MAX_LENGTH, example=convert("monster energy"))


@app.post("/api")
def api_endpoint():
    data = request.get_json(silent=True)
    content = data.get("content") if isinstance(data, dict) else None
    if not isinstance(content, str) or len(content) > MAX_LENGTH:
        return jsonify(status=f'send JSON like {{ "content": "your text" }}, at most {MAX_LENGTH} characters'), 400
    return jsonify(result=convert(content))


@app.get("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(port=int(os.getenv("PORT", 8000)))
