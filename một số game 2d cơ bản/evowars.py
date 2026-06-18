import pygame
import sys
import math
import random

# --- KHỞI TẠO HỆ THỐNG ---
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 750
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("EvoWars.io Offline Edition - Python")
clock = pygame.time.Clock()
font_sys = pygame.font.SysFont("Arial", 16, bold=True)
font_large = pygame.font.SysFont("Arial", 32, bold=True)

# Bản đồ thế giới ngầm
WORLD_WIDTH, WORLD_HEIGHT = 3000, 3000

# Bảng màu
BG_COLOR = (30, 30, 40)
GRID_COLOR = (45, 45, 55)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 50, 50)
BLUE = (50, 150, 255)
YELLOW = (255, 200, 0)
GREEN = (50, 200, 50)


# --- LỚP ĐỐI TƯỢNG: HẠT KINH NGHIỆM ---
class Orb:
    def __init__(self):
        self.x = random.randint(50, WORLD_WIDTH - 50)
        self.y = random.randint(50, WORLD_HEIGHT - 50)
        self.color = random.choice([RED, BLUE, YELLOW, GREEN, WHITE])
        self.radius = random.randint(4, 7)
        self.xp_value = self.radius

    def draw(self, surface, cam_x, cam_y):
        screen_x, screen_y = int(self.x - cam_x), int(self.y - cam_y)
        if -20 < screen_x < SCREEN_WIDTH + 20 and -20 < screen_y < SCREEN_HEIGHT + 20:
            pygame.draw.circle(surface, self.color, (screen_x, screen_y), self.radius)


