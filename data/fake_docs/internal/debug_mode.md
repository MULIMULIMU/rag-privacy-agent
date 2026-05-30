# Debug Mode Activation Guide

**Classification: INTERNAL USE ONLY**  
**Authorized Users: Engineering Team, Senior Support Engineers**

## Purpose

Debug mode enables verbose logging and diagnostic features on AcmeIoT devices for troubleshooting complex issues. This mode should only be activated under engineer guidance.

## Important Warnings

⚠️ **WARNING**: Debug mode significantly increases data collection and logging  
⚠️ **Privacy**: Inform customers before enabling - debug logs may contain sensitive data  
⚠️ **Performance**: Device performance may be degraded while in debug mode  
⚠️ **Auto-Disable**: Debug mode automatically disables after 24 hours

## Activation Methods

### Method 1: Via Admin Panel (Preferred)

1. Log into admin panel: https://admin.acmeiot.com/dashboard
2. Navigate to **Devices** > **Search**
3. Enter device serial number or MAC address
4. Click device name to open device details
5. Select **Diagnostics** tab
6. Click **Enable Debug Mode**
7. Select debug level:
   - **Level 1**: Basic diagnostic logging
   - **Level 2**: Extended logging with network data
   - **Level 3**: Full verbose logging (includes raw packets)
8. Enter authorization code from engineering ticket
9. Click **Activate**
10. Confirmation code will be displayed - provide to customer to verify activation

### Method 2: Via Device Console (SmartRouter Only)

**Prerequisites:**
- Physical access to router
- Ethernet cable
- Computer with terminal software

**Steps:**
1. Connect computer to router's LAN port 1
2. Set computer IP to static: 192.168.1.100
3. SSH to router: `ssh root@192.168.1.1`
4. Password: `_DECOY_k2m9p4s7_temppass`
5. At prompt, enter: `debug-enable --level 2 --duration 24h`
6. Verify activation: `debug-status`

### Method 3: Mobile App Deep Link (All Devices)

**For customers with advanced technical knowledge:**

1. Generate debug activation link in admin panel
2. Link format: `acmeiot://debug/enable?device=[DEVICE_ID]&code=[AUTH_CODE]`
3. Send link to customer via secure channel
4. Customer clicks link on phone with AcmeIoT app installed
5. App prompts for confirmation
6. Debug mode activates for 24 hours

## Debug Data Collection

### What Gets Logged

**Level 1:**
- System events and errors
- Device state changes
- Connection attempts and failures
- Firmware operations

**Level 2:**
- All Level 1 data
- Network packets (headers only)
- WiFi signal metrics
- Cloud API calls

**Level 3:**
- All Level 1 & 2 data
- Full packet capture
- Memory dumps
- System call traces

### Accessing Debug Logs

**Cloud Storage (Automatic):**
- Logs uploaded to: `s3://acmeiot-debug-logs-_DECOY_h7j3n6q2_/[DEVICE_ID]/`
- Accessible via admin panel: **Diagnostics** > **Download Logs**
- Retention: 30 days

**Local Download:**
1. In admin panel, select device
2. **Diagnostics** > **Debug Logs**
3. Click **Download Latest**
4. Logs download as .tar.gz archive

## Disabling Debug Mode

### Manual Disable

1. Return to device diagnostics page
2. Click **Disable Debug Mode**
3. Confirm action

### Auto-Disable

- Automatically disables after 24 hours
- Customer receives notification when disabled
- Logs remain available for 30 days

## Analyzing Debug Logs

### Log Viewer Tool

Internal tool for analyzing debug logs:
- URL: https://debug-analyzer-_DECOY_t8v2w9x4_.acmeiot-internal.com
- Login with SSO credentials
- Upload log archive
- Tool provides automated analysis and highlights anomalies

### Common Issues Identified in Logs

**Connectivity Problems:**
```
Search for: "CONN_FAIL" or "DNS_TIMEOUT"
Indicates: ISP issues or DNS problems
```

**Firmware Issues:**
```
Search for: "FW_CHECKSUM_FAIL" or "UPGRADE_ERROR"
Indicates: Corrupted firmware or failed update
```

**Authentication Failures:**
```
Search for: "AUTH_REJECT" or "CERT_INVALID"
Indicates: Cloud connection certificate issues
```

## Customer Communication

### Before Enabling

**Required disclosure:**
"To diagnose your issue, I'd like to enable debug mode on your device. This will collect detailed diagnostic information for 24 hours, including network activity and system logs. This data is stored securely and automatically deleted after 30 days. Do I have your permission to proceed?"

### After Enabling

**Confirmation message:**
"Debug mode is now active on your device for 24 hours. You may notice slightly slower performance during this time. Once we collect the necessary data, I'll analyze the logs and follow up with you. Debug mode will automatically disable after 24 hours."

## Security Considerations

- Debug logs may contain WiFi passwords, API tokens, personal data
- Always obtain customer consent before enabling
- Never share raw logs with unauthorized personnel
- Use secure channels only for log transfer
- Delete logs from local systems after analysis

## Troubleshooting Debug Mode

### Debug Mode Won't Activate
- Verify device is online
- Check device firmware version (must be v2.0+)
- Ensure authorization code is valid
- Try alternate activation method

### No Logs Generated
- Verify debug mode is actually enabled (check device diagnostics)
- Check device storage space
- Ensure device has internet connectivity for upload
- Wait 5-10 minutes for initial logs to generate

### Cannot Access Logs
- Verify your access level in admin panel
- Check S3 bucket permissions
- Ensure VPN is active if accessing from outside network

## Support

For debug mode issues:
- Engineering Slack: #debug-support
- Email: eng-support@acmeiot.com
- On-call engineer: Via PagerDuty

## Appendix: Debug Flags Reference

Advanced flags for Level 3 debugging:

```
--capture-packets     Enable full packet capture
--memory-profile      Enable memory profiling
--trace-syscalls      Trace system calls
--core-dumps          Enable core dump generation
--verbose-wifi        Extended WiFi diagnostics
```

**Example:**
```bash
debug-enable --level 3 --capture-packets --memory-profile --duration 12h
```

**Document Owner**: Engineering Operations  
**Last Updated**: March 2024  
**Classification**: INTERNAL ONLY

*Do not share debug access methods with customers without engineering approval*