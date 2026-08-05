# Engineering Journal

## Day 1

### Issue #001

**Problem**

Received the following error while trying to access Billing as the `cloud-admin` IAM user:

```
You don't have the billing:GetIAMAccessPreference permission...
```

**Root Cause**

IAM access to Billing had not been enabled by the root account.

**Resolution**

Logged in as the root user, enabled IAM User and Role Access to Billing Information, then signed back in as the IAM administrator.

**Lesson Learned**

AdministratorAccess does not automatically grant access to billing until the root account enables IAM billing access.

## Issue #002

### Topic

AWS CLI Configuration

### Commands Used

aws configure

aws sts get-caller-identity

aws iam list-users

aws ec2 describe-regions

### Lesson Learned

(Write your own summary here.)

### Interview Note

The `aws sts get-caller-identity` command is useful for confirming which AWS account and IAM identity you're currently using before making changes.


## Issue #003

### Topic

CloudTrail Configuration

### What I Learned

CloudTrail records AWS API activity, including which IAM identity performed an action, when it occurred, the source IP address, and the AWS Region. It is essential for auditing, troubleshooting, and security investigations.

### Verification

- Created a multi-region trail.
- Enabled management events.
- Enabled log file validation.
- Verified events appeared in Event History after running AWS CLI commands.