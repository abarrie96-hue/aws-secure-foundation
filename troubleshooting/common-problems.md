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