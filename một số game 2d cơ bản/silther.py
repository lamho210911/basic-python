import pygame
import sys
import random
import math

# --- 1. KHỞI TẠO HỆ THỐNG ---
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 750
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Slither.io V2.0 - Menu, Skins & 2 Players")
clock = pygame.time.Clock()

# Kích thước map
WORLD_WIDTH, WORLD_HEIGHT = 3500, 3500

# Bảng màu
DARK_BG = (10, 14, 22)
GRID_COLOR = (24, 33, 48)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 65, 54)
BLUE = (0, 116, 217)
GREEN = (46, 204, 113)
YELLOW = (255, 220, 0)
PURPLE = (177, 13, 201)
ORANGE = (255, 133, 27)
CYAN = (0, 255, 255)
GRAY = (100, 100, 100)

SKINS = [BLUE, RED, GREEN, YELLOW, PURPLE, CYAN]

# Font
font_small = pygame.font.SysFont("Arial", 18, bold=True)
font_medium = pygame.font.SysFont("Arial", 28, bold=True)
font_large = pygame.font.SysFont("Arial", 50, bold=True)
font_title = pygame.font.SysFont("Arial", 80, bold=True)

# Biến toàn cục (Cài đặt)
game_state = "MENU"  # MENU, PLAYING, SETTINGS, SKIN
difficulty = "NORMAL"  # EASY, NORMAL, HARD
player_skin_idx = 0
is_2_player_mode = False


# --- 2. LỚP ĐỐI TƯỢNG GAME ---

