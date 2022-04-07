#Installing dependencies
sudo apt install pip
sudo pip install psutil
sudo apt install curl

#creating a user
sudo adduser minitel --home /home/minitel
#adding the user to the sudoers
echo "minitel  ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/minitel
#creating a folder & adding the app in it
sudo mkdir /www
sudo cp -r * /www/
#App auto-start when you're connected to the user
echo "sudo python3 /www/CLI.py" | sudo tee -a /home/minitel/.profile