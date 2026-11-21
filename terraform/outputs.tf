output "instance_public_ip" {
  value = aws_instance.app_server.public_ip
}
output "app_url" {
  value = "http://${aws_instance.app_server.public_ip}"
}
output "ssh_command" {
  value = "ssh -i ~/.ssh/cafeteria-aroma ubuntu@${aws_instance.app_server.public_ip}"
}
