from bs4 import BeautifulSoup
from bs4 import Comment
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", help="Write founded comments to an output file", required=False)
parser.add_argument("-t", "--target", help="Webiste address to find comments inside its code", required=True)
args = parser.parse_args()

codename = """
             _  _____  ____       ____   _    ____  ____     
            | |/ / _ \|  _ \ _   |  _ \ / \  |  _ \/ ___|        
            | ' / | | | | | (_)  | |_) / _ \ | |_) \___ \          
            | . \ |_| | |_| |_   |  __/ ___ \|  _ < ___) |        
            |_|\_\___/|____/(_)  |_| /_/   \_\_| \_\____/  
"""

finder = """
  ____                                     _       _____ _           _      
 / ___|___  _ __ ___  _ __ ___   ___ _ __ | |_    |  ___(_)_ __   __| | ___  _ __
| |   / _ \| '_ ` _ \| '_ ` _ \ / _ \ '_ \| __|   | |_  | | '_ \ / _` |/ _ \| '__|
| |__| (_) | | | | | | | | | | |  __/ | | | |_    |  _| | | | | | (_| |  __/| |
 \____\___/|_| |_| |_|_| |_| |_|\___|_| |_|\__|   |_|   |_|_| |_|\__,_|\___||_|                      
\n\n"""

print(codename)
print(finder)

print("\nSearching comments on website: ", args.target)

resp = requests.get(args.target)
data = resp.text
sp = BeautifulSoup(data, "lxml")
comments = list(sp.findAll(text = lambda text: isinstance(text, Comment)))

for i,j in enumerate(comments):
        if j.replace(" ", "") == "":
            comments.pop(i)

if args.output != None:
    with open(args.output, "w") as f:
        for i in comments:
            if i.replace(" ", "") == "":
                continue
            res = "*"*25 + "COMMENT STARTS" + "*"*23 + "\n" + i + "\n" + "*"*25 + "COMMENT ENDS" + "*"*25 + "\n" 
            f.writelines(res)
    print("Results have been written to file: ", args.output)
else:
    for i in comments:
        if i.replace(" ", "") == "":
            continue
        res = "*"*25 + "COMMENT STARTS" + "*"*23 + "\n" + i + "\n" + "*"*25 + "COMMENT ENDS" + "*"*25 + "\n" 
        print(res)

print(str(len(comments)), " comments have founded!")