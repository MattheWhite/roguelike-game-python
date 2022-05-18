# game setup
WIDTH = 1600
HEIGTH = 800
FPS = 60
TILESIZE = 64


# bar size
BAR_HEIGHT = 30
HEALTH_BAR_WIDTH = 200
ITEM_BOX_SIZE = 80

# font
UI_FONT = 'graph/font/game_font.ttf'
UI_FONT_SIZE = 18
UI_HEALTH_FONT_SIZE = 25

# general colors
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#8E8E8E'
TEXT_COLOR = '#EEEEEE'
HEALTH_TEXT_COLOR = 'red'
UI_BORDER_COLOR_ACTIVE = 'gold'

# weapons
weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15, 'graphic': 'graph/weapons/sword/full.png'},
    'lance': {'cooldown': 400, 'damage': 30, 'graphic': 'graph/weapons/lance/full.png'},
    'axe': {'cooldown': 300, 'damage': 20, 'graphic': 'graph/weapons/axe/full.png'},
    'rapier': {'cooldown': 50, 'damage': 8, 'graphic': 'graph/weapons/rapier/full.png'},
    'sai': {'cooldown': 80, 'damage': 10, 'graphic': 'graph/weapons/sai/full.png'}}

# enemy
monster_data = {
	'squid': {'health': 100, 'exp': 100, 'damage': 20, 'attack_type': 'slash', 'attack_sound': 'audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
	'Boss': {'health': 300, 'exp': 250, 'damage': 40, 'attack_type': 'claw',  'attack_sound': 'audio/attack/claw.wav', 'speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
	'spirit': {'health': 100, 'exp': 110, 'damage': 8, 'attack_type': 'thunder', 'attack_sound': 'audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
	'bamboo': {'health': 70, 'exp': 120, 'damage': 6, 'attack_type': 'leaf_attack', 'attack_sound': 'audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}}