# This script sets this machine's local ip address on active conntection

# this command connects and gets the local ip address
# then puts it in a file.
ifconfig | grep "inet " | grep -Fv 127.0.0.1 | awk '{print $2}' > $HOME/.mylocalip.txt
