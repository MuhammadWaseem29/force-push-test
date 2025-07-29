# Configuration file with secrets - DO NOT COMMIT TO PRODUCTION!
DATABASE_URL = "postgresql://user:password123@localhost:5432/mydb"
API_KEY = "sk-1234567890abcdef1234567890abcdef"
SECRET_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY"

# GitHub Personal Access Token - EXTREMELY SENSITIVE!
GITHUB_PAT = "github_pat_11ABCDEFG0123456789_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Slack webhook URL - company internal
SLACK_WEBHOOK = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"

# Private Key for SSH
PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN
OPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890...
-----END RSA PRIVATE KEY-----"""

# Database configuration
DB_HOST = "localhost"
DB_USER = "admin"
DB_PASS = "super_secret_password_123"

# Additional secrets
WEBHOOK_SECRET = "abc123def456ghi789"
STRIPE_SECRET_KEY = "sk_test_1234567890abcdefghijklmnopqrstuvwxyz123456"
