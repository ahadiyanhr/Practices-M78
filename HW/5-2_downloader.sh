#! /bin/bash

echo $'-----------------------\nWelcome to my Bash-based Downloader Program!\nEnter the URL: '
read url
echo "Please Wait:"
wget -c --show-progress -o log1.txt $url
cat log1.txt | grep -w "saved" -m 1 > log.txt
rm log1.txt
echo "The result saved in log.txt"
