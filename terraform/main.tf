# ==============================================================================
# Aegis GRC • Sample Cloud Infrastructure (Terraform Baseline)
# Used for Shift-Left Static Compliance & Vulnerability Auditing
# ==============================================================================

terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# --- 1. S3 Storage Buckets (Evaluated for Control A.8.24 Cryptography & A.8.9) ---

# Compliant: Server-side KMS encryption enforced
resource "aws_s3_bucket" "compliance_evidence_vault" {
  bucket = "aegis-production-evidence-vault-2026"

  tags = {
    Environment        = "Production"
    DataClassification = "Restricted"
    Owner              = "Security"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "vault_crypto" {
  bucket = aws_s3_bucket.compliance_evidence_vault.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "aws:kms"
    }
  }
}

# Non-Compliant Test Case: Public logging bucket missing encryption
resource "aws_s3_bucket" "legacy_analytics_temp" {
  bucket = "aegis-legacy-temp-exports"

  tags = {
    Environment        = "Staging"
    DataClassification = "Internal"
  }
}

# --- 2. Security Groups (Evaluated for Control A.8.20 Networks Security) ---

# Compliant: Restricted Bastion SSH ingress to corporate CIDR
resource "aws_security_group" "bastion_ingress" {
  name        = "aegis-bastion-sg"
  description = "Restricted SSH ingress for internal jump host"

  ingress {
    description = "SSH from Corporate Zero-Trust Gateway"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["198.51.100.0/24"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Non-Compliant Test Case: Wide-open database port 5432 to entire Internet
resource "aws_security_group" "unrestricted_db_risk" {
  name        = "aegis-db-misconfigured-sg"
  description = "Flagged misconfiguration: Public ingress to database"

  ingress {
    description = "FLAGGED: Public Postgres access"
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
