import sys
import getpass
from myfunctions.ip_addr_valid import ip_addr_valid
from myfunctions.ip_reach import ip_reach
from myfunctions.ip_file_valid import ip_file_valid
from myfunctions.create_threads import create_threads, create_threads1
from myfunctions.generate_tsf import generate_tsf

# Enter username
firewall_admin = input("Please Enter firewall username: ")
# Enter password for firewall
firewall_password = getpass.getpass("Please enter firewall password: ")
    # Saving the list of ip address in in ip.txt to a variable
ip_list = ip_file_valid()

    # verifying the validity of each ip address in the list
try:
    ip_addr_valid(ip_list)

except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()

    # Verifying the reachablity of each IP address in the list
try:
    ip_reach(ip_list)

except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()

create_threads(ip_list, firewall_admin, firewall_password, generate_tsf)
#End of program
