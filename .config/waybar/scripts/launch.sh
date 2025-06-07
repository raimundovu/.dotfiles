#!/bin/sh

killall waybar

if [[ $USER = "mumen"]]
then 
  waybar -c 
