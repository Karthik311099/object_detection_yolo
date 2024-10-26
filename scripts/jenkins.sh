#!bin/bash

sudo apt update 

sudo apt install openjdk-8-jdk -y  #install java openjdk

https://pkg.jenkins.io/
https://pkg.jenkins.io/debian-stable/

sudo systemctl start jenkins

sudo systemctl enable jenkins

sudo systemctl status jenkins



## Installing Docker

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker $USER #docker as user mode

sudo usermod -aG docker jenkins # jenkin user mode otherwie it give permission error


newgrp docker

sudo apt install awscli -y

sudo usermod -a -G docker jenkins


## AWS configuration & restarts jenkins

aws configure


## Now setup elastic IP on AWS
#for same ip address



## For getting the admin password for jenkins

sudo cat /var/lib/jenkins/secrets/initialAdminPassword
