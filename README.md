
# Bitbucket Continous Integration 

## Build docker image and push to dockerhub. 

- Create Bitbucket account

- Enable MFA authentication 

- Create Project and repository

- Write script and push to repository

- Enable pipeline 

- Install SonarQube 

- Add SonarQube on to your pipeline 

# Project Title

In this project we are going to build docker image using Bitbucket, scan the code and push to docker dockerhub. 


## Need to create SonarQube server

Launch EC2 Ubuntu instance 

```bash
  Launch Ubuntu server 
  t2.micro
  Add Storage
  Add Default VPC, Availability zones
  Allow in security group required ports http, ssh, 9000
```

```bash
 Follow below commands to install SonarQube

 adduser sonarqube    #pass: sonar@123
 wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-9.4.0.54424.zip
 sudo apt install unzip
 chmod -R 755 /home/sonarqube/sonarqube-9.4.0.54424
 chown -R sonarqube:sonarqube /home/sonarqube/sonarqube-9.4.0.54424
 cd sonarqube-9.4.0.54424/bin/linux-x86-64/
 should not run as root user: 
 ./sonar.sh start
```

# Server creation

![App Screenshot](https://mysample-s3-webpage-09062023.s3.ap-south-1.amazonaws.com/Server+creation.jpg)

# Switch to Sonar user

![App Screenshot](https://mysample-s3-webpage-09062023.s3.ap-south-1.amazonaws.com/Switch+sonaruser.jpg)

# Start SonarQube  

## move to below path   /opt/sonarqube/bin/linux-x86-64

## start sonarqube ./sonar.sh start

![App Screenshot](https://mysample-s3-webpage-09062023.s3.ap-south-1.amazonaws.com/start+sonarqube.jpg)

# Login SonarQube

## copy server ip and hit browser public-ip:9000

## username: admin password: admin

## change the password first time

![App Screenshot](https://mysample-s3-webpage-09062023.s3.ap-south-1.amazonaws.com/login+sonar.jpg)


# Below files we need 

- Dockerfile

- bitbucket-pipelines.yml

- sonar-project.properties


## Write Docker file 

## Choose python build spec image from template

## For sonar properties we need to create from sonarqube, choose as local as per below snapshot

![App Screenshot](https://mysample-s3-webpage-09062023.s3.ap-south-1.amazonaws.com/sonar+local.jpg)

## Choose local 

![App Screenshot](https://mysample-s3-webpage-09062023.s3.ap-south-1.amazonaws.com/sonar+3.jpg)

## create project in sonarqube

![App Screenshot](https://mysample-s3-webpage-09062023.s3.ap-south-1.amazonaws.com/sonar+4.jpg)

## after choose key words choose type of code. Here we have python. Copy the script. This script need to include in our pipeline 

![App Screenshot](https://mysample-s3-webpage-09062023.s3.ap-south-1.amazonaws.com/sonar+5.jpg)

## Next we need to create to pipeline in our bitbucket. Commit the codes to repo

##  Enable pipeline 

## Choose the template of python code add in that our sonarqube script 

## in pipeline need to add our variable values as per below snapshot

![App Screenshot](https://mysample-s3-webpage-09062023.s3.ap-south-1.amazonaws.com/variables.jpg)


##  As per below snapshot we have build image and pushed to dockerhub


![App Screenshot](https://mysample-s3-webpage-09062023.s3.ap-south-1.amazonaws.com/bitbucket+run.jpg)



## Sonarqube scan 


![App Screenshot](https://mysample-s3-webpage-09062023.s3.ap-south-1.amazonaws.com/sonarscan+output.jpg)


## Dockerhub image pushed 

![App Screenshot](https://mysample-s3-webpage-09062023.s3.ap-south-1.amazonaws.com/dockerhub.jpg)



