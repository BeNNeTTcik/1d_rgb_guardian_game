sudo nano /etc/systemd/system/guardian.service
sudo /etc/systemd/system/guardian.service << EOF
[Unit]
Description=Guardian LED Game
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/guardian
ExecStart=/home/pi/guardian/.venv/bin/python /home/pi/guardian/main.py
Restart=on-failure
RestartSec=2

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable guardian.service
sudo systemctl start guardian.service

# Log check
journalctl -u guardian.service -f 
