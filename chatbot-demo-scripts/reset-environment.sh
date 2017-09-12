#!/bin/bash
# assume we want demo scripts in home directory
# TODO: remove the hard-coding of the home directory
# and read as an option from the command line
cd
rm -rf /home/ubuntu/chatbot-test
mkdir /home/ubuntu/chatbot-test
cd /home/ubuntu/chatbot-test

# get the latest chatbot source
wget https://raw.githubusercontent.com/jhancock1975/tensorflow-chatbot-tutorial/master/src/chatbot-tutorial-code-part-1.py
