output "fsdl_bucket_name" {
  value = aws_s3_bucket.fsdl_bucket_backend.id
}

output "cloudfront_distribution_id" {
  value = aws_cloudfront_distribution.s3_distribution.id
}
