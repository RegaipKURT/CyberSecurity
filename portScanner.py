#ÖRNEK AMAÇLI YAZILMIŞ BİR PORT TARAYICI

import argparse, socket

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--destination", type=str, help="Destination ip address", required=True)
parser.add_argument("-p", "--ports", help="Ports to scan", required=True)
parser.add_argument("-o", "--output", type=str, help="Output file")
parser.add_argument("-t", "--timeout", type=int, help="Timeout value to connect")
args = parser.parse_args()

targets = [args.destination] if "," not in args.destination else list(args.destination.split(",")) 
ports = list(args.ports.split(sep=",")) if "-" not in args.ports else [i for i in range(int(args.ports.split("-")[0]), int(args.ports.split("-")[1])+1)]
timeout = args.timeout if args.timeout else 2
outputFile = open(args.output, "w") if args.output else False


def portConn(target, port):
    try:
        port = int(port)
        s.settimeout(timeout)
        s.connect((target, port))
        return True
    except:
        return False

print("\nScannig Targets: {}\n".format(targets))

portCounter = 0
for target in targets:
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if portConn(target, port):
            portCounter+=1
            print("-"*49)
            print("| Port \t {} \t open on \t{} \t|".format(port, target))
            if outputFile:
                outputFile.writelines("Port {} \topen on \t{}\n".format(port, target))
        else:
            pass

print("-"*49)

print("\n{} open ports found on total {} targets!".format(portCounter, len(targets)))
