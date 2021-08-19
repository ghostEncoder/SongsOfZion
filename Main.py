import sys
import eel
import  FileWriter as fw
import Tamil_Search as ts

#Function To Search A Song
@eel.expose
def Search_Song(song_number):

    import Tamil_Search as ts
    response = ts.SearchSong(song_number)
    return response

#Function To Get Stanzas To Be Printed
@eel.expose
def GetVersesToBePrinted(VersesToBeDisplayed):
    print(VersesToBeDisplayed)
    import Tamil_Search as ts
    response= ts.GetVersesToBePrinted(VersesToBeDisplayed)
    return response

#Function To Reset
@eel.expose
def Reset():
    ts.ClearArrays()
    fw.ClearFiles()

# Function To Exit Application
@eel.expose
def Exit():
    sys.exit(0)

eel.init('web')
eel.start('Index.html')