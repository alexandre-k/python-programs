#!/bin/sh
echo "starting server..."
python3.5 manage.py runsslserver 45.32.13.245:8000 --certificate /etc/ssl/stunnel/stunnel.cert --key /etc/ssl/stunnel/stunnel.key &
echo "...server started"
