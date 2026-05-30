# WiFi Setup Guide

## Initial Device Setup

This guide covers connecting your AcmeIoT device to your home WiFi network for the first time.

## Before You Begin

### Requirements
- AcmeIoT Home app installed (iOS 13+ or Android 9+)
- Active AcmeIoT account
- 2.4GHz or 5GHz WiFi network
- WiFi password
- Smartphone or tablet

### Supported WiFi Standards
- 802.11 b/g/n/ac (2.4GHz)
- 802.11 a/n/ac (5GHz)
- WPA2 or WPA3 security

**Note**: SmartPlug models only support 2.4GHz networks

## Step-by-Step Setup

### 1. Prepare Your Device

**SmartRouter**
- Connect power cable and modem cable
- Wait for LED to flash blue (setup mode)

**SmartPlug**
- Plug into wall outlet
- Press and hold button for 5 seconds until LED flashes green

**SmartCam**
- Connect power cable
- Wait for LED to flash blue
- If LED doesn't flash, press reset button for 3 seconds

### 2. Open AcmeIoT Home App

1. Launch the AcmeIoT Home app
2. Log into your account (or create one)
3. Tap the **+** icon to add a new device
4. Select your device type from the list

### 3. Connect to Device

The app will guide you through one of two connection methods:

#### Method A: Bluetooth Pairing (Newer Devices)
1. Enable Bluetooth on your phone
2. App automatically detects nearby devices
3. Select your device from the list
4. Tap **Connect**

#### Method B: WiFi Direct (Older Devices)
1. App will prompt you to connect to device's WiFi
2. Go to phone's WiFi settings
3. Connect to network named "AcmeIoT-XXXX"
4. Return to AcmeIoT app

### 4. Select Your WiFi Network

1. App displays available networks
2. Select your home WiFi network
3. Enter your WiFi password
4. Tap **Connect**

**Troubleshooting**: If your network doesn't appear, ensure:
- Router is powered on
- You're within range
- Network is broadcasting (not hidden)
- Using correct frequency band (2.4GHz for SmartPlugs)

### 5. Complete Setup

1. Device will connect to WiFi (30-60 seconds)
2. LED will turn solid blue/green when connected
3. App will confirm successful connection
4. Name your device
5. Select room location
6. Tap **Finish**

## Changing WiFi Network

If you get a new router or change your WiFi password:

1. Open AcmeIoT Home app
2. Select the device
3. Go to **Settings** > **WiFi Settings**
4. Tap **Change Network**
5. Follow steps 3-5 above

## Advanced WiFi Settings

### Static IP Assignment
1. Device **Settings** > **Network**
2. Toggle **Static IP** ON
3. Enter IP address, subnet mask, gateway
4. Tap **Save**

### WiFi Band Preference (Dual-band devices)
1. Device **Settings** > **WiFi Settings**
2. Select **Band Preference**
3. Choose: Auto / 2.4GHz Only / 5GHz Only
4. Tap **Apply**

## Common Setup Issues

### Device Not Found
- Ensure device is in setup mode (flashing LED)
- Restart device and try again
- Move phone closer to device
- Disable VPN on phone

### Wrong Password Error
- Verify WiFi password (case-sensitive)
- Check for special characters
- Confirm network security type

### Connection Timeout
- Check internet connection
- Restart router
- Ensure router isn't blocking new devices
- Verify router firmware is up to date

### Device Offline After Setup
- Verify WiFi signal strength
- Check router is online
- Restart device
- Ensure router's DHCP is enabled

## Network Requirements

### Router Compatibility
- UPnP enabled (recommended)
- Ports 80, 443 open for cloud connection
- mDNS/Bonjour enabled for local discovery

### Firewall Settings
AcmeIoT devices require outbound access to:
- *.acmeiot.com
- *.acmeiot-cloud.net

## Need More Help?

- Video setup guides: support.acmeiot.com/setup-videos
- Live chat support: Available 24/7 in app
- Phone: 1-800-ACME-IOT
- Email: setup-help@acmeiot.com

*Document Version 2.4 | Last Updated: March 2024*