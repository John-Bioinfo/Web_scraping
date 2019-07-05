import json
from io import StringIO 
from urllib.request import urlopen 
from urllib.error import HTTPError 
from urllib.parse import quote_plus

def json_from_url(url): 

    """Returns API response after decoding and loading JSON. """ 

    response = urlopen(url) 
    data = response.read().decode('utf-8') 

    return json.loads(data) 

def output_cnv(jsonData):
    gene_data =  jsonData["associations"]
    for i in gene_data:
        data = i['gene']
        geneName = data['symbol']
        threshold = i['thresholdValue']
        copy_value = i['standardizedValue']
        print('{0}\t{1}\t{2}'.format(geneName, threshold, copy_value))

cell_line = '639V'
#cell_line = '22RV1'

data_url = "http://amp.pharm.mssm.edu/Harmonizome/api/1.0/gene_set/" + cell_line + "/CCLE+Cell+Line+Gene+CNV+Profiles"


try: 
    ##response = urlopen(url)
    res = json_from_url(data_url)
    output_cnv(res)
except HTTPError: 
    # Not every dataset has all downloads. 
    print(cell_line + ' CNV data not downloaded properly.')
    pass
