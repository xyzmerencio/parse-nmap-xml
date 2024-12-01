import xml.etree.ElementTree as ET


dic_nmap = {}

tree = ET.parse("/home/localho0st/Desktop/nmap.xml")
root = tree.getroot()


def parse():
    for i in root.iter("nmaprun"):
        for nmaprun in i:
            if nmaprun.tag == "host":
                for host in nmaprun:
                    if host.tag == "address":
                        if ":" not in host.attrib["addr"]:
                            dic_nmap["ip_v4"] = host.attrib["addr"]
                            dic_nmap["type"] = host.attrib["addrtype"]
                        else:
                            dic_nmap["ip_other"] = host.attrib["addr"]
                            dic_nmap["type"] = host.attrib["addrtype"]
                    if host.tag == "ports":
                        for port in host:
                            if port.tag == 'port':
                                dic_nmap["protocol"] = port.attrib["protocol"]
                                dic_nmap["portid"] = port.attrib["portid"]
                                for itens in port:
                                    if itens.tag == "state":
                                        dic_nmap["state"] = itens.attrib["state"]
                                    if itens.tag == "service":
                                        try:
                                            dic_nmap["name"] = itens.attrib["name"]
                                        except:
                                            dic_nmap["name"] = ""
                                        try:
                                            dic_nmap["product"] = itens.attrib["product"]
                                        except:
                                            dic_nmap["product"] = ""
                                        try:
                                            dic_nmap["ostype"] = itens.attrib["ostype"]
                                        except:
                                            dic_nmap["ostype"] = ""
                                        try:
                                            dic_nmap["method"] = itens.attrib["method"]
                                        except:
                                            dic_nmap["method"] = ""
                                        
                                        print(dic_nmap)

def main():
    parse()
    
    
if __name__ == '__main__':
    main()
