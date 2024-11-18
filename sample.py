import os
from PIL import Image, ImageDraw

def createwire(*args):
    # Create the folder if it doesn't exist
    folder_path = "sample_colors"
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
    createwire('black')
    createwire('white')
    createwire('red')
    createwire('green')
    createwire('blue')
    createwire('yellow')
    createwire('cyan')
    createwire('magenta')
    createwire('gray')
    createwire('brown')
    
    # Shades of Blue
    createwire('lightblue')
    createwire('dodgerblue')
    createwire('skyblue')
    createwire('navy')
    createwire('royalblue')
    createwire('mediumblue')
    createwire('steelblue')
    createwire('deepskyblue')
    
    # Shades of Green
    createwire('lime')
    createwire('forestgreen')
    createwire('darkgreen')
    createwire('lightgreen')
    createwire('olive')
    createwire('palegreen')
    createwire('chartreuse')
    createwire('mediumseagreen')
    
    # Shades of Red
    createwire('darkred')
    createwire('firebrick')
    createwire('indianred')
    createwire('lightcoral')
    createwire('salmon')
    createwire('tomato')
    
    # Shades of Purple
    createwire('purple')
    createwire('violet')
    createwire('orchid')
    createwire('indigo')
    createwire('blueviolet')
    createwire('mediumpurple')
    createwire('lavender')
    
    # Shades of Yellow
    createwire('gold')
    createwire('orange')
    createwire('yellowgreen')
    createwire('khaki')
    createwire('lightyellow')
    createwire('lightgoldenrodyellow')
    
    # Shades of Pink
    createwire('pink')
    createwire('lightpink')
    createwire('hotpink')
    createwire('deeppink')
    createwire('mediumvioletred')
    
    # Shades of Brown
    createwire('chocolate')
    createwire('saddlebrown')
    createwire('sandybrown')
    createwire('wheat')
    createwire('peru')
    createwire('burlywood')
    
    # Shades of Grey
    createwire('darkgray')
    createwire('gray')
    createwire('lightgray')
    createwire('dimgray')

