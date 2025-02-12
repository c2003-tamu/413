#!/bin/bash
echo -e "\n ************running nmap************ \n"
nmap 127.0.0.1

echo -e "\n ************testing port 8080************ \n"
telnet 127.0.0.1 8080

echo -e "\n ************initiating pork knocking************ \n"
telnet 127.0.0.1 1027
telnet 127.0.0.1 1026
telnet 127.0.0.1 1100
telnet 127.0.0.1 1025
telnet 127.0.0.1 1028
telnet 127.0.0.1 1029

echo -e "\n ************port knocking done, trying 8080 again************ \n"
telnet 127.0.0.1 8080

echo -e "\n ************running nmap************ \n"
nmap 127.0.0.1
