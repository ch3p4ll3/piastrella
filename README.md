# Piastrella As A Service

## The base of a smart world

## How to with UV
- clone the repo
- install [uv](https://docs.astral.sh/uv/getting-started/installation/)
- `uv sync`
- run with: `fastapi dev`
- enjoy `http://localhost:8000/piastrella`

## How to poor edition
- clone the repo
- create venv: `python3 -m venv venv`
- activate it: `source ./venv/bin/activate`
- install dependencies: `pip install .`
- run with: `fastapi dev`
- enjoy `http://localhost:8000/piastrella`

## How to Docker edition
- Jonatan loves this edition
- clone the repo
- run `docker compose up --build -d`
- enjoy `http://localhost:8000/piastrella`
- also checkout `http://localhost:8000/docs`


Inspired by [No-as-a-Service](https://github.com/hotheadhacker/no-as-a-service)