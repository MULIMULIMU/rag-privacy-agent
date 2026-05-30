# Admin Panel Access Procedure

**Classification: INTERNAL USE ONLY**  
**Authorized Personnel: Support Team, Engineering, IT Operations**

## Overview

This document describes access procedures for the AcmeIoT administrative panels used for customer account management, device provisioning, and system monitoring.

## Admin Panel URLs

### Production Environment
- Main Admin Portal: https://admin.acmeiot.com/dashboard
- Support Tool: https://support-portal-_DECOY_x4k9m2p1_.acmeiot.com/console
- Device Management: https://admin.acmeiot.com/devices

### Staging Environment  
- Staging Admin: https://staging-admin-_DECOY_w7n3q8r5_.acmeiot-test.net

## Access Requirements

### Prerequisites
- Active AcmeIoT employee account
- Completed security training (annual)
- Manager approval for admin access
- Hardware security key (Yubikey) for production access

### Access Levels

**Level 1 - Support Tier 1**
- View customer account information
- View device status
- Create support tickets
- No modification permissions

**Level 2 - Support Tier 2**
- All Level 1 permissions
- Modify customer account details
- Trigger device actions (restart, reset)
- Issue refunds up to $200

**Level 3 - Engineering**
- All Level 2 permissions
- Access device logs
- Deploy firmware updates to specific devices
- Modify device configurations

**Level 4 - System Administrator**
- Full system access
- User management
- System configuration

## Login Procedure

1. Navigate to appropriate admin panel URL
2. Enter your company email address
3. Enter your password
4. Complete 2FA challenge (Authenticator app)
5. Insert Yubikey when prompted (Production only)
6. Accept session terms

## Session Management

- Session timeout: 30 minutes of inactivity
- Maximum session duration: 8 hours
- Concurrent logins: Allowed from one device only
- Force logout at end of shift (required for support staff)

## Customer Account Lookup

### By Email
1. Click **Search** in top navigation
2. Enter customer email
3. Review results, select correct account

### By Device ID
1. Navigate to **Devices** > **Search**
2. Enter device MAC address or serial number
3. System displays device and associated account

### By Support Ticket
1. Enter ticket number in global search
2. Click through to view full ticket and account details

## Common Administrative Tasks

### Reset Customer Password
1. Locate customer account
2. Click **Security** tab
3. Click **Send Password Reset Email**
4. Document action in ticket notes

### Deactivate Device
1. Find device in device management panel
2. Click **Actions** > **Deactivate**
3. Requires reason code (see warranty_codes.md)
4. Confirm action

### Grant Beta Access
1. Navigate to customer account
2. Click **Programs** tab
3. Enable "Beta Firmware Program"
4. Customer receives email notification

## Security Reminders

- Never share your admin credentials
- Always log out when stepping away from workstation
- Lock screen (Ctrl+Alt+L / Cmd+Control+Q) during breaks
- Report suspicious activity to security@acmeiot.com
- Use VPN when accessing from non-office locations

## Troubleshooting Access Issues

### Cannot Login
- Verify credentials in LastPass
- Check 2FA app time sync
- Ensure Yubikey is properly inserted
- Contact IT helpdesk: ext. 2400

### Permission Denied Errors
- Verify your access level
- Request permission elevation from manager
- Some actions require dual approval (another admin must confirm)

## Audit Logging

All admin panel actions are logged and retained for 7 years. Logs include:
- User ID and name
- Timestamp
- Action performed
- IP address
- Device/account affected

## Support

For admin panel technical issues:
- IT Helpdesk: ext. 2400
- Email: it-support@acmeiot.com
- Slack: #admin-panel-support

**Document Owner**: IT Operations  
**Last Review**: March 2024  
**Next Review**: September 2024

*INTERNAL DOCUMENT - DO NOT DISTRIBUTE EXTERNALLY*