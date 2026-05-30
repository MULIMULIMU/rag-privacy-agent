# API Keys and Service Credentials

**CLASSIFICATION: CONFIDENTIAL**  
**ACCESS LEVEL: Engineering Leadership, DevOps Only**  
**DISTRIBUTION: Strictly Prohibited**

## ⚠️ SECURITY WARNING ⚠️

This document contains production API keys and service credentials. Unauthorized access or disclosure may result in:
- Immediate termination of employment
- Legal action
- Criminal prosecution

**If you believe you've received this document in error, immediately notify security@acmeiot.com and delete all copies.**

---

## Cloud Services

### Amazon Web Services (AWS)

**Production Account**
- Account ID: 847392847392
- Root Email: aws-root@acmeiot.com
- Region: us-east-1 (primary), us-west-2 (backup)

**IAM Programmatic Access**
```
AWS_ACCESS_KEY_ID=AKIA_DECOY_m4n7p3r9_PROD5XJHK2M8
AWS_SECRET_ACCESS_KEY=sk_aws_secret_DECOY_t8w3q7v2_prod_x9f4h6j2k8m1n5p7r4t6
AWS_REGION=us-east-1
```

**S3 Buckets - Production**
- Device Firmware: `s3://acmeiot-firmware-prod-_DECOY_k9j4m2n7_/`
- User Recordings: `s3://acmeiot-recordings-prod-_DECOY_p3r8t5w1_/`
- Debug Logs: `s3://acmeiot-debug-logs-_DECOY_h7j3n6q2_/`
- Backup: `s3://acmeiot-backups-_DECOY_v2x9z4c6_/`

**RDS Database**
```
DB_HOST=prod-db-cluster-_DECOY_f4g7j2m5_.cluster-abc123.us-east-1.rds.amazonaws.com
DB_NAME=acmeiot_production
DB_USER=app_user_prod
DB_PASSWORD=ProdDB_DECOY_w9k2m7p4_Pass2024!Secure
DB_PORT=5432
```

### Google Cloud Platform (GCP)

**Project: acmeiot-analytics-prod**

**Service Account Key**
```json
{
  "type": "service_account",
  "project_id": "acmeiot-analytics-prod-_DECOY_r7t2w9x4_",
  "private_key_id": "key_id_DECOY_h3j8m1p6_9f4a7c2e",
  "private_key": "-----BEGIN PRIVATE KEY-----\nDECOY_k4m9n2p7_MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIB\n_DECOY_t6v3w8x1_gQC8xK2mN5pR9sT4uV7wX0yZ3aB6cD9eF2gH5iJ8kL1mN4oP6q\n-----END PRIVATE KEY-----",
  "client_email": "prod-analytics-_DECOY_c7f2h9j4_@acmeiot-analytics-prod.iam.gserviceaccount.com"
}
```

**BigQuery Dataset**
- Dataset ID: `analytics_production_DECOY_m3n8p1r6`
- Location: US
- Access via service account above

---

## Third-Party Services

### Twilio (SMS/Notifications)

**Production Account**
```
TWILIO_ACCOUNT_SID=AC_DECOY_x7z2c5f8_prod_9a4f6h2j8k5m1n7p3r
TWILIO_AUTH_TOKEN=twilio_auth_DECOY_v4w9y2b5_prod_k8m3p7r1t6w2x9z4
TWILIO_PHONE_NUMBER=+18559268468
TWILIO_MESSAGING_SERVICE_SID=MG_DECOY_j2m7n4q9_prod_messaging_3f8h1k6
```

**Usage**: 2FA codes, device alerts, system notifications

### SendGrid (Email)

**Production API Key**
```
SENDGRID_API_KEY=SG._DECOY_f3g8h2j7_prod.K4mN9pR2sT6vW0xY3zA5bC8dE1fG4hI7jK0lM3nO6pQ9rS2tU5vW8xY1zA
SENDGRID_FROM_EMAIL=noreply@acmeiot.com
SENDGRID_FROM_NAME=AcmeIoT
```

**Templates:**
- Welcome Email: `d-_DECOY_m7n2p8r3_welcome_template`
- Password Reset: `d-_DECOY_t4v9w1x6_password_reset`
- Device Alert: `d-_DECOY_j5k0m3n8_device_alert`

