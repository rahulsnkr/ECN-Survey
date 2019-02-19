from scapy.all import rdpcap
import sys

# Read PCAP file
packets = rdpcap('sample.pcap')

# First packet from the server will be a SYN+ACK packet, so we need to check if the ECN flag is also set which is denoted by 'E'
if 'E' in packets[0].sprintf("%TCP.flags%"):
    with open("ecn_survey.txt", "a") as f:
        f.write(sys.argv[1].strip() + ',1\n')
else:
    with open("ecn_survey.txt", "a") as f:
        f.write(sys.argv[1].strip() + ',0\n')