from PIL import Image

def crop_image(image_path, output_path):
    img = Image.open(image_path)
    img = img.convert("RGBA")
    
    # Get the bounding box of the non-transparent pixels
    bbox = img.getbbox()
    
    if bbox:
        # Crop the image to the bounding box
        img_cropped = img.crop(bbox)
        
        # Save as a square image (favicons are usually square)
        width, height = img_cropped.size
        max_dim = max(width, height)
        
        # Create a new square image with a transparent background
        new_img = Image.new("RGBA", (max_dim, max_dim), (0, 0, 0, 0))
        
        # Paste the cropped image into the center of the new square image
        paste_x = (max_dim - width) // 2
        paste_y = (max_dim - height) // 2
        new_img.paste(img_cropped, (paste_x, paste_y))
        
        # Resize to 32x32 (standard favicon size) to ensure it's optimal
        new_img = new_img.resize((32, 32), Image.LANCZOS)
        
        new_img.save(output_path, "PNG")
        print(f"Successfully cropped and saved to {output_path}")
    else:
        print("Image is entirely transparent.")

if __name__ == "__main__":
    import os
    base_dir = r"c:/Users/joelj/Downloads/stolat-main"
    input_file = os.path.join(base_dir, "logo stolat.png")
    output_file = os.path.join(base_dir, "favicon.png")
    crop_image(input_file, output_file)
