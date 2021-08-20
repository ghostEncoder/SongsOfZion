def CombineArrays(tamil_array,telugu_array):
    response=[]

    #if telugu array is empty return only tamil
    if len(telugu_array)!=16:
        response = tamil_array
        return response
    if len(tamil_array) != 16:
        response = telugu_array
        return response
    else:
        for i in range(0,16):
            print(i)
            response.append( tamil_array[i]+["\n"]+telugu_array[i] )

        return response
