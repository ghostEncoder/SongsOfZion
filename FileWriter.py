
Song_Destination="C://Users//jedidiah//Documents//pycharmProjects_OLD//pycharmProjects//Alpha" \
                 "//Songs_Of_Zion_Tamil_V1.0//Outputs//FinalSong.txt"


def ClearFiles():
    FinalSong = open(Song_Destination, "w", encoding="utf-8")
    FinalSong.truncate(0)

def WriteToFile(CombinedArrays,VersesToBePrinted):
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
                else:
                    FinalSong.writelines(CombinedArrays[i])
                if (index != VersesToBePrintedLength-1):
                    FinalSong.write("\n")







    
