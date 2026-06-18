import json
import math
import random
import time
import tkinter as tk
from pathlib import Path


WIDTH = 480
HEIGHT = 720
FPS_MS = 16
GROUND_Y = 625
SCORE_FILE = Path(__file__).with_name("flappy_bird_scores.json")

SKINS = [
    {
        "name": "Classic",
        "body": "#ffd343",
        "wing": "#efb92d",
        "beak": "#f28a24",
        "eye": "#111111",
    },
    {
        "name": "Blue",
        "body": "#4e9dff",
        "wing": "#2d67c7",
        "beak": "#ffd166",
        "eye": "#111111",
    },
    {
        "name": "Rose",
        "body": "#f06c9b",
        "wing": "#c53e74",
        "beak": "#ffcd5c",
        "eye": "#111111",
    },
    {
        "name": "Mint",
        "body": "#5ee0a0",
        "wing": "#26996a",
        "beak": "#ffb25c",
        "eye": "#111111",
    },
]

DIFFICULTIES = [
    {
        "name": "Easy",
        "gravity": 0.26,
        "flap": -6.8,
        "speed": 2.55,
        "gap": 188,
        "pipe_every": 108,
    },
    {
        "name": "Normal",
        "gravity": 0.32,
        "flap": -7.35,
        "speed": 3.15,
        "gap": 165,
        "pipe_every": 94,
    },
    {
        "name": "Hard",
        "gravity": 0.38,
        "flap": -7.8,
        "speed": 3.8,
        "gap": 142,
        "pipe_every": 82,
    },
]

THEMES = [
    {
        "name": "Day",
        "top": "#77c7f2",
        "bottom": "#d8f6ff",
        "hill1": "#73cc86",
        "hill2": "#58aa73",
        "ground": "#dcb85e",
        "grass": "#6ecf54",
        "pipe": "#33b957",
        "pipe_dark": "#1d813a",
    },
    {
        "name": "Sunset",
        "top": "#f09070",
        "bottom": "#ffd59a",
        "hill1": "#8fc479",
        "hill2": "#5f9368",
        "ground": "#d69a59",
        "grass": "#7fc75d",
        "pipe": "#28a85a",
        "pipe_dark": "#176f3b",
    },
    {
        "name": "Night",
        "top": "#1a2a55",
        "bottom": "#465f95",
        "hill1": "#3f805e",
        "hill2": "#2e654e",
        "ground": "#b8874f",
        "grass": "#4aa45d",
        "pipe": "#3bbf73",
        "pipe_dark": "#207c4c",
    },
]

HELP_LINES = [
    "GOAL",
    "Fly through the gap between pipes.",
    "Each pipe passed gives 1 point.",
    "Do not hit pipes, ceiling, or ground.",
    "",
    "CONTROLS",
    "Space, W, Up Arrow, or mouse click: flap.",
    "P: pause or resume.",
    "R: restart after game over.",
    "Esc: return to menu.",
    "",
    "SETTINGS",
    "Skin changes only the bird colors.",
    "Difficulty changes gravity, speed, and pipe gap.",
    "Theme changes the sky, hills, ground, and pipes.",
    "Sound uses the default Tkinter bell.",
    "",
    "CODE IDEAS",
    "Bird velocity starts at 0.",
    "Gravity increases velocity every frame.",
    "Flap gives the bird a negative velocity.",
    "Negative velocity moves the bird upward.",
    "Positive velocity moves the bird downward.",
    "Pipes move left every frame.",
    "A new pipe appears after a timer reaches a limit.",
    "The pipe gap is made from one center point.",
    "Collision uses circle versus rectangle math.",
    "Score is added after the bird passes a pipe.",
    "High scores are saved in a JSON file.",
    "",
    "LEARNING TASKS",
    "Try changing WIDTH and HEIGHT.",
    "Try changing GROUND_Y.",
    "Try changing gravity in DIFFICULTIES.",
    "Try changing pipe speed in DIFFICULTIES.",
    "Try adding a new bird skin.",
    "Try adding a new theme.",
    "Try making pipes red after score 20.",
    "Try adding coins between pipes.",
    "Try adding a countdown before start.",
    "Try adding moving pipes.",
    "Try adding a shield power-up.",
    "Try adding sound files later with pygame.",
    "",
    "GOOD HABITS",
    "Keep variables clear and readable.",
    "Put repeated drawing code inside functions.",
    "Use classes for objects with their own data.",
    "Test one change at a time.",
    "Read error messages from top to bottom.",
    "Do not make code longer without a reason.",
]

