Reference:\
https://docs.aws.amazon.com/general/latest/gr/aws_tasks-that-require-root.html

## AWS Tasks That Require AWS Account Root User
The tasks listed below require you to sign in as the AWS account root user. We normally recommend that you use a standard IAM user with appropriate permissions to perform all normal user or administrative tasks. However, you can perform the tasks listed below only when you sign in as the root user of an account.

Modify root user details. This includes changing the root user's password.

Change your AWS support plan.

Change or delete your payment options - an IAM user can perform this after you enable billing access for IAM users. For more information, see Activating Access to the Billing and Cost Management Console.

View your account's billing information - an IAM user can perform this after you enable billing access for IAM users. For more information, see Activating Access to the Billing and Cost Management Console

Close an AWS account.

Sign up for GovCloud.

Submit a Reverse DNS for Amazon EC2 request. The "this form" link on that page to submit a request works only if you sign in with root user credentials.

Create a CloudFront key pair.

Create an AWS-created X.509 signing certificate. (You can still make self-created certificates for IAM users.)

Transfer an Route 53 domain to another AWS account.

Change the Amazon EC2 setting for longer resource IDs. Changing this setting as the root user affects all users and roles in the account. Changing it as an IAM user or IAM role affects only that user or role.

Submit a request to perform penetration testing on your AWS infrastructure using the web form. Alternatively, you can submit your request via email without needing root user access.

Request removal of the port 25 email throttle on your EC2 instance.

Find your AWS account canonical user ID. You can view your canonical user ID from the AWS Management Console only while signed in as the AWS account root user. You can view your canonical user ID as an IAM user with the AWS API or AWS CLI.

Reassigning permissions in a resource-based policy (such as an S3 bucket policy) that were revoked by explicitly denying IAM users access. Root users are not blocked by an explicit deny like IAM users can be.
