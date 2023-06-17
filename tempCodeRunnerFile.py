from PIL import Image, ImageDraw, ImageFont

img = Image.new(mode="RGBA", size=(400,300), color='darkorange')
draw = ImageDraw.Draw(img)

text="Hello World!"
font = ImageFont.truetype('consola.ttf', 100)
draw.text((10, 0), "HEllo",font = font, fill='white')
img.show()