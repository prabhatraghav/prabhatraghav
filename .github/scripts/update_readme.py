import random
import re
import requests
import os

# Images list (as defined above)
images = [
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

# Function to get the last selected image
def get_last_image():
    if os.path.exists('.last_image'):
        with open('.last_image', 'r') as f:
            return f.read().strip()
    return None

# Function to save the selected image
def save_selected_image(image_url):
    with open('.last_image', 'w') as f:
        f.write(image_url)

# Get the last selected image
last_image = get_last_image()

# Select a new image that's different from the last one
while True:
    selected_image = random.choice(images)
    if selected_image['url'] != last_image:
        break

# Save the newly selected image
save_selected_image(selected_image['url'])

# Read the current README
with open('README.md', 'r') as file:
    readme = file.read()

# Update the image URL, width, and height in the README
new_readme = re.sub(
    r'<img class="random-image" src="https://raw\.githubusercontent\.com/prabhatraghav/prabhatraghav/output/.*?\.gif" alt="Coding" width="\d+" height="\d+"',
    f'<img class="random-image" src="{selected_image["url"]}" alt="Coding" width="{selected_image["width"]}" height="{selected_image["height"]}"',
    readme
)

# Write the updated README
with open('README.md', 'w') as file:
    file.write(new_readme)

print(f"README updated with image: {selected_image['url']}")
