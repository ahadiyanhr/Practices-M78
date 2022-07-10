#! /bin/bash

echo $'-----------------------\nWelcome to my Bash-based Downloader Program!\nEnter the URL: '
read url
echo "Please Wait:"
wget -c --show-progress -o log1.txt $url
echo $'------\n'$(head -n 1 log1.txt)$'\n'$(tail -n 2 log1.txt) >> log.txt #Save result into log.txt
rm log1.txt
echo "The result saved in log.txt"