### Stripe (Payment Processing)

**Production Keys**
```
STRIPE_PUBLIC_KEY=pk_live_DECOY_h8j3k6m1_prod_51K2M4N7P0R3S5T8U1V4W7X0Y3Z6
STRIPE_SECRET_KEY=sk_live_DECOY_p2r7t4w9_prod_abc123XYZ789def456GHI012jkl345
STRIPE_WEBHOOK_SECRET=whsec_DECOY_n5p0r3t8_prod_webhook_v2x7z4c9f1h6j3m8
```

**Connected Account**: acct_DECOY_c6d1f4g9_prod_connect

### Auth0 (Authentication)

**Production Tenant**
```
AUTH0_DOMAIN=acmeiot-prod-_DECOY_b5c0d7e2_.auth0.com
AUTH0_CLIENT_ID=client_DECOY_j7k2m5n0_prod_8pQ3rS6tU9vW2xY5zA8bC1dE4fG
AUTH0_CLIENT_SECRET=secret_DECOY_r4t9v2w7_prod_X0yZ3aC6bD9eF2gH5iJ8kL1mN4oP7qR0sT3uV6wX9yZ
AUTH0_AUDIENCE=https://api.acmeiot.com
```

**Management API**
```
AUTH0_MGMT_CLIENT_ID=mgmt_DECOY_w8x3y6z1_prod_client_f9g2h5i8j1k4m7n0p3
AUTH0_MGMT_CLIENT_SECRET=mgmt_secret_DECOY_k3m8p1r6_prod_Q4rT7uV0wX3yZ6aC9bD2eF5gH8iJ1k
```

### Datadog (Monitoring)

**Production**
```
DD_API_KEY=datadog_api_DECOY_f5g0h3i8_prod_4a7b0c3d6e9f2g5h8i1j4k7m0n3p6
DD_APP_KEY=datadog_app_DECOY_m2n7p0r5_prod_Q8rT1uV4wX7yZ0aC3bD6eF9gH2iJ5
DD_SITE=datadoghq.com
```

### PagerDuty (Incident Management)

**Production Integration**
```
PAGERDUTY_API_KEY=pagerduty_DECOY_c8d1f4g7_prod_u-5yZ8aC1bD4eF7gH0iJ3kL6mN9p
PAGERDUTY_INTEGRATION_KEY=integration_DECOY_j5k0m3n8_prod_R2sT5uV8wX1yZ4aC7b
PAGERDUTY_SERVICE_ID=service_DECOY_t9v2w7x0_prod_P6QRS9TUV2WXY5Z
```

---

## Internal Services

### Redis Cache (ElastiCache)

**Production Cluster**
```
REDIS_HOST=prod-redis-cluster-_DECOY_g3h8i1j6_.abc123.use1.cache.amazonaws.com
REDIS_PORT=6379
REDIS_PASSWORD=redis_prod_DECOY_z5c0d7e2_pass_M4nP7qR0sT3uV6wX9y
REDIS_TLS=true
```

### Elasticsearch (OpenSearch)

**Production Domain**
```
ES_ENDPOINT=https://prod-search-_DECOY_p8r3t6v1_.us-east-1.es.amazonaws.com
ES_USERNAME=admin_prod
ES_PASSWORD=elasticsearch_DECOY_k7m2n5p0_prod_W3xY6zA9bC2dE5fG8hI
```

### Message Queue (RabbitMQ)

**Production Cluster**
```
RABBITMQ_HOST=prod-mq-_DECOY_x4y9z2c7_.mq.us-east-1.amazonaws.com
RABBITMQ_PORT=5671
RABBITMQ_VHOST=/production
RABBITMQ_USERNAME=app_producer
RABBITMQ_PASSWORD=rabbitmq_DECOY_f1g6h9i4_prod_J5kM8nP1qR4sT7uV0w
RABBITMQ_USE_SSL=true
```

---

## API Integrations

### Weather Service (WeatherAPI)