MEDALS = [
    {"name": "No Medal", "score": 0, "color": "#8a98a8"},
    {"name": "Bronze", "score": 5, "color": "#b87333"},
    {"name": "Silver", "score": 10, "color": "#c0c0c0"},
    {"name": "Gold", "score": 20, "color": "#ffd343"},
    {"name": "Platinum", "score": 35, "color": "#b9f2ff"},
    {"name": "Master", "score": 50, "color": "#d99cff"},
]

ACHIEVEMENTS = [
    {"name": "First Flight", "score": 1},
    {"name": "Pipe Rookie", "score": 3},
    {"name": "Bird Pilot", "score": 5},
    {"name": "Steady Wings", "score": 8},
    {"name": "Sky Runner", "score": 12},
    {"name": "Cloud Cutter", "score": 16},
    {"name": "Pipe Master", "score": 20},
    {"name": "High Flyer", "score": 28},
    {"name": "Feather Legend", "score": 36},
    {"name": "Flappy Champion", "score": 50},
]


def clamp(value, low, high):
    return max(low, min(high, value))


def lerp(a, b, t):
    return a + (b - a) * t


def hex_to_rgb(value):
    value = value.lstrip("#")
    return tuple(int(value[index:index + 2], 16) for index in (0, 2, 4))


def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)


def blend(color_a, color_b, t):
    a = hex_to_rgb(color_a)
    b = hex_to_rgb(color_b)
    return rgb_to_hex(
        (
            int(lerp(a[0], b[0], t)),
            int(lerp(a[1], b[1], t)),
            int(lerp(a[2], b[2], t)),
        )
    )


def circle_rect_collision(cx, cy, radius, rect):
    left, top, right, bottom = rect
    closest_x = clamp(cx, left, right)
    closest_y = clamp(cy, top, bottom)
    distance_x = cx - closest_x
    distance_y = cy - closest_y
    return distance_x * distance_x + distance_y * distance_y <= radius * radius


def read_scores():
    if not SCORE_FILE.exists():
        return []
    try:
        with open(SCORE_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (OSError, json.JSONDecodeError):
        return []
    if isinstance(data, list):
        return data
    return []


def write_scores(scores):
    try:
        with open(SCORE_FILE, "w", encoding="utf-8") as file:
            json.dump(scores[:10], file, indent=2)
    except OSError:
        pass


class Button:
    def __init__(self, x, y, width, height, text, action):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.action = action

    def contains(self, x, y):
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

    def draw(self, canvas, mouse_x, mouse_y):
        hovered = self.contains(mouse_x, mouse_y)
        fill = "#5f86b6" if hovered else "#45698d"
        outline = "#c7e4ff" if hovered else "#8fb2d3"
        canvas.create_rectangle(
            self.x,
            self.y,
            self.x + self.width,
            self.y + self.height,
            fill=fill,
            outline=outline,
            width=2,
        )
        canvas.create_text(
            self.x + self.width / 2,
            self.y + self.height / 2,
            text=self.text,
            fill="white",
            font=("Arial", 15, "bold"),
        )


class Cloud:
    def __init__(self, x, y, scale, speed):
        self.x = x
        self.y = y
        self.scale = scale
        self.speed = speed

    def update(self):
        self.x -= self.speed
        if self.x < -140:
            self.x = WIDTH + random.randint(20, 180)
            self.y = random.randint(70, 250)
            self.scale = random.uniform(0.65, 1.25)

    def draw(self, canvas):
        color = "#ffffff"
        parts = [
            (0, 16, 22),
            (24, 4, 30),
            (56, 18, 24),
            (32, 24, 27),
        ]
        for offset_x, offset_y, radius in parts:
            r = radius * self.scale
            cx = self.x + offset_x * self.scale
            cy = self.y + offset_y * self.scale
            canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill=color, outline="")


