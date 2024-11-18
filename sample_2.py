import os
from PIL import Image, ImageDraw

def createwire(*args):
    # Create the folder if it doesn't exist
    folder_path = "sample_colors_2"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # If one color is provided, fill the entire image with that color
    if len(args) == 1:
        img = Image.new('RGB', (80, 40))
        draw = ImageDraw.Draw(img)
        draw.rectangle([0, 0, 80, 40], fill=args[0])  # Fill the entire image
        filename = f"wire_{args[0]}.png"  # Filename based on the color
        img.save(os.path.join(folder_path, filename))  # Save to the folder
    
    # If two colors are provided, split the image horizontally (top and bottom)
    elif len(args) == 2:
        img = Image.new('RGB', (80, 40))
        draw = ImageDraw.Draw(img)
        
        # Draw the top half with the first color
        draw.rectangle([0, 0, 80, 20], fill=args[0])
        
        # Draw the bottom half with the second color
        draw.rectangle([0, 20, 80, 40], fill=args[1])
        
        # Create the filename based on the two colors
        filename = f"wire_{args[0]}_{args[1]}.png"
        img.save(os.path.join(folder_path, filename))  # Save to the folder
    
    else:
        print("Invalid input. Please provide one or two colors.")


def create_image(*args):
    # Create the folder if it doesn't exist
    folder_path = "color_png"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Validate input
    if len(args) == 1:
        img = Image.new('RGB', (20, 20))
        draw = ImageDraw.Draw(img)
        draw.rectangle([0, 0, 20, 20], fill=args[0])  # Draw one block
        filename = f"square_{args[0]}.png"  # Filename based on the color
        img.save(os.path.join(folder_path, filename))  # Save to the folder
    
    elif len(args) == 2:
        img = Image.new('RGB', (40, 20))
        draw = ImageDraw.Draw(img)
        
        # Draw the first 20x20 block
        draw.rectangle([0, 0, 20, 20], fill=args[0])
        
        # Draw the second 20x20 block
        draw.rectangle([20, 0, 40, 20], fill=args[1])
        
        # Create the filename based on the two colors
        filename = f"square_{args[0]}_{args[1]}.png"
        img.save(os.path.join(folder_path, filename))  # Save to the folder
    
    else:
        print("Invalid input. Please provide one or two colors.")

if __name__ == "__main__":
    # Example usage
    # createwire('navy')         # Creates navy.png inside the color_png folder
    # createwire('red', 'black') # Creates red_black.png inside the color_png folder
    # create_image('navy')       # Creates navy.png inside the color_png folder
    # create_image('red', 'black') # Creates red_black.png inside the color_png folder


    # sample colurs list
    createwire('slateblue')
    createwire('mediumslateblue')
    createwire('darkslateblue')
    createwire('teal')
    createwire('aqua')
    createwire('darkcyan')
    createwire('mediumaquamarine')
    createwire('turquoise')
    createwire('darkturquoise')
    createwire('cadetblue')
    createwire('powderblue')
    createwire('cornflowerblue')
    createwire('mediumspringgreen')
    createwire('springgreen')
    createwire('seagreen')
    createwire('lawngreen')
    createwire('lightseagreen')
    createwire('aquamarine')
    createwire('mintcream')
    createwire('honeydew')
    createwire('beige')
    createwire('ivory')
    createwire('antiquewhite')
    createwire('cornsilk')
    createwire('linen')
    createwire('bisque')
    createwire('peachpuff')
    createwire('oldlace')
    createwire('snow')
    createwire('seashell')
    createwire('ghostwhite')
    createwire('whitesmoke')
    createwire('gainsboro')
    createwire('floralwhite')
    createwire('azure')
    createwire('lavenderblush')
    createwire('aliceblue')
    createwire('rosybrown')
    createwire('lightsteelblue')
    createwire('silver')
    createwire('plum')
    createwire('crimson')
    createwire('orangered')
    createwire('darkorange')
    createwire('palegoldenrod')
    createwire('darkkhaki')
    createwire('goldenrod')
    createwire('navajowhite')
    createwire('tan')
    createwire('darkgoldenrod')
    createwire('sienna')
    createwire('maroon')
    createwire('darkslategray')
    createwire('slategray')
    
    
    createwire('papayawhip')
    createwire('blanchedalmond')
    createwire('darkolivegreen')
    createwire('mediumturquoise')
    createwire('paleturquoise')
    createwire('lightcyan')
    createwire('palevioletred')
    createwire('darkorchid')
    createwire('darkmagenta')
    createwire('fuchsia')
    createwire('lightsalmon')
    createwire('mediumorchid')
    createwire('thistle')
    createwire('mistyrose')
    createwire('slategray')
    createwire('darkslategray')
    createwire('yellow')
    createwire('darksalmon')
    createwire('goldenrod')
    createwire('darkkhaki')
    createwire('rosybrown')
    createwire('palegoldenrod')
    createwire('lemonchiffon')
    createwire('papayawhip')
    createwire('moccasin')
    createwire('navajowhite')
    createwire('peachpuff')
    createwire('coral')
    createwire('lightsteelblue')
    createwire('midnightblue')
    createwire('darkseagreen')
    createwire('gold')
    
    
