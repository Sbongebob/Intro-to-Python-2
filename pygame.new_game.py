import tkinter as tk
import random

# -------------------------
# Window Setup
# -------------------------
root = tk.Tk()
root.title("Catch the Star")
root.geometry("600x600")

canvas = tk.Canvas(root, width=600, height=600, bg="black")
canvas.pack()

# -------------------------
# Player
# -------------------------
player = canvas.create_rectangle(250, 550, 350, 570, fill="cyan")

score = 0
misses = 0
speed = 5

score_text = canvas.create_text(
    80, 20,
    text=f"Score: {score}",
    fill="white",
    font=("Arial", 16)
)

miss_text = canvas.create_text(
    500, 20,
    text=f"Misses: {misses}/3",
    fill="white",
    font=("Arial", 16)
)

# -------------------------
# Star
# -------------------------
star = canvas.create_oval(
    random.randint(20, 580),
    0,
    random.randint(20, 580) + 20,
    20,
    fill="yellow"
)


def move_left(event):
    x1, _, x2, _ = canvas.coords(player)
    if x1 > 0:
        canvas.move(player, -25, 0)


def move_right(event):
    x1, _, x2, _ = canvas.coords(player)
    if x2 < 600:
        canvas.move(player, 25, 0)


root.bind("<Left>", move_left)
root.bind("<Right>", move_right)


def create_new_star():
    global star
    x = random.randint(20, 560)
    star = canvas.create_oval(x, 0, x + 20, 20, fill="yellow")


def update():
    global score, misses, speed, star

    canvas.move(star, 0, speed)

    sx1, sy1, sx2, sy2 = canvas.coords(star)
    px1, py1, px2, py2 = canvas.coords(player)

    # Collision
    if sy2 >= py1 and sx2 >= px1 and sx1 <= px2:
        score += 1
        canvas.itemconfig(score_text, text=f"Score: {score}")

        if score % 10 == 0:
            speed += 1

        canvas.delete(star)
        create_new_star()

    # Missed
    elif sy2 > 600:
        misses += 1
        canvas.itemconfig(miss_text, text=f"Misses: {misses}/3")

        canvas.delete(star)
        create_new_star()

    # Game Over
    if misses >= 3:
        canvas.create_text(
            300,
            300,
            text=f"GAME OVER\nFinal Score: {score}",
            fill="red",
            font=("Arial", 30)
        )
        return

    root.after(30, update)


update()
root.mainloop()
