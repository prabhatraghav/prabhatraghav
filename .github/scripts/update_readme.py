import random
import re
import json
import os

# Define two sets of images
images_set1 = [
    {
        "url": "https://raw.githubusercontent.com/prabhatraghav/prabhatraghav/output/desk_worker.gif",
        "width": "300",
        "height": "210"
    },
    {
        "url": "https://raw.githubusercontent.com/prabhatraghav/prabhatraghav/output/coding-guy.gif",
        "width": "290",
        "height": "219"
    },
    {
        "url": "https://raw.githubusercontent.com/prabhatraghav/prabhatraghav/output/profilegif.gif",
        "width": "350",
        "height": "197"
    }
]

images_set2 = [
    {
        "url": "https://raw.githubusercontent.com/prabhatraghav/prabhatraghav/output/banner1-pipeline.gif",
    },
    {
        "url": "https://raw.githubusercontent.com/prabhatraghav/prabhatraghav/output/banner2-pipeline.gif",
    },
    {
        "url": "https://raw.githubusercontent.com/prabhatraghav/prabhatraghav/output/banner-header-0.svg",
    }
]

LAST_IMAGES_FILE = '.last_images.json'

def get_last_images():
    if os.path.exists(LAST_IMAGES_FILE):
        with open(LAST_IMAGES_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_last_images(last_images):
    with open(LAST_IMAGES_FILE, 'w') as f:
        json.dump(last_images, f)

def select_new_image(image_set, set_name, last_images):
    last_image = last_images.get(set_name)
    while True:
        selected_image = random.choice(image_set)
        if selected_image['url'] != last_image:
            break
    last_images[set_name] = selected_image['url']
    return selected_image

# Get the last selected images
last_images = get_last_images()

# Select new images for both sets
selected_image1 = select_new_image(images_set1, 'set1', last_images)
selected_image2 = select_new_image(images_set2, 'set2', last_images)

# Save the newly selected images
save_last_images(last_images)

# Read the current README
with open('README.md', 'r') as file:
    readme = file.read()

# Update the image URLs, widths, and heights in the README
new_readme = re.sub(
    r'<img class="random-image" src="https://raw\.githubusercontent\.com/prabhatraghav/prabhatraghav/output/.*?\.gif" alt="Coding" width="\d+" height="\d+"',
    f'<img class="random-image" src="{selected_image1["url"]}" alt="Coding" width="{selected_image1["width"]}" height="{selected_image1["height"]}"',
    readme
)

new_readme = re.sub(
    r'<img class="random-banner" alt="banner" src="https://raw\.githubusercontent\.com/prabhatraghav/prabhatraghav/output/.*?\.gif"',
    f'<img class="random-banner" alt="banner" src="{selected_image2["url"]}"',
    new_readme
)

# Write the updated README
with open('README.md', 'w') as file:
    file.write(new_readme)

print(f"README updated with images: {selected_image1['url']} and {selected_image2['url']}")
