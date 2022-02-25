# goes in /etc/systemd/system/<project name>.service
# then 'sudo systemctl daemon-reload', 'sudo systemctl start <service>.service', 'sudo systemctl enable <service>.service'
# don't forget to add proxy routing in nginx.conf
# and that .py file has a:
# if __name__ == '__main__':
#   uvicorn.run(app, host = '127.0.0.1', port = 50XY)
[Unit]
Description=serves vuebill with FastAPI

[Service]
User=alexhalme
Group=www-data
WorkingDirectory=/home/alexhalme/python/ahomepage
#EnvironmentFile=/etc/environment
#ExecStart=python3 vuebill_fastapi.py
ExecStart=python3 /home/alexhalme/.local/bin/uvicorn hp:app --proxy-headers --port 5145 --workers 5

[Install]
WantedBy=multi-user.target

