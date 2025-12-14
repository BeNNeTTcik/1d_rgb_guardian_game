sudo apt update
sudo apt install -y python3-venv python3-pip git

mkdir -p ~/guardian
cd ~/guardian
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip

sudo sed -i '$a dtparam=spi=on' /boot/firmware/config.txt

source ~/guardian/.venv/bin/activate
pip install rpi-ws281x