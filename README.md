# Piastrella As A Service

![Behold, Piastrella](/piastrella.png)

## The base of a smart world
Piastrellas are integrated everyday in our lives, providing us with a comfortable, regular and most importantly of all stylish flooring, on which we step on.
This is why we created **Piastrella As A Service**, because we believe every person deserves every day to have something that can help them stand on their feet, happy and content.
This is not a subscription based service, it is a free program that we are giving you to improve your life. Enjoy Piastrella's emotionally charged, deep and profound phrases every day! Starting today, even with Docker!

### Satisfied clients

"Let Piastrella improve your life, as Piastrella improved mine" - D. I. M.
"I have never been happier, thank you Piastrella" - L. D. K.
"One day piastrelle exploded in my house, but then I downloaded Piastrella, now I am happier than ever" - F. B.
"Piastrella helped me getting a house, I am so happy, thank you Piastrella!" - M. C.
"If it wasn't for Piastrella, I would have not learned Italian!" - J. A.
"Piastrella came to me in a dream and promised happiness if I created this piece of software" - M. V.
"Piastrella helped me discover the best way to track down more Piastrellas, so that I can have all the Piastrellas I need" - O. M.
"Actually, Piastrella is really the best thing that happened to me. It helped me shift to the next gear" - V. C.
"Well, gosh darn! I had no place in the room for me to sit, but Piastrella adviced me the right way to deal with this, thank you Piastrella! I will report you as the best advicer I have ever known!" - T. C.

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