## Execute these commands step by step on your Amazon Linux Instance

```console
sudo su
yum update -y
yum install -y httpd
service httpd start
chkconfig httpd on
echo "hello" > /var/www/html/index.html
```
