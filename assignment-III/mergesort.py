def mergeSort(number_list):
    if len(number_list)>1:
        mid = len(number_list)//2
        lefthalf = number_list[:mid]
        righthalf = number_list[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                number_list[k]=lefthalf[i]
                i=i+1
            else:
                number_list[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            number_list[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            number_list[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",number_list)

number_list = [14,46,43,27,57,41,45,21,70]
mergeSort(number_list)
print(number_list)