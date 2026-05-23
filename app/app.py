from fastapi import FastAPI, HTTPException

app = FastAPI()

text_posts = {
    1: "Learning Python is fun and powerful!",
    2: "Just finished building my first web app.",
    3: "Data structures and algorithms improve problem solving.",
    4: "Consistency beats motivation every time.",
    5: "Debugging code can feel like detective work.",
    6: "Frontend development is both creative and technical.",
    7: "Backend systems handle the logic behind applications.",
    8: "Open source contributions help developers grow.",
    9: "Building projects is the best way to learn coding.",
    10: "Never stop learning new technologies."
}

@app.get("/posts")
def get_all_post():
    return text_posts


@app.get("/posts/{id}")
def get_post(id: int): 
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)