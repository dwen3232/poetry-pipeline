from PIL import Image, ImageDraw, ImageFont


def create_image(size, bgColor, message, font, fontColor):
    W, H = size
    image = Image.new('RGB', size, bgColor)
    draw = ImageDraw.Draw(image)
    _, _, w, h = draw.textbbox((0, 0), message, font=font)
    draw.text(((W-w)/2, (H-h)/2), message, font=font, fill=fontColor)
    return image


if __name__=='__main__':
    myFont = ImageFont.truetype('fonts/Ubuntu-L.ttf', 16)
    myMessage = '\n'.join(["Had I the heavens' embroidered cloths", "Enwrought with golden and silver light,", "The blue and the dim and the dark cloths", "Of night and light and the half light,"])
    myImage = create_image((512, 512), 'white', myMessage, myFont, 'black')
    myImage.save('hello_world.png', "PNG")