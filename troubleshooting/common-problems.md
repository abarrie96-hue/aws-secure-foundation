## Nginx Running but Website Unreachable

### Symptoms

- Nginx service was active.
- Port 80 was listening locally.
- Public IP timed out in the browser.

### Root Cause

The EC2 Security Group did not allow inbound HTTP traffic on TCP port 80.

### Resolution

Added an inbound HTTP rule for TCP port 80 from `0.0.0.0/0`.

### Verification

Confirmed `HTTP/1.1 200 OK` locally and through the EC2 public IP.

## AWS CLI Package Not Available on Ubuntu

### Symptom

Attempting to install AWS CLI with:

sudo apt install -y awscli

returned:

Package 'awscli' has no installation candidate

### Investigation

The awscli package was not available from the configured Ubuntu package repositories.

### Resolution

Installed AWS CLI v2 using the official AWS installer.

Verified installation with:

aws --version

### Lesson Learned

A package installation failure does not necessarily mean the command syntax is incorrect. Check package availability and use the vendor-supported installation method when appropriate.

## AWS VPC Connectivity Troubleshooting

When an EC2 instance cannot be reached, troubleshoot the network layer by layer instead of randomly changing settings.

### Troubleshooting Order

1. Verify the application is running.
2. Verify the application is listening on the expected port.
3. Verify the EC2 instance IP configuration.
4. Check the Security Group.
5. Check the Network ACL.
6. Check the subnet route table.
7. Check the Internet Gateway or NAT Gateway.
8. Check DNS/client connectivity.

### Useful Commands

Test the application locally:

curl http://localhost

Check listening ports:

sudo ss -tulpn

Check network interfaces:

ip addr

Test external connectivity:

curl -I https://aws.amazon.com

### Key Lesson

If an application works locally but cannot be reached externally, investigate the networking path instead of immediately assuming the application is broken.