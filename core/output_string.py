from main import *


def format_input_ip(ip_str):
    """Format the input IP address line.

    Args:
        ip_str: The IP address as a string (e.g., "192.168.10.130")

    Returns:
        Formatted string: "Input IP: 192.168.10.130"

    Example:
        format_input_ip("192.168.10.130") -> "Input IP: 192.168.10.130"
    """
    return f"Input IP: {ip_str}\n"


def format_subnet_mask(mask_str):
    """Format the subnet mask line.

    Args:
        mask_str: The subnet mask as a string (e.g., "255.255.255.192")

    Returns:
        Formatted string: "Subnet Mask: 255.255.255.192"

    Example:
        format_subnet_mask("255.255.255.192") -> "Subnet Mask: 255.255.255.192"
    """
    return f"Subnet Mask: {mask_str}\n"


def format_classful_status(class_type):
 
    return f"{class_type}\n"


def format_network_address(network_address):
    """Format the network address line.

    Args:
        network_address: The network address as a string (e.g., "192.168.10.128")

    Returns:
        Formatted string: "Network Address: 192.168.10.128"

    Example:
        format_network_address("192.168.10.128") -> "Network Address: 192.168.10.128"
    """
    return f"Network Address: {network_address}\n"


def format_broadcast_address(broadcast_address):
    """Format the broadcast address line.
    
    Args:
        broadcast_address: The broadcast address as a string (e.g., "192.168.10.191")
        
    Returns:
        Formatted string: "Broadcast Address: 192.168.10.191"
    
    Example:
        format_broadcast_address("192.168.10.191") -> "Broadcast Address: 192.168.10.191"
    """
    return f"Broadcast Address: {broadcast_address}\n"


def format_num_hosts(num_hosts):
    """Format the number of hosts line.
    
    Args:
        num_hosts: The number of usable hosts in the subnet (integer)
        
    Returns:
        Formatted string: "Number of Hosts in this subnet: 62"
    
    Example:
        format_num_hosts(62) -> "Number of Hosts in this subnet: 62"
    """
    return f"Number of Hosts in this subnet: {num_hosts}\n"


def format_cidr_mask(cidr):
    """Format the CIDR mask line.
    
    Args:
        cidr: The CIDR notation number (e.g., 26 for /26)
        
    Returns:
        Formatted string: "CIDR Mask: /26"
    
    Example:
        format_cidr_mask(26) -> "CIDR Mask: /26"
    """
    return f"CIDR Mask: /{cidr}\n"



format_input_ip = format_input_ip(user_input[0])
format_subnet_mask = format_subnet_mask(user_input[0])
# format_classful_status = format_classful_status(class_type)
format_network_address = format_network_address(nice_network_address)
format_broadcast_address = format_broadcast_address(nice_broadcast)
format_num_hosts = format_num_hosts(num_of_host)
format_cidr_mask = format_cidr_mask(bin_to_cidr)


def write_output_file(format_input_ip,format_subnet_mask,format_network_address,format_broadcast_address,format_num_hosts,format_cidr_mask):#פונקציה שכותבת לקובץ
    filename = f"subnet_info_{user_input[0]}_207827924.txt"

    with open(filename, "w") as file:
        file.write(format_input_ip)
        file.write(format_subnet_mask)
        file.write(format_network_address)
        file.write(format_broadcast_address)
        file.write(format_num_hosts)
        file.write(format_cidr_mask)



# Input IP: 192.168.10.130
# Subnet Mask: 255.255.255.192
# Classless
# Network Address: 192.168.10.128
# Broadcast Address: 192.168.10.191
# Number of Hosts in this subnet: 62
# CIDR Mask: /26
