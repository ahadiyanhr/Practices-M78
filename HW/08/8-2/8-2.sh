#! /bin/bash

echo "This code run by VLC. Please install IT!"


var=$(find . -type f -name "*.mp3" -printf "%f\n" | shuf -n 1)


if [ "$var" ]; then
	echo -e "Rates: 0\nAverage: 0" > "$var.txt"
	echo "VLC is playing $var NOW!"
	cvlc --play-and-exit "$var"
	
	while :; do
		read -p "Enter your RATE (1/10): " rate
		if (($rate >= 1 && $rate <= 10)); then
			echo $rate > "$var.txt"
			break
		else
			read -p "Your Rate is not in Range."
		fi
	done
	
	
else
	echo "There is not any MP3 file in this location!!"
fi
 


# if [ -f $(*.mp3) ]
# then
# 	cvlc $(find . -name '*.mp3' | shuf -n 1)
# else
# 	echo "There is not mp3 file here!"
# fi

