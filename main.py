from PIL import Image, ImageDraw

def createwire(*args):
    # If one color is provided, fill the entire image with that color
    if len(args) == 1:
        img = Image.new('RGB', (80, 40))
        draw = ImageDraw.Draw(img)
        draw.rectangle([0, 0, 80, 40], fill=args[0])  # Fill the entire image
        filename = f"wire_{args[0]}.png"  # Filename based on the color
        img.save(filename)
    
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
        img.save(filename)
    
    else:
        print("Invalid input. Please provide one or two colors.")



def create_image(*args):
    # Validate input
    if len(args) == 1:
        img = Image.new('RGB', (20, 20))
        draw = ImageDraw.Draw(img)
        draw.rectangle([0, 0, 20, 20], fill=args[0])  # Draw one block
        filename = f"square_{args[0]}.png"  # Filename based on the color
        img.save(filename)
    
    elif len(args) == 2:
        img = Image.new('RGB', (40, 20))
        draw = ImageDraw.Draw(img)
        
        # Draw the first 20x20 block
        draw.rectangle([0, 0, 20, 20], fill=args[0])
        
        # Draw the second 20x20 block
        draw.rectangle([20, 0, 40, 20], fill=args[1])
        
        # Create the filename based on the two colors
        filename = f"square_{args[0]}_{args[1]}.png"
        img.save(filename)
    
    else:
        print("Invalid input. Please provide one or two colors.")

if __name__ == "__main__":
    # Example usage
    createwire('navy')         # Creates a red.png file
    createwire('red', 'black') # Creates a red_black.png file
    create_image('navy')         # Creates a red.png file
    create_image('red', 'black') # Creates a red_black.png file
