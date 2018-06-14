## How to view the EC2 Instance meta data

To view the EC2 Instance Meta Data visit this url from your EC2 Instance:

http://169.254.169.254/latest/meta-data/



## View the IAM Role Info including the access keys ID , secret access keys and the security token. 
From the linux shell you can type
```console 
curl 169.254.169.254/latest/meta-data/iam/security-credentials/your-role-name/

```
