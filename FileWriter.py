
Song_Destination="Outputs//FinalSong.txt"

def ClearSongFiles():
    # Clear Tamil Song Number
    TamilSongFile = open("Outputs//TamilSongNo.txt", "w")
    TamilSongFile.truncate(0)
    TamilSongFile.close()

    #CLEAR TELUGU SONG NUBMER
    TeluguSongNoFile = open("Outputs/TeluguSongNo.txt", "w", encoding="utf-8")
    TeluguSongNoFile.truncate(0)
    TeluguSongNoFile.close()

    # CLEAR HINDI SONG NUMBER
    HindiSongFile = open("Outputs//HindiSongNo.txt", "w", encoding="utf-8")
    HindiSongFile.truncate(0)
    HindiSongFile.close()

    #CLEAR HINDI SONG TITLE
    title = open("Outputs//HindiTitle.txt", "w", encoding="utf-8")
    title.truncate(0)
    title.close()

def ClearFiles():
    FinalSong = open(Song_Destination, "w", encoding="utf-8")
    FinalSong.truncate(0)


def WriteToFile(CombinedArrays,VersesToBePrinted):
    SelectedStanzasArray = []
    #Clear Files Before Writing
    ClearFiles()
    #Open FIle
    FinalSong=open(Song_Destination,"a",encoding="utf-8")
    VersesToBePrintedLength=len(VersesToBePrinted)
    if VersesToBePrintedLength>0:
        for index, i in enumerate(VersesToBePrinted):
            if len(CombinedArrays[i])>0:
                if index == VersesToBePrintedLength-1:
                    #CombinedArrays[i][-1]=CombinedArrays[i][-1].strip()
                    FinalSong.writelines(CombinedArrays[i][:-1])
                    FinalSong.write(CombinedArrays[i][-1][:-1])
                    SelectedStanzasArray.append(CombinedArrays[i])
                else:
                    FinalSong.writelines(CombinedArrays[i])
                    SelectedStanzasArray.append(CombinedArrays[i])
                if (index != VersesToBePrintedLength-1):
                    FinalSong.write("\n")

    return SelectedStanzasArray





    
