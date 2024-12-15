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
BACKGROUND_PATH = "asteroids-game/assets/starry_sky.png"

HEART_ICON_PATH = "asteroids-game/assets/heart_icon.png"
LIVES_POSITION = (10, 10)
SCORE_POSITION = (10, 45)

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = len(AsteroidKind)
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_BASE_SPEED_MIN = 40
ASTEROID_BASE_SPEED_MAX = 100
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
ASTEROID_COLORS = ["gray27", "gray49", "gray55", "peachpuff4", "wheat4"]
ASTEROID_RANDOM_NUM_VERTICES_CONSTRAINTS = (
    15,
    20,
)  # Random number of vertices for the polygon
ASTEROID_RANDOM_RADIUS_FACTOR_CONSTRAINTS = (
    1.15,
    1.55,
)  # Random variation to the radius to create a rugged look
ASTEROID_RANDOM_SPLIT_ANGLE_CONSTRAINTS = (
    20,
    50,
)  # Random angle in which split asteroids will move
ASTEROID_IMMUNITY_COOLDOWN = 1.0 # Time in seconds during which newly spawned asteroids cannot collide with each other
ASTEROID_NUM_CRATERS_CONSTRAINTS = (4, 7)
ASTEROID_CRATER_DARKEN_BY = 0.8 # Factor by which each color will be darkened (0.8 means 20%)

PLAYER_SIZE = 25
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 200
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN = 0.3
PLAYER_MAX_LIVES = 3
PLAYER_RESPAWN_COOLDOWN = 0.5
PLAYER_IMAGE_PATH = "asteroids-game/assets/spaceship.png"

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
GAME_OVER_BUTTON_CENTER_LEFT_OFFSET = -100
GAME_OVER_BUTTON_CENTER_HEIGHT_OFFSET = 50
GAME_OVER_BUTTON_WIDTH = 200
GAME_OVER_BUTTON_HEIGHT = 50

PAUSE_MENU_PANEL_WIDTH = 400
PAUSE_MENU_PANEL_HEIGHT = 229
PAUSE_MENU_BUTTON_WIDTH_OFFSET = 40
PAUSE_MENU_BUTTON_HEIGHT = 50
PAUSE_MENU_BUTTON_LEFT_OFFSET = 20
PAUSE_MENU_BUTTON_TOP_BASE_OFFSET = 20
PAUSE_MENU_BUTTON_TOP_CONSECUTIVE_OFFSET = (
    PAUSE_MENU_BUTTON_HEIGHT + PAUSE_MENU_BUTTON_TOP_BASE_OFFSET
)
