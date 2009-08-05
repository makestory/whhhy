cd /var/www/whhhy
python manage.py runfcgi method=threaded  host=127.0.0.1 port=9000 protocol=scgi  daemonize=false
