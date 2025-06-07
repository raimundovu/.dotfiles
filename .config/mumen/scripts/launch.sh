#!/bin/sh

killall waybar

if [[ $USER = "mumen" ]]; then
  waybar -c ~/repos/.dotfiles/.config/waybar/config & -s ~/repos/.dotfiles/.config/waybar/style.css
else
  waybar &
fi
