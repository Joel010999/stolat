import glob
import shutil
import os

source_dir = r"c:\Users\joelj\.gemini\antigravity\brain\e42ad819-f216-4f22-abbf-fadf463ace27"
dest_dir = r"c:\Users\joelj\Downloads\stolat-main\assets\images"

# Ensure the destination directory exists
os.makedirs(dest_dir, exist_ok=True)

image_names = [
    "gin_paff",
    "lemon_ice_spritz",
    "gomi_ron_blue",
    "cotton_candy_fizz",
    "oreo_irish_frappe",
    "skittles_vodka_punch",
    "lollipop_martini",
    "marshmallow_magic",
    "rainbow_candy_layer",
    "smirnoff_berry_crush"
]

for name in image_names:
    pattern = os.path.join(source_dir, f"{name}_*.png")
    matches = glob.glob(pattern)
    if matches:
        # Take the most recently generated one if there are multiple
        latest_file = max(matches, key=os.path.getctime)
        dest_file = os.path.join(dest_dir, f"{name}.png")
        shutil.copy2(latest_file, dest_file)
        print(f"Copied {latest_file} -> {dest_file}")
    else:
        print(f"Warning: No match found for {name}")

print("Copy complete.")
