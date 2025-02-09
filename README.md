# Dotfiles

This repository contains my personal configuration files (dotfiles) for various applications and tools.

## 📌 Requirements
Before using these dotfiles, ensure you have the following installed:

- **Zsh** – A powerful shell
- **Oh My Zsh** – A framework for managing Zsh configuration
- **Picom** – A lightweight compositor for Xorg
- **Qtile** – A tiling window manager
- **Kitty** – A fast, feature-rich terminal emulator
- **pywal** - To get wallpaper dominant colors
- **spicetify**
- **walcord**
- **firefox**
- **pywalfox**


### 🎨 Font Requirement
- **Ubuntu Mono Nerd Font** – Required for proper icon rendering. You can install it from [Nerd Fonts](https://www.nerdfonts.com/) or via package manager:
  ```sh
  sudo pacman -S ttf-ubuntu-mono-nerd
  ```

## 📦 Installation
Clone the repository into your home directory and apply the configurations using GNU Stow:

```sh
git clone https://github.com/Flozz2/dotfiles.git ~/dotfiles
cd ~/dotfiles
stow .
```

### 🔄 Updating Dotfiles
If you make changes to your configurations, you can update them with:

```sh
git add .
git commit -m "Update configs"
git push
```

## ⚙️ Customization
Feel free to modify the dotfiles according to your preferences. You can make changes and apply them again using `stow`.

## 📜 License
These dotfiles are free to use and modify. However, use them at your own risk!

---
⭐ If you like this setup, consider giving the repository a star!


