Project 0x08-networking_basics_2

Concepts Covered

1. What is localhost/127.0.0.1?
The hostname "localhost" refers to the current computer and always resolves to the IP address 127.0.0.1. It is frequently used to access services running on the local system.
2. What is 0.0.0.0?
The IP address 0.0.0.0 is a special-purpose address that often represents "any address" or "all addresses". It can be used in a variety of scenarios, including indicating a default route and binding a server socket to all accessible network interfaces.
3. What is /etc/hosts?
Definition: The /etc/hosts file is a plain-text file on Unix-like operating systems that maps hostnames to IP addresses. It is used for local hostname resolution and can be manually edited to override DNS settings or define custom hostname mappings.
4. How to display your machine’s active network interfaces?
Method: To display information about active network interfaces on your machine, run the ifconfig command (or the ip addr command on newer systems). This command returns information such as IP addresses, MAC addresses, and interface status.
