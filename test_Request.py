from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

req = Request("https://www.sfchronicle.com/giants/article/Is-Giants-Bruce-Bochy-part-of-a-dying-breed-of-13631991.php")
try:
    response = urlopen(req)
except HTTPError as e:
    print('Error code: ', e.code)
except URLError as e:
    print('Reason: ', e.reason)
else:
    # do something
    print('reading data!')

    data = response.read()
    dst = open("test1.txt", "wb")
    dst.write(data)

finally:
    if response:
        response.close()
    if dst:
        dst.close() 
