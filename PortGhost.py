import nmap

nm = nmap.PortScanner()

sudo = True
target = input("enter the ip: ")


print(f"\nScanning {target} on top 1000 ports")
nm.scan(hosts=target, ports="0-65535", arguments="-top-ports 1000 -v -sS -O")

for host in nm.all_hosts():
    print("-" * 60)
    print(f"Nmap scan report for {host} ({nm[host].hostname()})")
    print(f"Host is {nm[host].state()}")
    
    if 'osmatch' in nm[host] and len(nm[host]['osmatch']) >0:
        best_match = nm[host]['osmatch'][0]
        print(f"OS Detection : {best_match['name']} ({best_match['accuracy']}% accuracy)")
    else:
        print("OS Detection : Unknown (could not determine OS reliably)")

    print("-" * 60)
    
    for proto in nm[host].all_protocols():

        print(f"\n{'PORT':<15}{'STATE':<10}{'SERVICE':<20}SCAN METHOD")
        
        lport = sorted(nm[host][proto].keys())
        
        for port in lport:
            state = nm[host][proto][port]['state']
            service = nm[host][proto][port]['name']
            reason = nm[host][proto][port]['reason']

            port_proto = f"{port}/{proto}"
            print(f"{port_proto:<15}{state:<10}{service:<20}{reason}")

print("\nScan finished.")