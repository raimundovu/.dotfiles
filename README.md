# Dotfiles

This is my basic configuration for setting up my configuration.

##  Commands for MACOS (🤮).

```bash
    brew install lazygit
    brew install --cask alacritty
    brew install powerlevel10k
    brew install bat
```


## Useful commands.

For configuring powerlevel10k:

```bash 
    echo "source $(brew --prefix)/share/powerlevel10k/powerlevel10k.zsh-theme" >> ~/.zshrc
```

For copying files from this repo to the `~/.config/` folder, I am currently using

```bash 
cp -rf ~/.dotfiles/.config/path-to-program  ~/.config/
```

## TODO

- [ ] Check about stow for dotfiles managing.
- [ ] KEEP RICING ARCH LINUX
