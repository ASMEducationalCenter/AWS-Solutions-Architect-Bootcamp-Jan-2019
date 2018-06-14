## Some of the services on AWS doesnt cost you money , while some cost a lot of money.

## Things that cost a lot a lot of money
- NAT Gateway costs you like $35/month and there's no free tier
- PIOPS EBS (I01)
- Elastip IP(EIP)



## Things that doesn't cost money to have
- VPC 
- Subnets
- Security Groups
- NACL
- Internet gateway
- Autoscaling is a service that you dont pay anything for. But you pay for the EC2 it creates
- cloudformation is a service that you dont pay anything for. But you pay for the EC2 it creates


## Things covered under free tier but cost you money if you run out of free tier limit

EC2 - you get 750 hours/month for free for a year after you sign up
Elastic load balancer -  you get 750 hours/month for free for a year after you sign up



## Things to remember regarding cost

- EC2 and EBS are chargerd seperately. So when your EC2 is in a stoped state, you're still paying for EBS volumes
- S3: you get about 5 GB of storage per month. But you pay for storage and also for data transfer. So don't share your download links with many people
