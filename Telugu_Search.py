import sqlite3
import FileWriter as fw
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

destination = ""
#Clear all variable arrays
def ClearArrays():
    for i in CombinedArrays:
        i.clear()

# Function To Split Song
def SplitSong(song):
    ClearArrays()
    print(song)
    for i in song:
        print(i)
        if "c" in i:
            print("Chorus",i)
            CombinedArrays[0].append(i)
        if "1." in i:
            print("Stanza 1", i)
            CombinedArrays[1].append(i)
        if "2." in i:
            print("Stanza 2", i)
            CombinedArrays[2].append(i)
        if "3." in i:
            print("Stanza 3", i)
            CombinedArrays[3].append(i)
        if "4." in i:
            print("Stanza 4", i)
            CombinedArrays[4].append(i)
        if "5." in i:
            print("Stanza 5", i)
            CombinedArrays[5].append(i)
        if "6." in i:
            print("Stanza 6", i)
            CombinedArrays[6].append(i)
        if "7." in i:
            print("Stanza 7", i)
            CombinedArrays[7].append(i)
        if "8." in i:
            print("Stanza 8", i)
            CombinedArrays[8].append(i)
        if "9." in i:
            print("Stanza 9", i)
            CombinedArrays[9].append(i)
        if "10." in i:
            print("Stanza 10", i)
            CombinedArrays[10].append(i)
        if "11." in i:
            print("Stanza 11", i)
            CombinedArrays[11].append(i)
        if "12." in i:
            print("Stanza 12", i)
            CombinedArrays[12].append(i)
        if "13." in i:
            print("Stanza 13", i)
            CombinedArrays[13].append(i)
        if "14." in i:
            print("Stanza 14", i)
            CombinedArrays[14].append(i)
        if "15." in i:
            print("Stanza 15", i)
            CombinedArrays[15].append(i)

    #fw.ClearFiles()
    return CombinedArrays

#Function to read the copiedsongtelugu.txt file and send it to be split into arrays
def ReadCopiedSongTelugu():
    TeluguSongFile = open("Outputs/CopiedSongTelugu.txt", "r", encoding="utf-8")
    response = SplitSong(TeluguSongFile)
    return response

def WriteEmptySongNumber():
    # WRITE SONG NUMBER
    SongNoFile = open("Outputs/TeluguSongNo.txt", "w", encoding="utf-8")
    SongNoFile.write("~~~")
    SongNoFile.close()

#Function To read from SQL and copy the song in copiedsongteleug.txt
def teleguExtractor(choice):
    #Return error if song is out of range
    if int(choice)<1 or int(choice)>818:
        return "Out_Of_Range_Error"

    # WRITE SONG NUMBER
    SongNoFile = open("Outputs/TeluguSongNo.txt","w",encoding="utf-8")
    SongNoFile.write(choice)
    SongNoFile.close()

    print("TEL CHOICE", choice)
    f = open("Outputs/CopiedSongTelugu.txt", "w", encoding='utf-8')
    conn = sqlite3.connect("Telugu_Songs/telSongs.db")
    cur = conn.cursor()
    q = cur.execute("SELECT DATA FROM songer WHERE SongNumber={}".format(choice)).fetchall()[0][0]
    print(q)
    loc = q.find("||TELUGU TEXT||")
    song = q[loc:]
    loc = song.find("పల్లవి")

    if (loc >= 0):
        song = song[loc:].split("<br/><br/>")
    else:
        loc = song.find("1.")
        song = song[loc:].split("<br/><br/>")
    nums = [str(i) for i in range(1, 16)]
    print(" ")
    print(song)
    cho = "పల్లవి"
    print(" ")
    for i in song:
        if (i.__contains__(cho)):
            print(" INSIDE TEL EXTRACTOR CHORUS FOUND")
            if ('1.' in i):
                i = i.strip()
                temp = song[0]
                start = temp[0:temp.find('1.')]
                start = start[0:start.rfind("<br/>")]
                end = temp[temp.find('1.'):]
                song.insert(0, start)
                song.insert(1, end)
                song.pop(2)
                print("CLEANUP NEEDED")
                # print(song)
                print(" ")
                k = "c." + song[0]
                k = k.replace("<br/>", "\n" + "c" + ".")

                print(" ")
                f.write(k + "\n")
                f.write("\n")
            else:
                i = i.strip()
                print("CORRECT CORUS")
                k = "c." + i
                k = k.replace("<br/>", "\n" + "c" + ".")

                print(" ")
                f.write(k + "\n")
                f.write("\n")
        elif (len(i) > 0 and i[0] in nums):
            print(i)
            i = i.strip()
            k = i.replace("<br/>", "\n" + i[0] + ". ")
            print(k)
            print(" ")
            f.write(k + "\n")
            f.write("\n")
    f.close()
    response = ReadCopiedSongTelugu()
    return response
