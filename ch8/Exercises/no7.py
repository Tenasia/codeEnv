

import image

def double(oldImage):

    x = oldImage.get_width()
    y = oldImage.get_height()

    new_img = image.EmptyImage(x * 2, y * 2)

    for row in range(y):
        for col in range(x):
            oldPixel = oldImage.getPixel(col, row)
            
            r = oldPixel.get_red() / 3
            g = oldPixel.get_green() / 3
            b = oldPixel.get_blue() / 3

            new_pixel = image.Pixel(int(r), int(g), int(b))

            new_img.set_pixel(col * 2, row * 2, new_pixel)
            new_img.set_pixel(1 + col * 2, row * 2, new_pixel)
            new_img.set_pixel(col * 2, 1 + row * 2, new_pixel)
            new_img.set_pixel(1 + col * 2, 1 + row * 2, new_pixel)

            
    
    return new_img


def main():
    
    original_image = image.Image('luther.jpg')



    
    
    x = original_image.get_width()
    y = original_image.get_height()

    

    wn = image.ImageWin(x * 2, y * 2)


    bigger_image = double(original_image)
    bigger_image.draw(wn)


    wn.exitonclick()
    help(image)
if __name__ == '__main__':
    main()