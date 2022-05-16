# game setup
WIDTH = 1600
HEIGTH = 800
FPS = 60
TILESIZE = 64

# font
UI_FONT = 'graph/font/game_font.ttf'
UI_FONT_SIZE = 18
UI_HEALTH_FONT_SIZE = 25

# general colors
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = 'white'
TEXT_COLOR = '#EEEEEE'
HEALTH_TEXT_COLOR = 'red'

# weapons
weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15, 'graphic': '../graph/weapons/sword/full.png'},
    'lance': {'cooldown': 400, 'damage': 30, 'graphic': '../graph/weapons/lance/full.png'},
    'axe': {'cooldown': 300, 'damage': 20, 'graphic': '../graph/weapons/axe/full.png'},
    'rapier': {'cooldown': 50, 'damage': 8, 'graphic': '../graph/weapons/rapier/full.png'},
    'sai': {'cooldown': 80, 'damage': 10, 'graphic': '../graph/weapons/sai/full.png'}}
