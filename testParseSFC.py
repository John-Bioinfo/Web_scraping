import os, re
import json, io
import urllib.request
from urllib.request import Request
from urllib.request import urlopen
from urllib.parse import urlencode, quote_plus


scURL = "https://www.sfchronicle.com/giants/article/Is-Giants-Bruce-Bochy-part-of-a-dying-breed-of-13631991.php"
headers = [('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')]
## "https://www.sfchronicle.com/bayarea/article/SF-s-corridor-ambassadors-more-than-13632044.php"
## "https://www.sfchronicle.com/homeandgarden/article/Gardenlust-looks-at-best-21st-century-13580871.php"

if not os.path.exists("database.json"):
    ## request url and get data, then store data into json file
    opener = urllib.request.build_opener()
    opener.addheaders = headers
    resources = opener.open(scURL, data=None).read()
    decData = resources.decode("utf-8")

## ----------------------------------------------------------------------  
    jsonData = json.dumps({"test_data": decData} , ensure_ascii=False)
    # use dump , not dumps          
    with open("database.json", "w") as dump_file:
        json.dump(jsonData, dump_file)

# load data from the stored json file

with io.open("database.json", "r") as source_d:
    a = json.load(source_d)
    newDict = json.loads( a )
    ## json.loads(a) will return string object, and it need string input, as "a" above

newData = newDict["test_data"]
newData = newData.replace("\n", '')

## href="https://www.sfchronicle.com/bayarea/article/SF-s-corridor-ambassadors-more-than-13632044.php" />
#res_data = re.findall("href\=\"(https\:.*?.php)\" \/>", newData, re.S)
##res_data = re.findall("href\=\"(https\:\/\/www\.sfchronicle\.com.*?\.php)\" ", newData)
##res_data = re.findall("https\:\/\/www\.sfchronicle\.com.*?\.php", newData)
res_data = re.findall("href\=\"\S+.php\"", newData)

linkSets=set()
for i in res_data:
    if i.startswith("href=\"https://www.sfchronicle.com"):
        linkSets.add(i[6:-1])        
    elif i.split("/")[1] in ["giants", "food", "opinion", "crime", "warriors", "bayarea", "travel","sports", "collegesports"]:
        linkSets.add("https://www.sfchronicle.com" + i[6:-1])
    
##print(newData.find("SF-s-filthy-streets-We-re-spending-far-more-13215702."))
