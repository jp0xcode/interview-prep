"""
Network Connection Log Analyzer to find bruteforce attempt
--------------------------------
This Python script reads a log file containing network connection events 
and detects possible brute-force scanning activity. Each line of the input 
text file should represent a single network connection event in the following format:

    <source_ip>:<source_port> <destination_ip>:<destination_port>

Example line:
    192.168.1.10:50432 172.217.11.142:443

The script maps each source IP to the destination IPs it contacted, 
along with the distinct ports used. If a source IP connects to the same 
destination IP using more than 3 ports, it's flagged as potential brute-force behavior.
"""


from collections import defaultdict

def file_open():
    File_Path = input("Enter the text file-path with Network connection logs:")
    File =  open(File_Path,"r")
    File_Content = File.read()
    Event_List = File_Content.split("\n") # Split the content by new lines, each representing a network event
    File.close
    return mapping(Event_List)

def mapping(Event_List):
    mapping_set = defaultdict(lambda: defaultdict(set)) #Creates defaultdict which creates key on fly. No need check before and add keys. Creating Nested dictionary.
    for each in Event_List:
        src, dst = each.split(" ")
        src_ip,_ = src.split(":")
        dst_ip, dst_port = dst.split(":")
        mapping_set[src_ip][dst_ip].add(dst_port)
    brute_force_detection(mapping_set)

def brute_force_detection(mapping_set):
    for src_ip, dest_dict in mapping_set.items():
        for dest_ip, dest_port in dest_dict.items():
            if len(dest_port) > 3:
                print(f"BruteForce Found: {src_ip} → {dest_ip}: {len(dest_port)} distinct ports → {sorted(dest_port)}")


if __name__ == "__main__":
    file_open()
