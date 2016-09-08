sudo ln -sfi /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -sfi /home/box/web/etc/hello.conf  /etc/gunicorn.d/hello.conf
sudo /etc/init.d/gunicorn restart
