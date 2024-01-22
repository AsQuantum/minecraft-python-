from PIL import Image, ImageDraw, ImageOps

# app = Ursina()
def grass_block():
    im1 = Image.open('assets/minecraft/textures/block/grass_block_side.png')
    new_im = Image.new("RGBA", (im1.size[0] * 4, im1.size[0] * 4))
    im2 = Image.open('assets/minecraft/textures/block/grass_block_top.png')

    im2_ = Image.new("RGBA", im2.size, "#91bd59")
    im2_.putalpha(im2.convert("L"))
    im2 = Image.new("RGBA", im2.size, "#000000")
    im2 = Image.alpha_composite(im2, im2_)

    im3 = Image.open('assets/minecraft/textures/block/dirt.png')
    im4 = Image.open('assets/minecraft/textures/block/grass_block_side_overlay.png')

    im4_ = Image.new("RGBA", im4.size, "#91bd59")
    im4_.putalpha(im4.convert("L"))
    im4.paste(Image.new("RGBA", im4.size, "#000000"), (0, 0), im4)
    im4 = Image.alpha_composite(im4, im4_)

    new_im.paste(im2, (int(im1.size[0] * 2.5), im1.size[0] * 1))
    new_im.paste(im3, (int(im1.size[0] * 0.5), im1.size[0] * 1))

    new_im.paste(im1.rotate(270), (int(im1.size[0] * 1.5), im1.size[0] * 0))
    new_im.paste(im1.rotate(270), (int(im1.size[0] * 1.5), im1.size[0] * 1))
    new_im.paste(im1.rotate(270), (int(im1.size[0] * 1.5), im1.size[0] * 2))
    new_im.paste(im1.rotate(270), (int(im1.size[0] * 1.5), im1.size[0] * 3))

    new_im.paste(im4.rotate(270), (int(im1.size[0] * 1.5), im1.size[0] * 0), im4.rotate(270))
    new_im.paste(im4.rotate(270), (int(im1.size[0] * 1.5), im1.size[0] * 1), im4.rotate(270))
    new_im.paste(im4.rotate(270), (int(im1.size[0] * 1.5), im1.size[0] * 2), im4.rotate(270))
    new_im.paste(im4.rotate(270), (int(im1.size[0] * 1.5), im1.size[0] * 3), im4.rotate(270))

    return new_im

def model_texture(type, nbt, pixel):
    texture_img = Image.open(f'assets/minecraft/textures/{type}/{nbt}.png')
    model_texture_img = Image.new("RGBA", (4 * pixel, 4 * pixel))
    model_texture_img.paste(texture_img, (int(pixel * 2.5), int(pixel * 1)))
    model_texture_img.paste(texture_img, (int(pixel * 0.5), int(pixel * 1)))
    model_texture_img.paste(texture_img.rotate(270), (int(pixel * 1.5), int(pixel * 0)))
    model_texture_img.paste(texture_img.rotate(270), (int(pixel * 1.5), int(pixel * 1)))
    model_texture_img.paste(texture_img.rotate(270), (int(pixel * 1.5), int(pixel * 2)))
    model_texture_img.paste(texture_img.rotate(270), (int(pixel * 1.5), int(pixel * 3)))
    return model_texture_img
