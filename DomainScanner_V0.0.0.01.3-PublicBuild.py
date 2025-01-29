import nmap3
import dns.resolver
import textwrap
import whois
from scapy.all import *
from from_root import from_here
import package_root
import os



# Copyright Info at the bottom of source page.
print("Check the source for Copyright Info", end="\n")

# dns functions:
def get_ip_from_domain(domain_name):

    try:

        resolver = dns.resolver.Resolver()

        answers = resolver.query(domain_name, 'A')

        return answers[0].address

    except Exception as e:

        print(f"Error resolving domain: {e}")

        return None



# Variables!!!!!

domain = str(input("Enter the domain you want to look into:"))

ip_address = get_ip_from_domain(domain)



w = whois(domain)

w1 = str(w)



print(f"IP address for {domain}: {ip_address}") 

#  whois functions
wrapped_string1 = textwrap.wrap(w1, width=len(w1) //int(input("How many wrap lines for WHOIS scan? ")))
print("WHOIS:")
for line in wrapped_string1:
    print(line)

# Scapy/Traceroute Function:
TraceRt = input("Would you like to perform TraceRoute? Y/N ")
if TraceRt == "y" or TraceRt == "Y":
    ip_addressT = ("sudo -S likliklik traceroute " + ip_address)
    with os.popen(ip_addressT) as f:
        TRToutput = f.read
        print(TRToutput)
        
    # This is code that didn't work, but may be useful down the line.
    # It was intended to provide root access, but had faced a few errors.
    #
    #def traceroute(ip_address):
    #    for ttl in range(1, 30):
    #        pkt = IP(dst=ip_address, ttl=ttl) / ICMP()
    #        reply = sr1(pkt, verbose=0, timeout=2)
    #        if reply is None:
    #            print(f"{ttk}. *")
    #        elif reply.type ==3:
    #            print(f"{ttl}. {reply.src}")
    #            break
    #        else:
    #            print(f"{ttl}. {reply.src}")

Tru = "True"
if Tru == "True":
    dest_ip = ip_address
    traceroute(dest_ip)
    
else:
    print()
    print("TraceRoute cancelled by user\n\n")



# nmap functions:
print("NMAP:")
nmap = nmap3.Nmap()
results = nmap.scan_top_ports(ip_address, args="-sV")
results1 = str(results)
wrapped_string = textwrap.wrap(results1, width=len(results1) //int(input("How many wrap lines for nmap scan? ")))
print( 5*" " + "+" + 21*"=" + "+" )
for line in wrapped_string:
    print(line)

# DomainScanner_V0.0.0.01.3-PublicBuild by Dawserdoos GrahamCracker is marked with CC0 1.0 Universal
# Contact pikachu2002@live.com for questions, comments, or assistance.