#! /bin/bash

set -e  # Exit on error

# Define required packages
packages=("zsh" "picom" "qtile" "kitty" "stow" "ttf-ubuntu-mono-nerd")

echo "Checking for required packages..."
for package in "${packages[@]}"; do
    if ! pacman -Qi "$package" &>/dev/null; then
        echo "Installing $package..."
        sudo pacman -S --noconfirm "$package"
    else
        echo "$package is already installed."
    fi
done

# Install Oh My Zsh if not installed
if [ ! -d "$HOME/.oh-my-zsh" ]; then
    echo "Installing Oh My Zsh..."
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
else
    echo "Oh My Zsh is already installed."
fi

# Clone dotfiles if not already present
if [ ! -d "$HOME/.dotfiles" ]; then
    echo "Cloning dotfiles..."
    git clone https://github.com/Flozz2/dotfiles.git "$HOME/.dotfiles"
fi

# Apply dotfiles using stow
echo "Applying dotfiles..."
cd "$HOME/.dotfiles"
stow .

# Change default shell to Zsh
if [[ "$SHELL" != *"zsh" ]]; then
    echo "Changing default shell to Zsh..."
    chsh -s "$(which zsh)"
fi

echo "Installation complete! Log out and log back in to apply changes."

