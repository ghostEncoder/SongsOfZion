import FileWriter as fw
songs_path="C://Users//jedidiah//Documents//pycharmProjects_OLD//pycharmProjects//Alpha//Songs_Of_Zion_Tamil_V1.0//Hindi_Songs//"

#Variables
chorus=[]
s1=[]
s2=[]
s3=[]
s4=[]
s5=[]
s6=[]
s7=[]
s8=[]
s9=[]
s10=[]
s11=[]
s12=[]
s13=[]
s14=[]
s15=[]
Hindi_Song_Title=[]
CombinedArrays=[chorus,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15]

#Clear all variable arrays
def ClearArrays():
    global Hindi_Song_Title
    Hindi_Song_Title.clear()
    for i in CombinedArrays:
        i.clear()

def ConvertToThreeDigit(Song_No):
    if len(Song_No) == 1:
        Song_No='0'+'0'+Song_No
    elif len(Song_No) == 2:
        Song_No = '0' + Song_No
    else:
        Song_No = Song_No
    return Song_No

# WRITE ~~~ INCASE OF NO TAMIL SONG NUMBER
def WriteEmptySongNumber():
    # WRITE SONG NUMBER
    SongNoFile = open("Outputs/HindiSongNo.txt", "w", encoding="utf-8")
    SongNoFile.write("~~~")
    SongNoFile.close()
    
# Function To Search Song s
def SearchSong(Song_No):
    if len(Song_No)>0:
        if int(Song_No) < 1 or int(Song_No) > 755:
            return "Out_Of_Range_Error"
        else:
            Song_No=ConvertToThreeDigit(Song_No)
            print("finding song",Song_No)
            song=open(songs_path+str(Song_No)+".txt","r",encoding="utf-8")
            #Write Hindi Song Number
            HindiSongFile = open("Outputs//HindiSongNo.txt", "w")
            HindiSongFile.write(Song_No)
            HindiSongFile.close()
            response = SplitSong(song)
            return response
    else:

        return "No_Song_Error"

def WriteHindiTitle(Song_Title):
    title = open("Outputs//HindiTitle.txt", "w",encoding="utf-8")
    title.write(Song_Title[0])
    title.close()

# Function To Split Song
def SplitSong(song):
    ClearArrays()
    global CombinedArrays
    for i in song:
        if "v:" in i:
            print(i.replace("v:",""))
            Hindi_Song_Title.append(i.replace("v:",""))
        if "V:" in i:
            print(i.replace("V:", ""))
            Hindi_Song_Title.append(i.replace("V:", ""))
        if "c" in i:
            print("Chorus",i)
            CombinedArrays[0].append(i)
        if "s1." in i:
            print("Stanza 1", i)
            CombinedArrays[1].append(i.replace("s",""))
        if "s2." in i:
            print("Stanza 2", i)
            CombinedArrays[2].append(i.replace("s",""))
        if "s3." in i:
            print("Stanza 3", i)
            CombinedArrays[3].append(i.replace("s",""))
        if "s4." in i:
            print("Stanza 4", i)
            CombinedArrays[4].append(i.replace("s",""))
        if "s5." in i:
            print("Stanza 5", i)
            CombinedArrays[5].append(i.replace("s",""))
        if "s6." in i:
            print("Stanza 6", i)
            CombinedArrays[6].append(i.replace("s",""))
        if "s7." in i:
            print("Stanza 7", i)
            CombinedArrays[7].append(i.replace("s",""))
        if "s8." in i:
            print("Stanza 8", i)
            CombinedArrays[8].append(i.replace("s",""))
        if "s9." in i:
            print("Stanza 9", i)
            CombinedArrays[9].append(i.replace("s",""))
        if "s10." in i:
            print("Stanza 10", i)
            CombinedArrays[10].append(i.replace("s",""))
        if "s11." in i:
            print("Stanza 11", i)
            CombinedArrays[11].append(i.replace("s",""))
        if "s12." in i:
            print("Stanza 12", i)
            CombinedArrays[12].append(i.replace("s",""))
        if "s13." in i:
            print("Stanza 13", i)
            CombinedArrays[13].append(i.replace("s",""))
        if "s14." in i:
            print("Stanza 14", i)
            CombinedArrays[14].append(i.replace("s",""))
        if "s15." in i:
            print("Stanza 15", i)
            CombinedArrays[15].append(i.replace("s",""))
            
    #WRITE THE HINDI TITLE
    WriteHindiTitle(Hindi_Song_Title)
    fw.ClearFiles()
    return CombinedArrays
    #GetVersesToBePrinted(CombinedArrays)

def GetVersesToBePrinted(VersesToBeDisplayed):
    # function to write song into output file
    response = fw.WriteToFile(CombinedArrays, VersesToBeDisplayed)
    return response

