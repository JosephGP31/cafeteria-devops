output "instance_public_ip" {
  description = "IP publica asignada a la instancia EC2"
  value       = aws_instance.app_server.public_ip
}

output "ssh_command" {
  description = "Comando para conectarse por SSH al servidor"
  value       = "ssh -i ~/.ssh/cafeteria-aroma ubuntu@${aws_instance.app_server.public_ip}"
}