# --- LỚP ĐỐI TƯỢNG: CHIẾN BINH (PLAYER & BOT) ---
class Warrior:
    def __init__(self, x, y, color, name, is_bot=False):
        self.x = x
        self.y = y
        self.color = color
        self.name = name
        self.is_bot = is_bot
        self.is_dead = False

        # Chỉ số tiến hóa
        self.level = 1
        self.xp = 0
        self.max_xp = 30
        self.base_speed = 4.5

        # Chỉ số vật lý thay đổi theo cấp độ
        self.update_stats()

        # Hướng di chuyển và Tấn công
        self.angle = 0
        self.is_swinging = False
        self.swing_progress = 0  # Từ 0 đến 1
        self.swing_speed = 0.08
        self.swing_arc = math.pi * 0.7  # Góc vung vũ khí (Khoảng 126 độ)
        self.cooldown = 0

        # AI Logic
        self.target_orb = None

    def update_stats(self):
        # Lên cấp: To hơn, vũ khí dài hơn, nhưng chạy chậm lại
        self.radius = 15 + (self.level * 3)
        self.weapon_length = self.radius + 20 + (self.level * 6)
        self.speed = max(1.5, self.base_speed - (self.level * 0.15))

    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= self.max_xp:
            self.xp -= self.max_xp
            self.level += 1
            self.max_xp = int(self.max_xp * 1.5)
            self.update_stats()

    def attack(self):
        if not self.is_swinging and self.cooldown <= 0:
            self.is_swinging = True
            self.swing_progress = 0

    def update(self, target_x, target_y):
        if self.is_dead: return

        # Xử lý thời gian hồi chiêu
        if self.cooldown > 0:
            self.cooldown -= 1

        # Xử lý đòn vung vũ khí (Swing)
        if self.is_swinging:
            self.swing_progress += self.swing_speed
            if self.swing_progress >= 1:
                self.is_swinging = False
                self.swing_progress = 0
                self.cooldown = 20  # Delay trước nhát chém tiếp theo

        # Tính toán hướng đi
        dx = target_x - self.x
        dy = target_y - self.y
        dist = math.hypot(dx, dy)

        # Xoay mặt về phía mục tiêu
        if dist > 0:
            self.angle = math.atan2(dy, dx)

        # Di chuyển (Bots dừng lại khi đánh, Player di chuyển liên tục)
        if dist > self.speed and (not self.is_bot or not self.is_swinging):
            self.x += math.cos(self.angle) * self.speed
            self.y += math.sin(self.angle) * self.speed

        # Giới hạn bản đồ
        self.x = max(self.radius, min(self.x, WORLD_WIDTH - self.radius))
        self.y = max(self.radius, min(self.y, WORLD_HEIGHT - self.radius))

    def check_hit(self, other_warrior):
        # Kiểm tra xem vũ khí có chém trúng kẻ địch không
        if not self.is_swinging or other_warrior.is_dead:
            return False

        dist = math.hypot(other_warrior.x - self.x, other_warrior.y - self.y)
        if dist < self.weapon_length + other_warrior.radius:
            # Kiểm tra góc vung (Hitbox hình quạt)
            angle_to_enemy = math.atan2(other_warrior.y - self.y, other_warrior.x - self.x)

            # Tính góc vũ khí hiện tại
            current_weapon_angle = self.angle - (self.swing_arc / 2) + (self.swing_arc * self.swing_progress)

            # Chuẩn hóa khác biệt góc
            angle_diff = (angle_to_enemy - current_weapon_angle + math.pi) % (2 * math.pi) - math.pi

            # Nếu kẻ địch nằm trong vùng quét của vũ khí
            if abs(angle_diff) < 0.4:
                return True
        return False

    def draw(self, surface, cam_x, cam_y):
        if self.is_dead: return
        screen_x, screen_y = int(self.x - cam_x), int(self.y - cam_y)

        # Vẽ vũ khí (Kiếm/Gậy)
        if self.is_swinging:
            w_angle = self.angle - (self.swing_arc / 2) + (self.swing_arc * self.swing_progress)
        else:
            w_angle = self.angle - 0.5  # Tư thế cầm vũ khí khi nghỉ

        end_x = screen_x + math.cos(w_angle) * self.weapon_length
        end_y = screen_y + math.sin(w_angle) * self.weapon_length
        pygame.draw.line(surface, WHITE, (screen_x, screen_y), (end_x, end_y), int(5 + self.level))

        # Vẽ thân nhân vật
        pygame.draw.circle(surface, self.color, (screen_x, screen_y), int(self.radius))
        pygame.draw.circle(surface, BLACK, (screen_x, screen_y), int(self.radius), 3)

        # Vẽ tên và Cấp độ
        txt = font_sys.render(f"{self.name} (Lv.{self.level})", True, WHITE)
        surface.blit(txt, (screen_x - txt.get_width() // 2, screen_y - self.radius - 20))


# --- KHỞI TẠO GAME TRẠNG THÁI ---
player = Warrior(WORLD_WIDTH // 2, WORLD_HEIGHT // 2, BLUE, "YOU")
orbs = [Orb() for _ in range(800)]
bots = []
bot_names = ["Slayer", "Titan", "NoobMaster", "Shadow", "Berserker", "Viking", "Samurai"]

for i in range(15):
    b = Warrior(random.randint(100, WORLD_WIDTH - 100), random.randint(100, WORLD_HEIGHT - 100), RED,
                random.choice(bot_names), True)
    bots.append(b)

# --- VÒNG LẶP CHÍNH ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            player.attack()

    # Nhập liệu chuột cho Player
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Tính tọa độ Camera khóa vào Player
    if not player.is_dead:
        cam_x = player.x - SCREEN_WIDTH // 2
        cam_y = player.y - SCREEN_HEIGHT // 2

        # Tọa độ thực tế của chuột trên World
        world_mouse_x = mouse_x + cam_x
        world_mouse_y = mouse_y + cam_y
        player.update(world_mouse_x, world_mouse_y)

    # Cập nhật Bots
    all_warriors = [player] + bots
    dead_bots = []

    for bot in bots:
        # AI Đơn giản: Tìm hạt gần nhất nếu chưa có
        if not bot.target_orb or bot.target_orb not in orbs:
            if orbs:
                bot.target_orb = random.choice(orbs)

        target_x, target_y = bot.x, bot.y
        if bot.target_orb:
            target_x, target_y = bot.target_orb.x, bot.target_orb.y

        # Tự động tấn công nếu có ai lại gần
        for other in all_warriors:
            if other != bot and not other.is_dead:
                dist = math.hypot(other.x - bot.x, other.y - bot.y)
                if dist < bot.weapon_length + 20:
                    target_x, target_y = other.x, other.y
                    bot.attack()
                    break

        bot.update(target_x, target_y)

    # Kiểm tra va chạm (Ăn Orbs và Chém nhau)
    for w in all_warriors:
        if w.is_dead: continue

        # Ăn Orbs
        for orb in orbs[:]:
            if math.hypot(w.x - orb.x, w.y - orb.y) < w.radius + orb.radius:
                w.gain_xp(orb.xp_value)
                orbs.remove(orb)
                orbs.append(Orb())  # Spawn lại hạt mới

        # Chém nhau
        for target in all_warriors:
            if w != target and w.check_hit(target):
                target.is_dead = True
                w.gain_xp(target.level * 15)  # Giết địch được nhiều XP

                # Giải phóng xác thành hạt XP khổng lồ
                for _ in range(target.level * 3):
                    o = Orb()
                    o.x = target.x + random.randint(-30, 30)
                    o.y = target.y + random.randint(-30, 30)
                    o.radius = 10
                    o.xp_value = 5
                    orbs.append(o)

    # Loại bỏ bot chết, hồi sinh bot mới
    bots = [b for b in bots if not b.is_dead]
    while len(bots) < 15:
        bots.append(Warrior(random.randint(100, WORLD_WIDTH - 100), random.randint(100, WORLD_HEIGHT - 100), RED,
                            random.choice(bot_names), True))

    # --- KẾT XUẤT ĐỒ HỌA (RENDER) ---
    screen.fill(BG_COLOR)

    # Vẽ lưới nền thế giới
    start_x = int(cam_x // 100) * 100
    start_y = int(cam_y // 100) * 100
    for x in range(start_x, int(cam_x + SCREEN_WIDTH + 100), 100):
        pygame.draw.line(screen, GRID_COLOR, (x - cam_x, 0), (x - cam_x, SCREEN_HEIGHT))
    for y in range(start_y, int(cam_y + SCREEN_HEIGHT + 100), 100):
        pygame.draw.line(screen, GRID_COLOR, (0, y - cam_y), (SCREEN_WIDTH, y - cam_y))

    # Vẽ ranh giới bản đồ
    pygame.draw.rect(screen, RED, (-cam_x, -cam_y, WORLD_WIDTH, WORLD_HEIGHT), 5)

    # Vẽ vật thể
    for orb in orbs: orb.draw(screen, cam_x, cam_y)

    # Sắp xếp để người cấp nhỏ (bé hơn) được vẽ trước, người cấp to đè lên trên
    for w in sorted(all_warriors, key=lambda w: w.radius):
        w.draw(screen, cam_x, cam_y)

    # UI: Điểm số & Thanh kinh nghiệm
    if not player.is_dead:
        score_txt = font_large.render(f"LEVEL: {player.level}", True, WHITE)
        screen.blit(score_txt, (20, 20))

        # Vẽ thanh XP
        pygame.draw.rect(screen, BLACK, (20, 60, 200, 20))
        xp_width = int(200 * (player.xp / player.max_xp))
        pygame.draw.rect(screen, BLUE, (20, 60, xp_width, 20))
        pygame.draw.rect(screen, WHITE, (20, 60, 200, 20), 2)
    else:
        go_txt = font_large.render("BẠN ĐÃ BỊ HẠ GỤC! Chạy lại Code để hồi sinh.", True, RED)
        screen.blit(go_txt, (SCREEN_WIDTH // 2 - go_txt.get_width() // 2, SCREEN_HEIGHT // 2))

    pygame.display.update()
    clock.tick(60)