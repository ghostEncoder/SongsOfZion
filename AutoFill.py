mapListHindi = {}
mapListTelugu = {}
def start():
    print("INSIDE AUTOFILL START")
    import csv
    csvfile=open("SongIndex//songindex_Updated.csv","r")
    reader = csv.DictReader(csvfile)

    for i in reader:
       mapListTelugu[i['TELUGU']]=i['HINDI']
       if(bool(i['HINDI'])):
           mapListHindi[i['HINDI']]=i['TELUGU']
    csvfile.close()

def findTelugu(songNo):

    try:
     return mapListHindi[songNo]
    except KeyError:
        return ''

def findHindi(songNo):

    try:
        return mapListTelugu[songNo]
    except KeyError:
        return ''