class Particle:
    def __init__(self, x, y, dx, dy, color, radius, life):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color
        self.radius = radius
        self.life = life
        self.max_life = life

    def update(self):
        self.life -= 1
        self.x += self.dx
        self.y += self.dy
        self.dy += 0.05

    def alive(self):
        return self.life > 0

    def draw(self, canvas):
        if self.life <= 0:
            return
        ratio = self.life / self.max_life
        r = self.radius * ratio
        canvas.create_oval(self.x - r, self.y - r, self.x + r, self.y + r, fill=self.color, outline="")


class Bird:
    def __init__(self, skin):
        self.skin = skin
        self.x = 130
        self.y = 300
        self.radius = 18
        self.velocity = 0
        self.angle = 0
        self.wing_phase = 0

    def reset(self):
        self.x = 130
        self.y = 300
        self.velocity = 0
        self.angle = 0
        self.wing_phase = 0

    def set_skin(self, skin):
        self.skin = skin

    def flap(self, power):
        self.velocity = power
        self.wing_phase = 1.0

    def idle(self, frame):
        self.y = 300 + math.sin(frame * 0.08) * 9
        self.velocity = 0
        self.angle = -0.15
        self.wing_phase = (math.sin(frame * 0.2) + 1) / 2

    def update(self, gravity):
        self.velocity += gravity
        self.velocity = clamp(self.velocity, -10, 10)
        self.y += self.velocity
        self.angle = clamp(self.velocity * 0.08, -0.65, 1.25)
        self.wing_phase *= 0.82

    def hit_box(self):
        shrink = 3
        return (
            self.x - self.radius + shrink,
            self.y - self.radius + shrink,
            self.x + self.radius - shrink,
            self.y + self.radius - shrink,
        )

    def draw(self, canvas):
        r = self.radius
        body = self.skin["body"]
        wing = self.skin["wing"]
        beak = self.skin["beak"]
        eye = self.skin["eye"]

        tilt = self.angle
        beak_x = self.x + math.cos(tilt) * r * 1.25
        beak_y = self.y + math.sin(tilt) * r * 1.25

        canvas.create_oval(
            self.x - r,
            self.y - r * 0.8,
            self.x + r * 1.1,
            self.y + r * 0.85,
            fill=body,
            outline="#111111",
            width=2,
        )
        wing_y = self.y + 5 + self.wing_phase * 4
        canvas.create_oval(
            self.x - r * 0.75,
            wing_y - r * 0.35,
            self.x + r * 0.15,
            wing_y + r * 0.38,
            fill=wing,
            outline="#111111",
            width=2,
        )
        canvas.create_polygon(
            beak_x,
            beak_y,
            beak_x + 18,
            beak_y - 7,
            beak_x + 18,
            beak_y + 7,
            fill=beak,
            outline="#111111",
        )
        eye_x = self.x + r * 0.45
        eye_y = self.y - r * 0.28
        canvas.create_oval(eye_x - 6, eye_y - 6, eye_x + 6, eye_y + 6, fill="white", outline="#111111")
        canvas.create_oval(eye_x - 2, eye_y - 2, eye_x + 3, eye_y + 3, fill=eye, outline="")


class PipePair:
    def __init__(self, x, gap_y, gap_size, speed, theme):
        self.x = x
        self.gap_y = gap_y
        self.gap_size = gap_size
        self.speed = speed
        self.width = 74
        self.scored = False
        self.theme = theme

    def update(self):
        self.x -= self.speed

    def off_screen(self):
        return self.x + self.width < -10

    def top_rect(self):
        return (self.x, 0, self.x + self.width, self.gap_y - self.gap_size / 2)

    def bottom_rect(self):
        return (self.x, self.gap_y + self.gap_size / 2, self.x + self.width, GROUND_Y)

    def passed_by(self, bird):
        if not self.scored and self.x + self.width < bird.x:
            self.scored = True
            return True
        return False

    def collides(self, bird):
        cx = bird.x
        cy = bird.y
        radius = bird.radius - 3
        return circle_rect_collision(cx, cy, radius, self.top_rect()) or circle_rect_collision(cx, cy, radius, self.bottom_rect())

    def draw_pipe_rect(self, canvas, rect):
        left, top, right, bottom = rect
        pipe = self.theme["pipe"]
        pipe_dark = self.theme["pipe_dark"]
        canvas.create_rectangle(left, top, right, bottom, fill=pipe, outline=pipe_dark, width=3)
        canvas.create_rectangle(left + 11, top, left + 22, bottom, fill=blend(pipe, "#ffffff", 0.18), outline="")
        canvas.create_line(right - 9, top + 4, right - 9, bottom - 4, fill=pipe_dark, width=3)

    def draw(self, canvas):
        top = self.top_rect()
        bottom = self.bottom_rect()
        cap_h = 28
        self.draw_pipe_rect(canvas, top)
        self.draw_pipe_rect(canvas, bottom)

        top_cap = (self.x - 7, top[3] - cap_h, self.x + self.width + 7, top[3])
        bottom_cap = (self.x - 7, bottom[1], self.x + self.width + 7, bottom[1] + cap_h)
        self.draw_pipe_rect(canvas, top_cap)
        self.draw_pipe_rect(canvas, bottom_cap)


