#!/bin/bash

# Check if directory is provided as argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 /path/to/wallpaper/directory"
    exit 1
fi

# Check if directory exists
if [ ! -d "$1" ]; then
    echo "Error: Directory '$1' does not exist"
    exit 1
fi

# Check if feh is installed
if ! command -v feh &> /dev/null; then
    echo "Error: feh is not installed. Please install it first."
    exit 1
fi

# Array of valid image extensions
valid_extensions=("jpg" "jpeg" "png" "gif" "bmp")

# Create array of image files
images=()
for ext in "${valid_extensions[@]}"; do
    while IFS= read -r -d $'\0' file; do
        images+=("$file")
    done < <(find "$1" -type f -iname "*.$ext" -print0)
done

# Check if any images were found
if [ ${#images[@]} -eq 0 ]; then
    echo "Error: No valid image files found in directory"
    exit 1
fi

# Select random image
random_image=${images[$RANDOM % ${#images[@]}]}

# Set wallpaper using feh
feh --bg-fill "$random_image"

# Print selected image path
echo "Set wallpaper to: $random_image"