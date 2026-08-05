# Security Review - Day 1

## Completed

- Root account protected with MFA
- IAM administrator user created
- MFA enabled for administrator
- Billing alerts configured
- CloudTrail enabled (update after completion)
- AWS CLI configured

## Risks Remaining

- AdministratorAccess policy still assigned
- GuardDuty not enabled
- Security Hub not enabled
- AWS Config not enabled

## Planned Improvements

- Replace AdministratorAccess with least privilege
- Enable GuardDuty
- Enable Security Hub
- Enable AWS Config

## Lessons Learned

- Root account should only be used for account-level tasks.
- IAM users should be protected with MFA.
- Billing access must be enabled by the root account before IAM administrators can access Billing.
