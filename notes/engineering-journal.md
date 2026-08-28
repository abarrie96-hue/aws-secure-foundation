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

# Engineering Journal

## Date
2026-08-06

## Ticket
Ticket #002 - Linux Administration, Permissions & Automation

---

## Objective

Continue learning Linux administration on an AWS EC2 Ubuntu instance and begin automating common server administration tasks.

---

## Topics Learned

### Linux Permissions

Learned how Linux permissions are represented using:

- Read (r)
- Write (w)
- Execute (x)

Learned numeric permissions:

- 400
- 644
- 755

Understood why SSH private keys require:

chmod 400

Only the owner should have read access to the private key.

---

### File Ownership

Learned:

- Owner
- Group
- Others

Commands learned:

ls -l
chown
chgrp
id
whoami

Key takeaway:

Ownership determines who controls the file while permissions determine what actions users can perform.

---

### Bash Automation

Created my first Bash script:

server-health.sh

The script checks:

- Hostname
- Current user
- Operating system
- Kernel version
- Disk usage
- Memory
- CPU
- Nginx status
- Uptime

Learned how to make a script executable:

chmod 755 server-health.sh

---

### EC2 User Data

Learned that EC2 User Data is a Bash script executed automatically during the first boot of an instance.

Benefits:

- Consistent server configuration
- Automation
- Faster deployments
- Reduced manual work

Important log:

/var/log/cloud-init-output.log

---

### IAM Roles

Learned that EC2 instances should use IAM Roles instead of storing AWS Access Keys.

Benefits:

- Temporary credentials
- Automatic credential rotation
- Better security
- Principle of Least Privilege

---

## Troubleshooting Performed

Issue:

Unable to install nginx.

Root Cause:

Package name was typed incorrectly as:

ngnix

Resolution:

Corrected package name to:

nginx

---

Issue:

Website unreachable.

Root Cause:

HTTP port 80 was not allowed in the Security Group.

Resolution:

Added inbound HTTP rule.

---

Issue:

Permission denied when executing script.

Root Cause:

Script was not executable.

Resolution:

chmod 755 server-health.sh

---

## Commands Practiced

apt update
apt upgrade
systemctl
journalctl
chmod
chown
chgrp
ls -l
whoami
id
hostname
df -h
free -h
uptime
curl
ss
tail
cat

---

## Biggest Lessons Today

Automation reduces repetitive work.

Permissions and ownership are different concepts.

Always troubleshoot by gathering evidence before making changes.

Linux security and AWS IAM are separate security layers.

Least Privilege should always be followed.

---

## Interview Questions Reviewed

Why use chmod 400 for SSH keys?

Difference between apt update and apt upgrade.

Why are logs stored in /var/log?

Why use IAM Roles instead of Access Keys?

Why is User Data better than manual configuration?

---

## Tomorrow's Goals

Finish Ticket #002.

Learn IAM Roles for EC2 in more detail.

Complete Ticket #002 documentation.

## IAM Roles for EC2

### What I Learned

EC2 instances can access AWS services securely by using IAM roles instead of storing long-term AWS access keys on the server.

I created:

- IAM Role: acme-ec2-s3-readonly-role
- Trusted Service: EC2
- Permission: AmazonS3ReadOnlyAccess

### Verification

I verified the identity being used by the EC2 instance with:

aws sts get-caller-identity

The EC2 instance successfully assumed the IAM role.

I tested an allowed operation:

aws s3 ls

I also tested an operation outside the role's permissions:

aws iam list-users

The IAM operation returned AccessDenied, which confirmed that least privilege was working correctly.

### Security Takeaway

IAM roles are safer than storing access keys on EC2 instances because AWS provides and rotates temporary credentials automatically.

The EC2 instance should only receive the permissions required for its workload.

In production, I would further restrict the policy to only the specific S3 bucket and actions required.

## Ticket #002 Closeout

Status: COMPLETE

### Deliverables

- Ubuntu EC2 instance deployed
- SSH access configured
- Linux system updated
- Nginx installed and configured
- HTTP connectivity verified
- Linux permissions practiced
- Linux ownership practiced
- Bash health-check script created
- EC2 User Data studied
- AWS CLI v2 installed
- EC2 IAM role configured
- S3 read-only permissions tested
- Least privilege verified
- Troubleshooting documented
- Work committed to Git

### Final Result

Ticket #002 successfully established foundational skills in EC2, Linux administration, AWS security, troubleshooting, and automation.

Begin Project #2 - AWS Networking.