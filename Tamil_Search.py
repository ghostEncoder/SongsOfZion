import FileWriter as fw
songs_path="C://Users//jedidiah//Documents//pycharmProjects_OLD//pycharmProjects//Alpha//Songs_Of_Zion_Tamil_V1.0//Tamil_Songs//"

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
CombinedArrays=[chorus,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15]

def ClearArrays():
    for i in CombinedArrays:
        i.clear()


# Function To Search Song s
def SearchSong(song_no):
    if len(song_no)>0:
        print("finding song",song_no)
        song=open(songs_path+str(song_no)+".txt","r",encoding="utf-8")
        SplitSong(song)
    else:

        return "No_Song_Error"

# Function To Split Song
def SplitSong(song):
    ClearArrays()
    for i in song:
        if "c" in i:
            print("Chorus",i)
            CombinedArrays[0].append(i)
        if "s1." in i:
            print("Stanza 1", i)
            CombinedArrays[1].append(i)
        if "s2." in i:
            print("Stanza 2", i)
            CombinedArrays[2].append(i)
        if "s3." in i:
            print("Stanza 3", i)
            CombinedArrays[3].append(i)
        if "s4." in i:
            print("Stanza 4", i)
            CombinedArrays[4].append(i)
        if "s5." in i:
            print("Stanza 5", i)
            CombinedArrays[5].append(i)
        if "s6." in i:
            print("Stanza 6", i)
            CombinedArrays[6].append(i)
        if "s7." in i:
            print("Stanza 7", i)
            CombinedArrays[7].append(i)
        if "s8." in i:
            print("Stanza 8", i)
            CombinedArrays[8].append(i)
        if "s9." in i:
            print("Stanza 9", i)
            CombinedArrays[9].append(i)
        if "s10." in i:
            print("Stanza 10", i)
            CombinedArrays[10].append(i)
        if "s11." in i:
            print("Stanza 11", i)
            CombinedArrays[11].append(i)
        if "s12." in i:
            print("Stanza 12", i)
            CombinedArrays[12].append(i)
        if "s13." in i:
            print("Stanza 13", i)
            CombinedArrays[13].append(i)
        if "s14." in i:
            print("Stanza 14", i)
            CombinedArrays[14].append(i)
        if "s15." in i:
            print("Stanza 15", i)
            CombinedArrays[15].append(i)

    #GetVersesToBePrinted(CombinedArrays)

def GetVersesToBePrinted(VersesToBeDisplayed):
    #verse_to_be_displayed = input("enter stanza to display")
    #verse_to_be_displayed = verse_to_be_displayed.split(" ")
    # function to write song into output file
    fw.WriteToFile(CombinedArrays, VersesToBeDisplayed)



