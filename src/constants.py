from enum import Enum


class AsteroidKind(Enum):
    SMALL = (1, 25)  # (radius, score)
    MEDIUM = (2, 100)
    LARGE = (3, 250)


GAME_FPS = 60

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FONT_SIZE = 28
FONT_STYLE_PATH = "asteroids-game/assets/pixeloid_sans.ttf"

HEART_ICON_PATH = "asteroids-game/assets/heart_icon.png"
LIVES_POSITION = (10, 10)
SCORE_POSITION = (10, 45)

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = len(AsteroidKind)
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
ASTEROID_COLORS = ["gray", "dim gray", "dark gray"]
ASTEROID_RANDOM_NUM_VERTICES_CONSTRAINTS = (
    10,
    15,
)  # Random number of vertices for the polygon
ASTEROID_RANDOM_RADIUS_FACTOR_CONSTRAINTS = (
    0.8,
    1.2,
)  # Random variation to the radius to create a rugged look
ASTEROID_RANDOM_SPLIT_ANGLE_CONSTRAINTS = (
    20,
    50,
)  # Random angle in which split asteroids will move

PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 200
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN = 0.3
PLAYER_MAX_LIVES = 3
PLAYER_RESPAWN_COOLDOWN = 0.5
PLAYER_COLOR = "white"

SHOT_RADIUS = 5
SHOT_COLOR = "red"

EXPLOSION_CIRCLES_NUM = 8
EXPLOSION_RANDOM_RADIUS_FACTOR = (0.3, 1.0)  # Random radius factor for each circle
EXPLOSION_RANDOM_ORIGIN_OFFSET_CONSTRAINTS = (
    -5,
    5,
)  # Random origin offsets for each circle (small jitter)
EXPLOSION_COLORS = [
    (255, 69, 0),  # Orange-Red
    (255, 140, 0),  # Dark Orange
    (255, 215, 0),  # Gold
    (255, 255, 0),  # Yellow
]

GAME_OVER_TEXT_CENTER_HEIGHT_OFFSET = -75
GAME_OVER_FINAL_SCORE_CENTER_HEIGHT_OFFSET = 0
GAME_OVER_EXIT_BUTTON_CENTER_LEFT_OFFSET = -100
GAME_OVER_EXIT_BUTTON_CENTER_HEIGHT_OFFSET = 50
GAME_OVER_EXIT_BUTTON_WIDTH = 200
GAME_OVER_EXIT_BUTTON_HEIGHT = 50
