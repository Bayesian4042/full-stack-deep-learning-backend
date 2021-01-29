provider "aws" {
  region = "eu-central-1"
}

terraform {
  backend "s3" {
    bucket  = "fsdl-tf-backend"
    key     = "fsdl.tfstate.backend"
    region  = "eu-central-1"
    encrypt = true
  }
}

locals {
  prefix = "${var.prefix}-${terraform.workspace}"
  common_tags = {
    Environment = terraform.workspace
    Project     = var.project
    ManageBy    = "Terraform"
    Owner       = "abhilasha"
  }
}