class Food:
    def __init__(self, x=None, y=None, is_big=False):
        self.pos = pygame.math.Vector2(
            int(x) if x is not None else random.randint(50, WORLD_WIDTH - 50),
            int(y) if y is not None else random.randint(50, WORLD_HEIGHT - 50)
        )
        self.is_big = is_big
        self.color = random.choice([RED, BLUE, GREEN, YELLOW, PURPLE, CYAN])
        self.radius = random.randint(5, 8) if not is_big else random.randint(12, 16)
        self.value = 1 if not is_big else 5

    def draw(self, surface, camera_pos):
        screen_pos = self.pos - camera_pos
        if -20 < screen_pos.x < SCREEN_WIDTH + 20 and -20 < screen_pos.y < SCREEN_HEIGHT + 20:
            pygame.draw.circle(surface, self.color, (int(screen_pos.x), int(screen_pos.y)), int(self.radius))
            pygame.draw.circle(surface, WHITE, (int(screen_pos.x), int(screen_pos.y)), int(self.radius // 2))


class Snake:
    def __init__(self, x, y, color, name, ctrl_type="bot"):
        self.name = name
        self.color = color
        self.ctrl_type = ctrl_type  # 'mouse' (P1), 'keys' (P2), 'bot'

        self.pos = pygame.math.Vector2(x, y)
        self.angle = random.uniform(0, 2 * math.pi)
        self.velocity = pygame.math.Vector2(math.cos(self.angle), math.sin(self.angle))

        # Chỉ số dựa trên độ khó
        self.base_speed = 3.5 if ctrl_type != "bot" else (
            2.5 if difficulty == "EASY" else (3.5 if difficulty == "NORMAL" else 4.5))
        self.speed = self.base_speed

        self.score = 0
        self.segment_radius = 16
        self.segment_distance = 8
        self.is_dead = False

        self.body = [pygame.math.Vector2(self.pos)]
        for i in range(25):
            self.body.append(pygame.math.Vector2(self.pos.x - i * self.segment_distance, self.pos.y))

        self.bot_timer = 0

    def update(self, target_pos, boost_active, foods):
        if self.is_dead: return

        # Xử lý Boost
        if boost_active and len(self.body) > 15:
            self.speed = self.base_speed * 1.8
            if random.random() < 0.1:
                last_seg = self.body.pop()
                foods.append(Food(int(last_seg.x), int(last_seg.y), is_big=False))
                self.score = max(0, self.score - 1)
        else:
            self.speed = self.base_speed

        # Xử lý Hướng đi
        if self.ctrl_type == "mouse":
            # Điều khiển bằng chuột (Player 1)
            move_vec = target_pos - pygame.math.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            if move_vec.length() > 0:
                self.velocity = move_vec.normalize()

        elif self.ctrl_type == "keys":
            # Điều khiển bằng phím WASD (Player 2)
            keys = pygame.key.get_pressed()
            turn_speed = 0.08
            if keys[pygame.K_a]: self.angle -= turn_speed
            if keys[pygame.K_d]: self.angle += turn_speed
            self.velocity = pygame.math.Vector2(math.cos(self.angle), math.sin(self.angle))

        else:
            # Điều khiển bằng BOT AI
            self.bot_timer += 1
            if self.bot_timer > (60 if difficulty == "EASY" else 30):
                self.bot_timer = 0
                # Bot khó sẽ ưu tiên tìm mồi
                if difficulty in ["NORMAL", "HARD"]:
                    closest_food = min(foods, key=lambda f: self.pos.distance_to(f.pos), default=None)
                    if closest_food and self.pos.distance_to(closest_food.pos) < 300:
                        vec = closest_food.pos - self.pos
                        if vec.length() > 0:
                            self.angle = math.atan2(vec.y, vec.x)
                    else:
                        self.angle += random.uniform(-1, 1)
                else:
                    self.angle += random.uniform(-0.5, 0.5)

            self.velocity = pygame.math.Vector2(math.cos(self.angle), math.sin(self.angle))

        # Di chuyển
        self.pos += self.velocity * self.speed
        self.body[0] = pygame.math.Vector2(self.pos)

        # Chuyển động khớp đuôi
        for i in range(1, len(self.body)):
            prev = self.body[i - 1]
            curr = self.body[i]
            direction = curr - prev
            if direction.length() > self.segment_distance:
                direction = direction.normalize()
                self.body[i] = prev + direction * self.segment_distance

        # Khóa biên đồ thị
        self.pos.x = max(40, min(self.pos.x, WORLD_WIDTH - 40))
        self.pos.y = max(40, min(self.pos.y, WORLD_HEIGHT - 40))

        # Phóng to rắn
        self.segment_radius = 16 + int(math.sqrt(self.score) * 0.4)
        self.segment_distance = max(6, self.segment_radius // 2)

    def draw(self, surface, camera_pos):
        if self.is_dead: return
        for i in range(len(self.body) - 1, -1, -1):
            screen_pos = self.body[i] - camera_pos
            if -50 < screen_pos.x < SCREEN_WIDTH + 50 and -50 < screen_pos.y < SCREEN_HEIGHT + 50:
                color = self.color if i % 2 == 0 else WHITE
                pygame.draw.circle(surface, color, (int(screen_pos.x), int(screen_pos.y)), int(self.segment_radius))
                if i == 0:
                    name_surface = font_small.render(f"{self.name} ({self.score})", True, WHITE)
                    surface.blit(name_surface, (int(screen_pos.x) - name_surface.get_width() // 2,
                                                int(screen_pos.y) - int(self.segment_radius) - 22))


# --- 3. HÀM HỖ TRỢ UI VÀ ĐỒ HỌA ---
def draw_button(surface, text, x, y, w, h, default_color, hover_color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    rect = pygame.Rect(x, y, w, h)

    is_hovered = rect.collidepoint(mouse)
    color = hover_color if is_hovered else default_color

    pygame.draw.rect(surface, color, rect, border_radius=10)
    pygame.draw.rect(surface, WHITE, rect, 3, border_radius=10)

    text_surf = font_medium.render(text, True, WHITE)
    surface.blit(text_surf, (x + (w - text_surf.get_width()) // 2, y + (h - text_surf.get_height()) // 2))

    return is_hovered and click[0]


def draw_grid(surface, camera_pos):
    grid_size = 100
    start_x = int(camera_pos.x // grid_size) * grid_size
    start_y = int(camera_pos.y // grid_size) * grid_size

    for x in range(int(start_x), int(start_x + SCREEN_WIDTH + grid_size), grid_size):
        if 0 <= x <= WORLD_WIDTH:
            pygame.draw.line(surface, GRID_COLOR, (int(x - camera_pos.x), 0), (int(x - camera_pos.x), SCREEN_HEIGHT), 1)

    for y in range(int(start_y), int(start_y + SCREEN_HEIGHT + grid_size), grid_size):
        if 0 <= y <= WORLD_HEIGHT:
            pygame.draw.line(surface, GRID_COLOR, (0, int(y - camera_pos.y)), (SCREEN_WIDTH, int(y - camera_pos.y)), 1)


# --- 4. KHỞI TẠO BIẾN TRÒ CHƠI ---
foods = []
bots = []
p1 = None
p2 = None


def init_game(two_players=False):
    global foods, bots, p1, p2, is_2_player_mode
    is_2_player_mode = two_players
    foods = [Food() for _ in range(600)]

    p1 = Snake(WORLD_WIDTH // 2, WORLD_HEIGHT // 2, SKINS[player_skin_idx], "P1 (Mouse)", "mouse")
    if two_players:
        p2 = Snake(WORLD_WIDTH // 2 + 100, WORLD_HEIGHT // 2, ORANGE, "P2 (WASD)", "keys")
    else:
        p2 = None

    num_bots = 8 if difficulty == "EASY" else (12 if difficulty == "NORMAL" else 20)
    bots = []
    for i in range(num_bots):
        bots.append(
            Snake(random.randint(200, WORLD_WIDTH - 200), random.randint(200, WORLD_HEIGHT - 200), random.choice(SKINS),
                  f"Bot_{i}", "bot"))


# --- 5. VÒNG LẶP CHÍNH CỦA GAME ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(DARK_BG)

    # =============== TRẠNG THÁI: MENU CHÍNH ===============
    if game_state == "MENU":
        title = font_title.render("SLITHER.IO V2.0", True, GREEN)
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))

        if draw_button(screen, "PLAY (1 PLAYER)", SCREEN_WIDTH // 2 - 150, 250, 300, 60, BLUE, CYAN):
            init_game(two_players=False)
            game_state = "PLAYING"
            pygame.time.delay(200)

        if draw_button(screen, "PLAY (2 PLAYERS)", SCREEN_WIDTH // 2 - 150, 330, 300, 60, ORANGE, YELLOW):
            init_game(two_players=True)
            game_state = "PLAYING"
            pygame.time.delay(200)

        if draw_button(screen, "SETTINGS", SCREEN_WIDTH // 2 - 150, 410, 300, 60, GRAY, WHITE):
            game_state = "SETTINGS"
            pygame.time.delay(200)

        if draw_button(screen, "SKINS", SCREEN_WIDTH // 2 - 150, 490, 300, 60, PURPLE, RED):
            game_state = "SKIN"
            pygame.time.delay(200)

    # =============== TRẠNG THÁI: CHỌN SKIN ===============
    elif game_state == "SKIN":
        title = font_large.render("SELECT PLAYER 1 SKIN", True, WHITE)
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))

        # Hiển thị màu hiện tại
        pygame.draw.circle(screen, SKINS[player_skin_idx], (SCREEN_WIDTH // 2, 300), 60)
        pygame.draw.circle(screen, WHITE, (SCREEN_WIDTH // 2, 300), 60, 4)

        if draw_button(screen, "< PREV", SCREEN_WIDTH // 2 - 200, 270, 100, 60, GRAY, WHITE):
            player_skin_idx = (player_skin_idx - 1) % len(SKINS)
            pygame.time.delay(150)

        if draw_button(screen, "NEXT >", SCREEN_WIDTH // 2 + 100, 270, 100, 60, GRAY, WHITE):
            player_skin_idx = (player_skin_idx + 1) % len(SKINS)
            pygame.time.delay(150)

        if draw_button(screen, "BACK TO MENU", SCREEN_WIDTH // 2 - 150, 500, 300, 60, RED, PURPLE):
            game_state = "MENU"
            pygame.time.delay(200)

    # =============== TRẠNG THÁI: CÀI ĐẶT ===============
    elif game_state == "SETTINGS":
        title = font_large.render("SETTINGS - DIFFICULTY", True, WHITE)
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))

        curr_diff = font_medium.render(f"CURRENT: {difficulty}", True, YELLOW)
        screen.blit(curr_diff, (SCREEN_WIDTH // 2 - curr_diff.get_width() // 2, 200))

        if draw_button(screen, "EASY", SCREEN_WIDTH // 2 - 150, 280, 300, 50, GREEN if difficulty == "EASY" else GRAY,
                       GREEN):
            difficulty = "EASY"
        if draw_button(screen, "NORMAL", SCREEN_WIDTH // 2 - 150, 350, 300, 50,
                       BLUE if difficulty == "NORMAL" else GRAY, BLUE):
            difficulty = "NORMAL"
        if draw_button(screen, "HARD", SCREEN_WIDTH // 2 - 150, 420, 300, 50, RED if difficulty == "HARD" else GRAY,
                       RED):
            difficulty = "HARD"

        if draw_button(screen, "BACK TO MENU", SCREEN_WIDTH // 2 - 150, 550, 300, 60, RED, PURPLE):
            game_state = "MENU"
            pygame.time.delay(200)

    # =============== TRẠNG THÁI: ĐANG CHƠI ===============
    elif game_state == "PLAYING":
        mouse_pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        p1_boost = pygame.mouse.get_pressed()[0]
        p2_boost = keys[pygame.K_SPACE] or keys[pygame.K_w]

        while len(foods) < 600:
            foods.append(Food())

        # Cập nhật rắn
        if not p1.is_dead: p1.update(mouse_pos, p1_boost, foods)
        if is_2_player_mode and not p2.is_dead: p2.update(None, p2_boost, foods)

        for bot in bots:
            bot.update(None, False, foods)

        all_snakes = [s for s in [p1, p2] + bots if s and not s.is_dead]

        # Xử lý va chạm
        for snake in all_snakes:
            # Ăn mồi
            for food in foods[:]:
                if snake.pos.distance_to(food.pos) < snake.segment_radius + food.radius:
                    snake.score += food.value
                    for _ in range(food.value): snake.body.append(pygame.math.Vector2(snake.body[-1]))
                    foods.remove(food)

            # Va chạm giữa các rắn (Đầu chạm Thân)
            for other_snake in all_snakes:
                if snake == other_snake: continue
                for segment in other_snake.body:
                    if snake.pos.distance_to(segment) < snake.segment_radius + other_snake.segment_radius * 0.7:
                        snake.is_dead = True
                        for seg in snake.body[::2]: foods.append(Food(int(seg.x), int(seg.y), is_big=True))
                        break
                if snake.is_dead: break

        # Xóa bot chết & Sinh bot mới
        dead_bots = [b for b in bots if b.is_dead]
        for db in dead_bots:
            bots.remove(db)
            bots.append(Snake(random.randint(200, WORLD_WIDTH - 200), random.randint(200, WORLD_HEIGHT - 200),
                              random.choice(SKINS), "Bot_New", "bot"))

        # Camera đuổi theo P1 (Nếu P1 chết, đuổi theo P2)
        target_cam_snake = p1 if not p1.is_dead else p2
        if target_cam_snake and not target_cam_snake.is_dead:
            camera_pos = target_cam_snake.pos - pygame.math.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        else:
            # Game Over hoàn toàn
            game_state = "MENU"
            continue

        # Render Game
        draw_grid(screen, camera_pos)
        pygame.draw.rect(screen, RED, (int(-camera_pos.x), int(-camera_pos.y), WORLD_WIDTH, WORLD_HEIGHT), 6)

        for food in foods: food.draw(screen, camera_pos)
        for bot in bots: bot.draw(screen, camera_pos)
        if is_2_player_mode and not p2.is_dead: p2.draw(screen, camera_pos)
        if not p1.is_dead: p1.draw(screen, camera_pos)

        # Leaderboard mini
        lb_bg = pygame.Surface((220, 180), pygame.SRCALPHA)
        lb_bg.fill((20, 30, 45, 200))
        screen.blit(lb_bg, (SCREEN_WIDTH - 230, 10))
        for i, s in enumerate(sorted(all_snakes, key=lambda x: x.score, reverse=True)[:5]):
            txt = font_small.render(f"#{i + 1} {s.name}: {s.score}", True, s.color)
            screen.blit(txt, (SCREEN_WIDTH - 220, 20 + i * 30))

        if is_2_player_mode:
            info = font_small.render("P1: Mouse (Click to Boost) | P2: WASD (Space to Boost)", True, WHITE)
            screen.blit(info, (10, 10))

        if draw_button(screen, "QUIT TO MENU", 10, SCREEN_HEIGHT - 50, 150, 40, RED, PURPLE):
            game_state = "MENU"

    pygame.display.update()
    clock.tick(60)