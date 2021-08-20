import sys
import eel
import  FileWriter as fw
import Tamil_Search as ts
import Combiner as cm
import Telugu_Search as te
#Variables
CombinedResponse=[]

#Function To Search A Song
@eel.expose
def Search_Song(song_number):
    tamil_song_no = "#"
    telugu_song_no = "#"
    response_tamil = []
    response_telugu = []
    global CombinedResponse
    CombinedResponse = []

    for song in song_number:
        if "TA:" in song:
            tamil_song_no = song.replace("TA:","")
        if "TE:" in song:
            telugu_song_no = song.replace("TE:","")

    #IF SONG NUMBER IS PRESENT CALL THE SEARCH FOR EACH LANGUAGE
    if tamil_song_no != "#":
        response_tamil = ts.SearchSong(tamil_song_no)
    if telugu_song_no != "#":
        response_telugu = te.teleguExtractor(telugu_song_no)

    # if song number is emptry write ~~~
    if tamil_song_no == "#":
        ts.WriteEmptySongNumber()
    if telugu_song_no == "#":
        te.WriteEmptySongNumber()

    #COMBINE BOTH RESPONSES FROM EACH LANGUAGE
    CombinedResponse= cm.CombineArrays(response_tamil,response_telugu)
    return CombinedResponse




#Function To Get Stanzas To Be Printed
@eel.expose
def GetVersesToBePrinted(VersesToBeDisplayed):
    print(VersesToBeDisplayed)
    import FileWriter as fw
    #SEND TO FILEWRITER THE FINAL COMBINED OUTPUT
    global CombinedResponse
    response = fw.WriteToFile(CombinedResponse,VersesToBeDisplayed)
    return response

#Function To Reset
@eel.expose
def Reset():
    ts.ClearArrays()
    te.ClearArrays()
    fw.ClearFiles()
    fw.ClearSongFiles()

# Function To Exit Application
@eel.expose
def Exit():
    sys.exit(0)


#start eel on 8081 port
eel.init('Web')
eel.start('Index.html',port=8081)