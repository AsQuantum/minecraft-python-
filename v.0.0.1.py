from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from test2 import *
from perlin_noise import PerlinNoise
app = Ursina()
window.fps_counter.enabled = False
window.exit_button.visible = False

grass_texture = Texture(grass_block())
stone_texture = Texture(model_texture("block", "stone", 16))
brick_texture = Texture(model_texture("block", "bricks", 16))
dirt_texture = Texture(model_texture("block", "dirt", 16))
block_pick = 1
punch_sound = Audio("assets/virtual/legacy/sound3/dig/stone1.ogg",loop=False,autoplay=False)

def update():
    global block_pick
    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
    if player.position.y < -5:
        player.position = Vec3(0, 0, 0)

def input(key):
    if key == 'escape':
        quit()
class Block(Button):
    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/minecraft/models/block/block',
            texture=texture,
            origin_y=0.5,
            scale=0.5,
            color=color.white,
            double_sided=True
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                destroy(self)
                punch_sound.play()
            if key == 'right mouse down':
                if block_pick == 1: block = Block(position=self.position + mouse.normal, texture=grass_texture)
                if block_pick == 2: block = Block(position=self.position + mouse.normal, texture=stone_texture)
                if block_pick == 3: block = Block(position=self.position + mouse.normal, texture=brick_texture)
                if block_pick == 4: block = Block(position=self.position + mouse.normal, texture=dirt_texture)
                punch_sound.play()

class Sky(Entity):
    def __init__(self):
        from PIL import Image
        super().__init__(
            parent=scene,
            model='sphere',
            color=color.white,
            scale=150,
            texture=Texture(Image.new("RGBA",(16, 16),(200,200,255))),
            double_sided=True
        )

class Hand(Entity):
    def __init__(self):
        from PIL import Image
        super().__init__(
            parent=camera.ui,
            model='sphere',
            color=color.white,
            scale=150,
            texture=Texture(Image.new("RGBA",(16, 16),(200,200,255))),
            double_sided=True
        )


noise = PerlinNoise(octaves = 3, seed = 2023)
player = FirstPersonController()
sky = Sky()
scale = 24
for z in range(20):
    for x in range(20):
        block = Block(position=(x, 0, z))
        block.y = floor(noise([x/scale, z/scale]) * 8)
app.run()
