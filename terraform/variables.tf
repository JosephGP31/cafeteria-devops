variable "aws_region" {
  type    = string
  default = "us-east-1"
}
variable "project_name" {
  type    = string
  default = "cafeteria-aroma"
}
variable "instance_type" {
  type    = string
  default = "t3.small"
}
variable "my_ip_cidr" {
  type = string
}
variable "ami_id" {
  type    = string
  default = ""
}
