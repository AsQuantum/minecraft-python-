from ursina import *

app = Ursina()


class Test_cube(Entity):
    def __init__(self):
        super().__init__(
            model="cube",
            texture='assets/minecraft/textures/block/grass_block_top.png',
            rotation=Vec3(45, 45, 45)
        )


class Test_button(Button):
    def __init__(self, highlight_texture=None):
        super().__init__(
            parent=scene,
            model='cube',
            texture='assets/minecraft/textures/gui/sprites/widget/button.png',
            color=color.white,
            text="test",
            text_color=color.white
        )
        self.highlight_texture = 'assets/minecraft/textures/gui/sprites/widget/button_highlighted.png'

    def input(self, key):
        if self.disabled or not self.model:
            return

        if key == 'left mouse down':
            if self.hovered:
                self.model.setColorScale(self.pressed_color)
                self.model.setScale(Vec3(self.pressed_scale, self.pressed_scale, 1))

        if key == 'left mouse up':
            if self.hovered:
                self.model.setColorScale(self.highlight_color)
                self.model.setScale(Vec3(self.highlight_scale, self.highlight_scale, 1))
            else:
                self.model.setColorScale(self.color)
                self.model.setScale(Vec3(1, 1, 1))

    def on_mouse_enter(self):
        if not self.disabled and self.model:
            self.model.setColorScale(self.highlight_color)

            # change highlight texture
            self.icon_setter(self.highlight_texture)

            if self.highlight_scale != 1:
                self.model.setScale(Vec3(self.highlight_scale, self.highlight_scale, 1))

        if hasattr(self, 'tooltip') and self.tooltip:
            self.tooltip.enabled = True

    def on_mouse_exit(self):
        if not self.disabled and self.model:
            self.model.setColorScale(self.color)

            # change highlight texture
            self.icon_setter(self.texture)

            if not mouse.left and self.highlight_scale != 1:
                self.model.setScale(Vec3(1, 1, 1))

        if hasattr(self, 'tooltip') and self.tooltip:
            self.tooltip.enabled = False


def update():
    if held_keys['a']:
        test.x -= 1 * time.dt


test = Entity(model="cube", color=color.orange, scale=2, position=(5, 0))
test2 = Text(text="codinghou", scale=2)
test4 = Test_cube()
test5 = Test_button()
app.run()
