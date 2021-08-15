import eel
@eel.expose
def Search_Song(song_number):

    import Tamil_Search as ts
    response = ts.SearchSong(song_number)
    return response
    
@eel.expose
def GetVersesToBePrinted(VersesToBeDisplayed):
    print(VersesToBeDisplayed)
    import Tamil_Search as ts
    response= ts.GetVersesToBePrinted(VersesToBeDisplayed)



eel.init('web')
eel.start('Index.html')