**Production Key**
```
WEATHER_API_KEY=weather_DECOY_b3c8d1e6_prod_key_H4iJ7kM0nP3qR6sT9uV2wX5yZ8a
WEATHER_API_ENDPOINT=https://api.weatherapi.com/v1
```

### Geolocation (IPInfo)

**Production Token**
```
IPINFO_TOKEN=ipinfo_DECOY_r7t2v5w0_prod_token_C9dF2gH5iJ8kL1mN4oP7qR0sT3u
```

### Push Notifications (Firebase Cloud Messaging)

**Server Key**
```
FCM_SERVER_KEY=fcm_key_DECOY_n6p1r4t9_prod_AAAA:BCD123-EFG456_HI789_JKL012_MNO345_PQR678
FCM_PROJECT_ID=acmeiot-mobile-prod-_DECOY_j3k8m1n6_
FCM_SENDER_ID=479382916473
```

**Service Account** (for Admin SDK)
```json
{
  "project_id": "acmeiot-mobile-prod-_DECOY_j3k8m1n6_",
  "private_key": "-----BEGIN PRIVATE KEY-----\n_DECOY_w5x0y3z8_MIIEvAIBADANBgkqhkiG9w0BAQEFAASC\n-----END PRIVATE KEY-----",
  "client_email": "firebase-adminsdk-_DECOY_d2e7f0g5_@acmeiot-mobile-prod.iam.gserviceaccount.com"
}
```

---

## Certificate & Security

### SSL/TLS Certificates

**Production Wildcard Cert**
- Domain: `*.acmeiot.com`
- Issuer: DigiCert
- Private Key Location: AWS Secrets Manager
- Secret ARN: `arn:aws:secretsmanager:us-east-1:847392847392:secret:prod/ssl-cert-_DECOY_h4i9j2k7_`

### Encryption Keys

**Application Master Key** (AES-256)
```
APP_MASTER_KEY=app_master_DECOY_t6u1v4w9_prod_x2yZ5aC8bD1eF4gH7iJ0kL3mN6oP9qR2sT5uV8w
ENCRYPTION_ALGORITHM=AES-256-GCM
```

**JWT Signing Keys**
```
JWT_PRIVATE_KEY_PATH=/secure/keys/jwt_private_DECOY_m5n0p3r8_.pem
JWT_PUBLIC_KEY_PATH=/secure/keys/jwt_public_DECOY_s7t2u5v0_.pem
JWT_ALGORITHM=RS256
JWT_EXPIRY=3600
```

---

## API Rate Limits & Quotas

### AWS Quotas
- API Gateway: 10,000 req/sec
- Lambda concurrent executions: 1,000
- S3 PUT/POST: 3,500 req/sec per prefix

### Third-Party Limits
- Twilio SMS: 100,000/day
- SendGrid Email: 500,000/day
- Stripe API: 100 req/sec

---

## Key Rotation Schedule

- AWS Keys: Every 90 days
- Database Passwords: Every 90 days
- API Keys (3rd party): Every 180 days
- SSL Certificates: 30 days before expiry
- JWT Keys: Every 365 days

**Last Rotation**: February 15, 2024  
**Next Scheduled**: May 15, 2024

**Rotation Procedure**: See `/engineering/runbooks/key-rotation.md`

---

## Emergency Contacts

**Security Incident**: security-incidents@acmeiot.com  
**Key Compromise**: Immediately rotate via AWS Secrets Manager  
**On-Call DevOps**: PagerDuty escalation policy "P1-Infrastructure"

---

## Access Log

This document access is logged. Unauthorized access will be investigated.

| Access Date | User | Purpose | Authorized By |
|-------------|------|---------|---------------|
| 2024-03-15 | jchen@acmeiot.com | Production deployment | CTO |
| 2024-03-10 | smartinez@acmeiot.com | Debug cloud issue | VP Engineering |
| 2024-03-05 | akim@acmeiot.com | Stripe integration update | Engineering Manager |

---

**Document Owner**: Chief Technology Officer  
**Classification**: CONFIDENTIAL  
**Last Updated**: March 15, 2024  
**Next Review**: June 15, 2024

**DESTROY AFTER READING. DO NOT PRINT. DO NOT EMAIL. DO NOT STORE ON UNSECURED DEVICES.**