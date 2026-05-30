# Warranty Processing Codes

**Classification: INTERNAL USE ONLY**  
**Audience: Support Team, RMA Department**

## Overview

This document contains internal codes used for warranty claim processing, RMA (Return Merchandise Authorization) creation, and inventory management.

## Warranty Status Codes

Use these codes when documenting warranty claims in Zendesk:

### Active Warranty
- **WA-001**: Standard warranty, in coverage period
- **WA-002**: Extended warranty, in coverage period
- **WA-003**: Beta program device (extended coverage)

### Warranty Expired
- **WE-001**: Expired less than 30 days ago (goodwill consideration)
- **WE-002**: Expired more than 30 days ago (no coverage)
- **WE-003**: Expired, but safety recall applies (process anyway)

### Warranty Void
- **WV-001**: Physical damage detected
- **WV-002**: Water damage detected
- **WV-003**: Unauthorized modification/tampering
- **WV-004**: Commercial use of consumer product
- **WV-005**: Missing serial number/label removed

## Failure Type Codes

Document reason for RMA using these codes:

### Hardware Failures
- **HW-101**: Power supply failure
- **HW-102**: WiFi module failure
- **HW-103**: LED indicator malfunction
- **HW-104**: Button/switch failure
- **HW-105**: Camera sensor failure
- **HW-106**: Microphone failure
- **HW-107**: Speaker failure
- **HW-108**: Overheating issue
- **HW-109**: Random reboots/instability
- **HW-110**: Complete device failure (DOA)

### Firmware/Software Issues
- **SW-201**: Firmware update failure
- **SW-202**: Persistent connectivity issues
- **SW-203**: App pairing failure
- **SW-204**: Configuration corruption
- **SW-205**: Performance degradation

### Customer Experience
- **CX-301**: Customer dissatisfaction (functional but unhappy)
- **CX-302**: Changed mind/unwanted gift
- **CX-303**: Compatibility issues
- **CX-304**: Duplicate purchase

## RMA Approval Codes

### Auto-Approve (No Manager Approval Required)
- **AA-001**: Device age <30 days, clear defect
- **AA-002**: Safety-related issue
- **AA-003**: DOA (Dead on Arrival)
- **AA-004**: Systematic known issue (check engineering bulletins)

### Manager Approval Required
- **MA-001**: Out of warranty but goodwill consideration
- **MA-002**: Replacement value >$200
- **MA-003**: Customer requesting upgrade model
- **MA-004**: Third replacement for same customer
- **MA-005**: Warranty status unclear/disputed

### Denied Claims
- **DN-001**: Out of warranty, no goodwill
- **DN-002**: Physical damage (warranty void)
- **DN-003**: Missing proof of purchase
- **DN-004**: Device reported stolen/lost
- **DN-005**: Attempted fraud detected

## Replacement Actions

### Ship Replacement
- **RA-001**: Standard advance replacement (requires CC hold)
- **RA-002**: Standard replacement (after defective received)
- **RA-003**: Upgraded replacement (model discontinued)
- **RA-004**: Refurbished replacement (out of warranty goodwill)

### Refund
- **RF-001**: Full refund to original payment method
- **RF-002**: Store credit issued
- **RF-003**: Partial refund (prorated based on usage)

### Repair
- **RP-001**: Send to repair depot
- **RP-002**: Not repairable, convert to replacement

## Processing Procedures

### Creating RMA in System

1. Log into RMA portal at admin.acmeiot.com/rma
2. Click **Create New RMA**
3. Enter customer email or device serial
4. Select failure type code (HW-XXX, SW-XXX, CX-XXX)
5. Select warranty status code (WA-XXX, WE-XXX, WV-XXX)
6. System auto-determines if approval needed
7. If auto-approve eligible, select replacement action code (RA-XXX)
8. If manager approval needed, select MA-XXX code and assign to manager
9. Add notes and photos if available
10. Submit RMA

### RMA Number Format

RMA numbers are auto-generated:
- Format: `RMA-YYYY-NNNNNN` (e.g., RMA-2024-003847)
- Prefix indicates year
- Sequential six-digit number

### Manager Approval Process

Managers review pending RMAs at: admin.acmeiot.com/rma/pending

Managers use approval codes:
- **APPR**: Approve as requested
- **DENY**: Deny claim (must provide reason)
- **MODY**: Modify replacement (e.g., refurb instead of new)

## Special Situations

### Beta Program Devices
- Always use code **WA-003**
- Extended warranty applies (24 months)
- Notify product team via #beta-issues Slack channel

### Promotional/Free Devices
- Warranty coverage: 90 days
- Use code **WA-001-PROMO**
- Replacement only, no refunds

### Bulk/Commercial Accounts
- Route to enterprise team: enterprise-support@acmeiot.com
- Do not process through standard RMA
- Use code **ESC-COMM**

### Safety Recalls
- Check current recalls: safety.acmeiot.com/recalls
- If device affected, expedite replacement
- Use code **SAFETY-RECALL-[RECALL_ID]**
- No cost to customer regardless of warranty status

## Shipping Codes

### Outbound Shipping
- **SH-STD**: Standard shipping (5-7 business days) - Free
- **SH-EXP**: Expedited (2-3 business days) - $15 customer charge
- **SH-OVN**: Overnight (1 business day) - $35 customer charge
- **SH-INTL**: International shipping - varies by country

### Return Shipping
- **RT-PPD**: Prepaid return label (standard for warranties)
- **RT-CUST**: Customer pays return shipping (out of warranty)

## Quality Tracking

### Return Root Cause Analysis

When defective device received at warehouse, QA assigns:
- **QA-CONF**: Defect confirmed as reported
- **QA-DIFF**: Different issue than reported
- **QA-NFF**: No fault found (device works properly)
- **QA-USER**: User error, not defect

This data feeds back to engineering for quality improvements.

## Metrics & Reporting

Support team measured on:
- RMA processing time (target: <2 hours)
- Approval accuracy (target: <5% manager overrides)
- Correct code usage (target: >95%)

Run reports at: admin.acmeiot.com/rma/reports

## Questions?

- RMA Process: #rma-support Slack channel
- Warranty Policy Questions: warranty-team@acmeiot.com
- Manager Approval: Assign ticket to RMA Manager queue

**Document Owner**: Customer Experience  
**Last Updated**: March 2024  
**Next Review**: June 2024

*INTERNAL USE ONLY - Not for customer distribution*