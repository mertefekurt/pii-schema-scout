from __future__ import annotations

from pii_schema_scout.models import Rule

PROJECT_NAME = 'pii-schema-scout'
DESCRIPTION = 'Find privacy-sensitive fields in schemas, exports, and data dictionaries.'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "service", "dataset", "route", "metric", "field", "path")
HIGH_SAMPLE = 'customer_email, phone_number, ssn, billing_address'
MEDIUM_SAMPLE = '\\b(email|phone|address|full_name|date_of_birth)\\b'
CLEAN_SAMPLE = 'account_id, plan_name, created_at, region_code'

RULES = (
    Rule(
        code='government-id-field',
        severity='high',
        pattern='\\b(ssn|social security|passport|national_id|tax_id)\\b',
        message='government identifier field detected',
        recommendation='Require privacy review, masking, and access controls.',
    ),
    Rule(
        code='contact-pii-field',
        severity='medium',
        pattern='\\b(email|phone|address|full_name|date_of_birth)\\b',
        message='direct contact or identity field detected',
        recommendation='Confirm purpose, retention, and minimization requirements.',
    ),
    Rule(
        code='location-field',
        severity='low',
        pattern='\\b(ip_address|latitude|longitude|geo|postal_code)\\b',
        message='location-like field detected',
        recommendation='Check whether location precision is necessary.',
    ),
)
