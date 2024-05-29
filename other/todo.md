# To be organized later

# Network

## port

- All URLs have port numbers hidden. The default port number for https is 443, so accessing websites with naver.com:443 works and it hides the port number.


# OS

## Cloud services

### Intro

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

### On prem vs Off prem