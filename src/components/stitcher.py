from PIL import Image, ImageDraw, ImageFont


def create_image(size, bgColor, message, font, fontColor):
    W, H = size

    image = Image.new('RGB', size, bgColor)
    draw = ImageDraw.Draw(image)
    _, _, w, h = draw.textbbox((0, 0), message, font=font)
    draw.text(((W-w)/2, (H-h)/2), message, font=font, fill=fontColor)
    return image


def stitch_images_horizontally(image1, image2):
    (width1, height1) = image1.size
    (width2, height2) = image2.size

    result_width = (width1 + width2)
    result_height = max(height1, height2)

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(width1, 0))
    return result


def stitch_comp(file_paths, parsed, font):
    # first, make sure number of prompts matches number of images
    assert len(file_paths) == len(parsed)
    for file_path, parse in zip(file_paths, parsed):
        file_image = Image.open(file_path)
        myFont = ImageFont.truetype(f"fonts/{font}", 16)
        myMessage = '\n'.join(parse)
        text_image = create_image((512, 512), 'white', myMessage, myFont, 'black')
        result = stitch_images_horizontally(file_image, text_image)
        result.save(file_path)
    return file_paths

