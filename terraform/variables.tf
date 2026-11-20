variable "aws_region" {
  description = "Región de AWS donde se desplegará la infraestructura"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Nombre del proyecto para etiquetar recursos en AWS"
  type        = string
  default     = "cafeteria-aroma"
}

variable "instance_type" {
  description = "Tipo de instancia EC2"
  type        = string
  default     = "t3.small"
}

variable "my_ip_cidr" {
  description = "Tu IP pública en formato CIDR para permitir SSH"
  type        = string
}
