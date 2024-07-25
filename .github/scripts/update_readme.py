import random
import re
import requests

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

# Randomly select an image
selected_image = random.choice(images)

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