class ScoreBoard:
    def __init__(self):
        self.scores = read_scores()

    def best_score(self):
        if not self.scores:
            return 0
        return max(item.get("score", 0) for item in self.scores)

    def add(self, score, difficulty, skin):
        entry = {
            "score": int(score),
            "difficulty": difficulty,
            "skin": skin,
        }
        self.scores.append(entry)
        self.scores.sort(key=lambda item: item.get("score", 0), reverse=True)
        self.scores = self.scores[:10]
        write_scores(self.scores)


class MedalSystem:
    def medal_for_score(self, score):
        current = MEDALS[0]
        for medal in MEDALS:
            if score >= medal["score"]:
                current = medal
        return current

    def next_medal(self, score):
        for medal in MEDALS:
            if score < medal["score"]:
                return medal
        return None

    def draw_medal(self, canvas, x, y, score):
        medal = self.medal_for_score(score)
        canvas.create_oval(x - 32, y - 32, x + 32, y + 32, fill=medal["color"], outline="#ffffff", width=3)
        canvas.create_oval(x - 18, y - 18, x + 18, y + 18, fill="#1d2d40", outline="#ffffff", width=2)
        canvas.create_text(x, y, text=str(int(score)), fill="white", font=("Arial", 14, "bold"))
        canvas.create_text(x, y + 48, text=medal["name"], fill="#e8f0ff", font=("Arial", 12, "bold"))

    def draw_next_goal(self, canvas, x, y, score):
        next_medal = self.next_medal(score)
        if next_medal is None:
            text = "All medals unlocked"
        else:
            needed = next_medal["score"] - score
            text = "{} more point(s) for {}".format(int(needed), next_medal["name"])
        canvas.create_text(x, y, text=text, fill="#d9ecff", font=("Arial", 11, "bold"))


class AchievementSystem:
    def unlocked_for_score(self, score):
        unlocked = []
        for achievement in ACHIEVEMENTS:
            if score >= achievement["score"]:
                unlocked.append(achievement)
        return unlocked

    def locked_for_score(self, score):
        locked = []
        for achievement in ACHIEVEMENTS:
            if score < achievement["score"]:
                locked.append(achievement)
        return locked

    def latest_unlocked(self, score):
        unlocked = self.unlocked_for_score(score)
        if unlocked:
            return unlocked[-1]
        return None

    def next_achievement(self, score):
        locked = self.locked_for_score(score)
        if locked:
            return locked[0]
        return None

    def draw_summary(self, canvas, x, y, score):
        unlocked = self.unlocked_for_score(score)
        canvas.create_text(
            x,
            y,
            anchor="w",
            text="Achievements: {}/{}".format(len(unlocked), len(ACHIEVEMENTS)),
            fill="#e8f0ff",
            font=("Arial", 12, "bold"),
        )

        latest = self.latest_unlocked(score)
        if latest is None:
            latest_text = "Latest: none"
        else:
            latest_text = "Latest: " + latest["name"]

        canvas.create_text(
            x,
            y + 24,
            anchor="w",
            text=latest_text,
            fill="#d9ecff",
            font=("Arial", 11),
        )

        next_item = self.next_achievement(score)
        if next_item is None:
            next_text = "Next: all done"
        else:
            next_text = "Next: {} at {} pts".format(next_item["name"], next_item["score"])

        canvas.create_text(
            x,
            y + 46,
            anchor="w",
            text=next_text,
            fill="#d9ecff",
            font=("Arial", 11),
        )

    def draw_full_list(self, canvas, x, y, score):
        for index, achievement in enumerate(ACHIEVEMENTS):
            unlocked = score >= achievement["score"]
            mark = "OK" if unlocked else "--"
            color = "#4fd67c" if unlocked else "#98a5b5"
            row = "{}  {} - {} pts".format(mark, achievement["name"], achievement["score"])
            canvas.create_text(
                x,
                y + index * 24,
                anchor="w",
                text=row,
                fill=color,
                font=("Arial", 11, "bold"),
            )


class FlappyBirdGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Flappy Bird 1000")
        self.root.resizable(False, False)
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT, highlightthickness=0)
        self.canvas.pack()

        self.state = "menu"
        self.skin_index = 0
        self.difficulty_index = 1
        self.theme_index = 0
        self.sound_enabled = True

        self.score_board = ScoreBoard()
        self.medals = MedalSystem()
        self.achievements = AchievementSystem()
        self.bird = Bird(SKINS[self.skin_index])
        self.pipes = []
        self.clouds = [
            Cloud(40, 115, 0.95, 0.18),
            Cloud(240, 190, 0.75, 0.12),
            Cloud(400, 90, 1.05, 0.10),
        ]
        self.particles = []
        self.buttons = []

        self.frame = 0
        self.score = 0
        self.saved_score = False
        self.pipe_timer = 0
        self.ground_scroll = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.last_time = time.perf_counter()

        self.root.bind("<KeyPress>", self.on_key_press)
        self.root.bind("<Motion>", self.on_mouse_move)
        self.root.bind("<Button-1>", self.on_click)
        self.root.protocol("WM_DELETE_WINDOW", self.quit_game)

        self.loop()

    def difficulty(self):
        return DIFFICULTIES[self.difficulty_index]

    def theme(self):
        return THEMES[self.theme_index]

    def quit_game(self):
        self.root.destroy()

    def beep(self):
        if self.sound_enabled:
            self.root.bell()

    def new_game(self):
        self.state = "playing"
        self.score = 0
        self.saved_score = False
        self.pipe_timer = 0
        self.ground_scroll = 0
        self.pipes = []
        self.particles = []
        self.bird.set_skin(SKINS[self.skin_index])
        self.bird.reset()
        self.spawn_pipe(WIDTH + 120)
        self.spawn_pipe(WIDTH + 120 + 215)

    def game_over(self):
        if self.state != "playing":
            return
        self.state = "game_over"
        self.beep()
        if not self.saved_score:
            self.score_board.add(
                self.score,
                self.difficulty()["name"],
                SKINS[self.skin_index]["name"],
            )
            self.saved_score = True

    def spawn_pipe(self, x=None):
        settings = self.difficulty()
        if x is None:
            x = WIDTH + 60
        min_y = 165
        max_y = GROUND_Y - 160
        gap_y = random.randint(min_y, max_y)
        self.pipes.append(
            PipePair(
                x=x,
                gap_y=gap_y,
                gap_size=settings["gap"],
                speed=settings["speed"],
                theme=self.theme(),
            )
        )

    def flap(self):
        if self.state == "menu":
            self.new_game()
            return
        if self.state == "game_over":
            self.new_game()
            return
        if self.state == "paused":
            self.state = "playing"
            return
        if self.state != "playing":
            return

        self.bird.flap(self.difficulty()["flap"])
        self.beep()
        for _ in range(4):
            self.particles.append(
                Particle(
                    self.bird.x - 15,
                    self.bird.y + random.randint(-5, 8),
                    random.uniform(-1.4, -0.4),
                    random.uniform(-0.7, 0.8),
                    "#ffffff",
                    random.uniform(2.5, 4.5),
                    random.randint(18, 30),
                )
            )

    def on_key_press(self, event):
        key = event.keysym.lower()
        if key in ("space", "up", "w"):
            self.flap()
        elif key == "p":
            if self.state == "playing":
                self.state = "paused"
            elif self.state == "paused":
                self.state = "playing"
        elif key == "r":
            self.new_game()
        elif key == "escape":
            if self.state in ("playing", "paused", "game_over", "settings", "scores", "help"):
                self.state = "menu"
            else:
                self.quit_game()

    def on_mouse_move(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y

    def on_click(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y
        for button in self.buttons:
            if button.contains(event.x, event.y):
                self.handle_action(button.action)
                return
        self.flap()

    def handle_action(self, action):
        if action == "start":
            self.new_game()
        elif action == "settings":
            self.state = "settings"
        elif action == "scores":
            self.state = "scores"
        elif action == "help":
            self.state = "help"
        elif action == "menu":
            self.state = "menu"
        elif action == "quit":
            self.quit_game()
        elif action == "restart":
            self.new_game()
        elif action == "resume":
            self.state = "playing"
        elif action == "skin_prev":
            self.skin_index = (self.skin_index - 1) % len(SKINS)
            self.bird.set_skin(SKINS[self.skin_index])
        elif action == "skin_next":
            self.skin_index = (self.skin_index + 1) % len(SKINS)
            self.bird.set_skin(SKINS[self.skin_index])
        elif action == "difficulty":
            self.difficulty_index = (self.difficulty_index + 1) % len(DIFFICULTIES)
        elif action == "theme":
            self.theme_index = (self.theme_index + 1) % len(THEMES)
        elif action == "sound":
            self.sound_enabled = not self.sound_enabled

    def update_background(self):
        for cloud in self.clouds:
            cloud.update()
        self.ground_scroll = (self.ground_scroll - self.difficulty()["speed"]) % 28

    def update_particles(self):
        for particle in self.particles:
            particle.update()
        self.particles = [particle for particle in self.particles if particle.alive()]

    def update_playing(self):
        settings = self.difficulty()
        self.bird.update(settings["gravity"])
        self.pipe_timer += 1
        if self.pipe_timer >= settings["pipe_every"]:
            self.pipe_timer = 0
            self.spawn_pipe()

        for pipe in self.pipes:
            pipe.update()
            if pipe.passed_by(self.bird):
                self.score += 1
                self.beep()
                self.particles.append(
                    Particle(
                        self.bird.x,
                        self.bird.y - 20,
                        0,
                        -1.2,
                        "#ffd343",
                        6,
                        28,
                    )
                )

        self.pipes = [pipe for pipe in self.pipes if not pipe.off_screen()]

        if self.bird.y - self.bird.radius <= 0:
            self.game_over()
        if self.bird.y + self.bird.radius >= GROUND_Y:
            self.bird.y = GROUND_Y - self.bird.radius
            self.game_over()
        for pipe in self.pipes:
            if pipe.collides(self.bird):
                self.game_over()
                break

    def update(self):
        self.frame += 1
        self.update_background()
        self.update_particles()
        if self.state == "menu":
            self.bird.idle(self.frame)
        elif self.state == "playing":
            self.update_playing()
        elif self.state == "game_over":
            if self.bird.y + self.bird.radius < GROUND_Y:
                self.bird.update(self.difficulty()["gravity"])

    def draw_gradient_background(self):
        theme = self.theme()
        steps = 24
        for index in range(steps):
            y1 = int(index * HEIGHT / steps)
            y2 = int((index + 1) * HEIGHT / steps)
            color = blend(theme["top"], theme["bottom"], index / max(1, steps - 1))
            self.canvas.create_rectangle(0, y1, WIDTH, y2, fill=color, outline="")

    def draw_world(self):
        theme = self.theme()
        self.draw_gradient_background()

        if theme["name"] == "Night":
            for index in range(18):
                x = (index * 73 + 31) % WIDTH
                y = 35 + (index * 47) % 230
                self.canvas.create_oval(x - 1, y - 1, x + 2, y + 2, fill="white", outline="")
        else:
            self.canvas.create_oval(365, 60, 425, 120, fill="#ffe681", outline="")

        for cloud in self.clouds:
            cloud.draw(self.canvas)

        self.canvas.create_polygon(
            -20,
            GROUND_Y,
            82,
            470,
            185,
            GROUND_Y,
            fill=theme["hill1"],
            outline="",
        )
        self.canvas.create_polygon(
            120,
            GROUND_Y,
            290,
            430,
            500,
            GROUND_Y,
            fill=theme["hill2"],
            outline="",
        )
        self.canvas.create_polygon(
            300,
            GROUND_Y,
            405,
            475,
            520,
            GROUND_Y,
            fill=theme["hill1"],
            outline="",
        )

    def draw_ground(self):
        theme = self.theme()
        self.canvas.create_rectangle(0, GROUND_Y, WIDTH, HEIGHT, fill=theme["ground"], outline="")
        self.canvas.create_rectangle(0, GROUND_Y, WIDTH, GROUND_Y + 18, fill=theme["grass"], outline="")
        self.canvas.create_line(0, GROUND_Y + 18, WIDTH, GROUND_Y + 18, fill="#27663a", width=3)
        start = int(self.ground_scroll) - 28
        for x in range(start, WIDTH + 28, 28):
            self.canvas.create_rectangle(x, GROUND_Y + 42, x + 12, GROUND_Y + 49, fill="#a57745", outline="")
            self.canvas.create_rectangle(x + 12, GROUND_Y + 67, x + 27, GROUND_Y + 73, fill="#e9c878", outline="")

    def draw_particles(self):
        for particle in self.particles:
            particle.draw(self.canvas)

    def draw_score(self):
        text = str(int(self.score))
        self.canvas.create_text(WIDTH / 2 + 3, 82 + 3, text=text, fill="#333333", font=("Arial", 44, "bold"))
        self.canvas.create_text(WIDTH / 2, 82, text=text, fill="white", font=("Arial", 44, "bold"))

    def draw_status_bar(self):
        best = self.score_board.best_score()
        label = "Best: {}   Difficulty: {}   Skin: {}".format(
            best,
            self.difficulty()["name"],
            SKINS[self.skin_index]["name"],
        )
        self.canvas.create_rectangle(0, 0, WIDTH, 34, fill="#1b2533", outline="")
        self.canvas.create_text(14, 17, anchor="w", text=label, fill="#e8f0ff", font=("Arial", 11, "bold"))

    def draw_game_scene(self):
        self.draw_world()
        for pipe in self.pipes:
            pipe.draw(self.canvas)
        self.draw_particles()
        self.draw_ground()
        self.bird.draw(self.canvas)
        self.draw_status_bar()
        self.draw_score()

    def draw_buttons(self):
        for button in self.buttons:
            button.draw(self.canvas, self.mouse_x, self.mouse_y)

    def draw_menu(self):
        self.buttons = [
            Button(150, 285, 180, 48, "START", "start"),
            Button(150, 345, 180, 48, "SETTINGS", "settings"),
            Button(150, 405, 180, 48, "SCORES", "scores"),
            Button(150, 465, 180, 48, "HELP", "help"),
            Button(150, 525, 180, 48, "QUIT", "quit"),
        ]
        self.draw_game_scene()
        self.canvas.create_rectangle(42, 132, 438, 255, fill="#1d2d40", outline="#7fa8c8", width=3)
        self.canvas.create_text(WIDTH / 2, 170, text="FLAPPY BIRD", fill="white", font=("Arial", 34, "bold"))
        self.canvas.create_text(
            WIDTH / 2,
            215,
            text="Space / click to fly",
            fill="#d9ecff",
            font=("Arial", 14, "bold"),
        )
        self.draw_buttons()

    def draw_settings(self):
        self.buttons = [
            Button(54, 612, 160, 48, "BACK", "menu"),
            Button(100, 240, 48, 44, "<", "skin_prev"),
            Button(332, 240, 48, 44, ">", "skin_next"),
            Button(150, 345, 180, 48, self.difficulty()["name"], "difficulty"),
            Button(150, 415, 180, 48, self.theme()["name"], "theme"),
            Button(150, 485, 180, 48, "Sound: " + ("ON" if self.sound_enabled else "OFF"), "sound"),
        ]
        self.draw_world()
        self.draw_ground()
        self.canvas.create_text(WIDTH / 2, 118, text="SETTINGS", fill="white", font=("Arial", 34, "bold"))
        self.canvas.create_text(WIDTH / 2, 192, text="Bird Skin", fill="#e8f0ff", font=("Arial", 16, "bold"))
        self.canvas.create_rectangle(170, 222, 310, 304, fill="#1d2d40", outline="#7fa8c8", width=2)
        preview = Bird(SKINS[self.skin_index])
        preview.x = WIDTH / 2
        preview.y = 263
        preview.wing_phase = 0.8
        preview.draw(self.canvas)
        self.canvas.create_text(
            WIDTH / 2,
            322,
            text=SKINS[self.skin_index]["name"],
            fill="white",
            font=("Arial", 13, "bold"),
        )
        self.canvas.create_text(WIDTH / 2, 380, text="Difficulty", fill="#d9ecff", font=("Arial", 11))
        self.canvas.create_text(WIDTH / 2, 450, text="Theme", fill="#d9ecff", font=("Arial", 11))
        self.canvas.create_text(WIDTH / 2, 520, text="Sound", fill="#d9ecff", font=("Arial", 11))
        self.draw_buttons()

    def draw_scores(self):
        self.buttons = [
            Button(54, 612, 160, 48, "BACK", "menu"),
        ]
        self.draw_world()
        self.draw_ground()
        self.canvas.create_rectangle(60, 125, 420, 555, fill="#1d2d40", outline="#7fa8c8", width=3)
        self.canvas.create_text(WIDTH / 2, 168, text="HIGH SCORES", fill="white", font=("Arial", 28, "bold"))
        if not self.score_board.scores:
            self.canvas.create_text(WIDTH / 2, 270, text="No score yet", fill="#d9ecff", font=("Arial", 15))
        else:
            y = 225
            for index, item in enumerate(self.score_board.scores[:10], start=1):
                row = "{}. {} pts | {} | {}".format(
                    index,
                    item.get("score", 0),
                    item.get("difficulty", "Normal"),
                    item.get("skin", "Classic"),
                )
                self.canvas.create_text(92, y, anchor="w", text=row, fill="#e8f0ff", font=("Arial", 13, "bold"))
                y += 30
        self.draw_buttons()

    def draw_paused(self):
        self.buttons = [
            Button(150, 340, 180, 48, "RESUME", "resume"),
            Button(150, 405, 180, 48, "MENU", "menu"),
        ]
        self.draw_game_scene()
        self.canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="#000000", stipple="gray50", outline="")
        self.canvas.create_rectangle(84, 230, 396, 470, fill="#1d2d40", outline="#7fa8c8", width=3)
        self.canvas.create_text(WIDTH / 2, 285, text="PAUSED", fill="white", font=("Arial", 30, "bold"))
        self.draw_buttons()

    def draw_game_over(self):
        self.buttons = [
            Button(82, 455, 150, 48, "RESTART", "restart"),
            Button(248, 455, 150, 48, "MENU", "menu"),
        ]
        self.draw_game_scene()
        self.canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="#000000", stipple="gray50", outline="")
        self.canvas.create_rectangle(58, 220, 422, 525, fill="#1d2d40", outline="#7fa8c8", width=3)
        self.canvas.create_text(WIDTH / 2, 270, text="GAME OVER", fill="white", font=("Arial", 30, "bold"))
        self.canvas.create_text(WIDTH / 2, 330, text="Score: {}".format(int(self.score)), fill="#e8f0ff", font=("Arial", 19, "bold"))
        self.canvas.create_text(WIDTH / 2, 366, text="Best: {}".format(self.score_board.best_score()), fill="#e8f0ff", font=("Arial", 17, "bold"))
        self.canvas.create_text(WIDTH / 2, 404, text="Press R to restart", fill="#d9ecff", font=("Arial", 13))
        self.draw_buttons()

    def draw(self):
        self.canvas.delete("all")
        if self.state == "menu":
            self.draw_menu()
        elif self.state == "settings":
            self.draw_settings()
        elif self.state == "scores":
            self.draw_scores()
        elif self.state == "playing":
            self.buttons = []
            self.draw_game_scene()
        elif self.state == "paused":
            self.draw_paused()
        elif self.state == "game_over":
            self.draw_game_over()

    def loop(self):
        now = time.perf_counter()
        self.last_time = now
        self.update()
        self.draw()
        self.root.after(FPS_MS, self.loop)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    game = FlappyBirdGame()
    game.run()
