from PIL import Image, ImageDraw, ImageFont, ImageOps

def create_png_with_text(output_path, text, font_path=None, font_size=50, image_size=(500, 200), text_color=(0, 0, 0), bg_color=(255, 255, 255), corner_radius=20):
    # Create a blank image with the specified background color
    img = Image.new('RGB', image_size, bg_color)
    
    # Initialize ImageDraw
    draw = ImageDraw.Draw(img)
    
    # Load font if provided, else use default
    font = ImageFont.truetype(font_path, font_size) if font_path else ImageFont.load_default()
    
    # Create rounded corners manually
    mask = Image.new("L", image_size, 0)
    mask_draw = ImageDraw.Draw(mask)
    
    # Draw rounded corners
    width, height = image_size
    mask_draw.rectangle([corner_radius, 0, width - corner_radius, height], fill=255)
    mask_draw.rectangle([0, corner_radius, width, height - corner_radius], fill=255)
    mask_draw.pieslice([0, 0, corner_radius * 2, corner_radius * 2], 180, 270, fill=255)
    mask_draw.pieslice([width - corner_radius * 2, 0, width, corner_radius * 2], 270, 360, fill=255)
    mask_draw.pieslice([0, height - corner_radius * 2, corner_radius * 2, height], 90, 180, fill=255)
    mask_draw.pieslice([width - corner_radius * 2, height - corner_radius * 2, width, height], 0, 90, fill=255)

    # Split text into lines
    lines = text.split('\n')
    line_height = font_size + 5  # Add spacing between lines
    total_text_height = line_height * len(lines)
    
    # Start drawing from the vertical center
    y_offset = (image_size[1] - total_text_height) // 2
    
    for line in lines:
        text_width, _ = draw.textsize(line, font=font)
        x_offset = (image_size[0] - text_width) // 2
        draw.text((x_offset, y_offset), line, fill=text_color, font=font)
        y_offset += line_height

    # Apply the mask to the image
    rounded_img = ImageOps.fit(img, image_size, centering=(0.5, 0.5))
    rounded_img.putalpha(mask)
    
    # Save as PNG
    rounded_img.save(output_path, format="PNG")
    print(f"Image saved at {output_path}")


if __name__ == "__main__":
    # Example inputs (these can be modified as needed)
    inputs = {
        "001": ["Esc", (100, 100), (255, 192, 203), 10, (0, 0, 0), 30, "Size_10.png"],
        "002": ["Esc", (110, 110), (255, 192, 203), 20, (0, 0, 0), 30, "Size_20.png"],
        "003": ["Esc", (120, 120), (255, 192, 203), 30, (0, 0, 0), 30, "Size_30.png"],
        "004": ["Esc", (130, 130), (255, 192, 203), 40, (0, 0, 0), 30, "Size_40.png"],
        "005": ["Esc", (140, 140), (255, 192, 203), 50, (0, 0, 0), 30, "Size_50.png"],
        "006": ["Esc", (150, 150), (255, 192, 203), 60, (0, 0, 0), 30, "Size_60.png"],
        "007": ["Esc", (160, 160), (255, 192, 203), 70, (0, 0, 0), 30, "Size_70.png"],
        "008": ["Esc", (170, 170), (255, 192, 203), 80, (0, 0, 0), 30, "Size_80.png"],
        "009": ["Esc", (180, 180), (255, 192, 203), 90, (0, 0, 0), 30, "Size_90.png"],
        "010": ["Esc", (190, 190), (255, 192, 203), 100, (0, 0, 0), 30, "Size_100.png"],
        "011": ["Esc", (200, 200), (255, 192, 203), 100, (0, 0, 0), 30, "Size_200.png"]
        
    }
    
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Adjust path if needed

    for key, values in inputs.items():
        text, image_size, bg_color, font_size, text_color, corner_radius, output_file = values
        create_png_with_text(output_file, text, font_path, font_size, image_size, text_color, bg_color, corner_radius)

