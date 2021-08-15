
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
                    CombinedArrays[i][-1]=CombinedArrays[i][-1].strip()
                    FinalSong.writelines(CombinedArrays[i])
                else:
                    FinalSong.writelines(CombinedArrays[i])
                if (index != VersesToBePrintedLength-1):
                    FinalSong.write("\n")



def WriteToFileOld(CombinedArrays,VersesToBePrinted):
    #Clear Files Before Writing
    ClearFiles()
    #Open FIle
    FinalSong=open(Song_Destination,"a",encoding="utf-8")
    for index, i in enumerate(CombinedArrays):
        if len(i)>0 and index in VersesToBePrinted:
            print(i)
            #if you have reached the last stanza remove the newline
            if index<14 and len(CombinedArrays[index+1])==0:
                i[-1]=i[-1].strip()
                FinalSong.writelines(i)

            # if you have reached the 15th stanza remove the newline
            elif index==14 and len(CombinedArrays[index+1])>0:
                i[-1]=i[-1].strip()
                FinalSong.writelines(i)

            else:
                FinalSong.writelines(i)

            # Only add newline gap between stanzas only if another stanza exists
            if index<14 and len(CombinedArrays[index+1])>0:
                FinalSong.write("\n")

            print(index, i)

    FinalSong.close()



    
