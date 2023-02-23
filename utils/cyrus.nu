# /etc/nginx/sites-available/default

server {
    listen 80;

    server_name www.cyrus.nu cyrus.nu;
    index index.php index.html;

    root /home/cyrus.nu/cyrus/;

    location / { 
	proxy_pass http://127.0.0.1:8000; }
}
