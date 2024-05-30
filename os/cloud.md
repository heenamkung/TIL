
# OS

## Cloud Service

### Virtual Machine

Google docs, google excels, microsoft 365 are all services provided on cloud.
Virtual machine is the fundamental technology behind cloud. 

Traditional approach to deployment. For example:
1. Install OS to hardware
2. Create different accounts for OS (multiple windows user accounts)
3. Install programs on top (LOL, word)

Problem: Program installed on account A may affect account B when installing something new on account B

New approach - Virtual Machines:
Implment computer hardware with software. Use one computer to install multiple OS without needing to install new hardware (CPU, RAM)

Example:
1. Hypervisor (software to run multiple OS on single hardware) on top of hardwares
2. Multiple virtual machines on top of hypervisor
3. OS inside each virtual machines

Pros:
Users can distribute hardware (4gb ram to vm1, 16gb ram to vm2) without having to actually install hardware.

### Off prem vs On prem
#### Off Prem
- Cloud service 
- Service hosted by another company
- Deploy service without physical harware
- AWS

#### On Prem
- Service running on actual hardware: network cables, servers, database, etc.
- e.g. Naver Data Center, Google Data Center

### IaaS, PaaS, SaaS 
#### IaaS
- Infrastructure as a Service 
- Cloud only provides infrastructure
- Users need to install nodejs, mongdoDB, spring etc but they are not tied to a specific service
- AWS EC2, NCP 
- Analogy: an empty room

#### PaaS
- Platform as a service
- Cloud provdies platform
- Nodejs, mongoDB are all installed, or can install them with a click of a button
- Provides monitor, CI/CD
- Heroku
- Analogy: room with basic furnitures and electronics (air conditioning, refrigerator)

#### SAAS
- Software as a Service
- The product running on cloud is already complete and ready for use
- Slack, dropbox, googledocs(edit word documents on multiple devices without having to install word)

### IaaS vs PaaS
Flexibility & Portability : IaaS > PaaS
Cost Efficiency: IaaS < PaaS
- IaaS is an empty room. When moving to a new bigger server, it's much easiser
- PaaS is a room with built in furnitures (nodejs, mongoDB, mySQL). The installed services (nodejs, mongodb) are dependent on the platform. Moving from heroku to another platform might cause migration issues from different versioning. Hence moving to a new server is more difficulty 
- PaaS provides CI/CD, monitoring so its cheaper. 

### Container and Docker
#### Container
- Allows application to run properly on different computing environments by packing all code and dependencies.
- Shares the same OS, making it fast, lightweight (no need to install 10GB OS on each container) and isolated (each container can install any kind of programs). However due to the same OS, a problem with the OS may lead to problems on every container applications.
- Setting up the environment is time consuming and difficult
- Java might not install properly on another server, or the setup might get too complicated such as running scripts to install a db properly
#### Container deployment vs virtual machine deployment
- Container: Infrastructure - Host OS - Docker - App A, App B, ... (Container Applications)

- Virtual Machine: Infrastructure - Hypervisor - VM1, VM2, ... (virtual machines each container their own OS and applications)

#### Docker
- A platform that provides all the functionalities for container deployment (e.g. create containers)
- Combines the advantages of using IaaS and PaaS. Users can move a docker container easily to another computing environment (IaaS). Also docker provdies simple commands (docker pull, docker push) to install and run (PaaS). 

Docker File, Docker Image, Docker Container:
- File: Includes all packages, environment variable. Converted into docker image
- Image: Includes all files, settings, data required to run a container and is immutable. Multiple containers can be made from a single image. What happens inside the container doesn't afftect the image
- Container: Running the container connects the program, data in docker image to actual computing resources. 

### CI / CD
#### Continuous Integration and Continuous Delivery/Deployment
After writing some code, it needs to be continuously integrated to the actual service and continuously delivered and deployed.

#### CI/CD Pipeline
1. CI (1. Build, 2. Test, 3. Merge)
2. Continuous Delivery (Automatically release to repo)
3. Continuous Deployment (Automatally deploy to productions)

The pipeline forces developers to test their code before merging.

CI/CD pipline
- Build: Using .vue extension for frontend dev. However browsers only support html css js. The build process will convert them to html css js. (e.g. Webpack)
- Test: 
    - Unit test: testing a simple function
    - Integration Test: Integrate all software modules(external library, DB) for testing. Might find bug with environment such as not working on multicore cpu. e.g. mocha.js
    - End to end (E2E) test: Before deployment, test the whole service in the point of view of the actual users. If button clicks work properly. 