#!/bin/bash

# Reading list of websites into an array
readarray websites < websites.txt

# Iterating through all the websites
for website in "${websites[@]}"
do  
    echo $website
    # For capturing packets 
    tcpdump -i wlo1 -w sample.pcap -v -n src $website &

    # Storing PID of the process to kill it later
    TCP_PID=$!

    # Making a request to the website
    wget --tries=1 $website

    # Killing packet capturing process
    kill $TCP_PID

    # Deleting file downloaded by wget
    rm index.html

    # Python script to check if server uses ECN
    python3 packet_analyser.py "$website"

done

# Python script to read survey file and plot graph
python3 ecn_survey.py

# Display graph
eog survey.png







