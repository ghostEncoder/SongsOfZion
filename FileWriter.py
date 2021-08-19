
Song_Destination="Outputs//FinalSong.txt"

def ClearSongFiles():
    # Clear Tamil Song Number File
    TamilSongFile = open("Outputs//TamilSongNo.txt", "w")
    TamilSongFile.truncate(0)

def ClearFiles():
    FinalSong = open(Song_Destination, "w", encoding="utf-8")
    FinalSong.truncate(0)


def WriteToFile(CombinedArrays,VersesToBePrinted):
    SelectedStanzasArrayTamil = []
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
                    SelectedStanzasArrayTamil.append(CombinedArrays[i])
                else:
                    FinalSong.writelines(CombinedArrays[i])
                    SelectedStanzasArrayTamil.append(CombinedArrays[i])
                if (index != VersesToBePrintedLength-1):
                    FinalSong.write("\n")

    return SelectedStanzasArrayTamil





    
