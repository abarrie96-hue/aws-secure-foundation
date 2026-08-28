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