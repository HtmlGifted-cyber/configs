#!/bin/bash
## This shell script creates a virtual host on apache2 webserver 
## setup on ubuntu 18.04

## This is the beginning of the script.
#Asks for mane for the new vhost
echo 'Please enter the name of your new vhost EXAMPLE: mysite.com.'

#reads users input and sets a variable
read varhost

##Step 1 — Create the Directory Structure
    sudo mkdir -p /var/www/html/$varhost
    sudo mkdir -p /var/www/html/$varhost/public_html

##Step 2 — Grant Permissions
    sudo chown -R $USER:$USER /var/www/html/$varhost/public_html

##Step 3 — Create Demo Pages for Each Virtual Host
    sudo mkdir /var/www/html/$varhost/public_html/index.html && echo "<html>
  <head>
    <title>Welcome to $varhost!</title>
  </head>
  <body>
    <h1>Success! The $varhost virtual host is working!</h1>
  </body>
</html>" > /var/www/html/$varhost/public_html/index.html

##Step 4 — Create New Virtual Host Files

##Create the First Virtual Host File
    sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/$varhost.conf && echo "<VirtualHost *:43>
    ServerAdmin admin@$varhost
    ServerName $varhost
    ServerAlias www.$varhost
    DocumentRoot /var/www/$varhost/public_html
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>"

##gets the servers network ip address and sets as variable
localip=$(ifconfig | grep "inet " | grep -Fv 127.0.0.1 | awk '{print $2}')

##Step 5 — Enable the New Virtual Host configuration File
    sudo a2ensite $varhost.conf

##Step 6 — Set Up Local Hosts File
    echo > "127.0.0.1   localhost
127.0.1.1   guest-desktop
$LOCALIP $varhost

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters"

##restart apache2 to make changes active
    sudo systemctl restart apache2

##Step 7 — Test your Results
  echo " $USER Your new virtualhost has been setup."
  echo  "http://$varhost"
