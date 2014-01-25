
#score_type = raw_input("Enter 1 for Needleman & Wunsh, 2 for Smith and Waterman")
match = raw_input("how many points for match? ")
mismatch = raw_input("how many points for mismatch? ")
gap = raw_input("how many points for gap penalty? ")

def vertical(nested_list,ver,hor):
    if nested_list == []:
        ver_num = (-1)*(hor+1)
    else:
        ver_num = nested_list[ver-1][hor]
    ver_num = ver_num + int(gap)
    return ver_num

def horizontal(row_list, ver, hor):
    if row_list == []:
        hor_num = (-1)*(ver+1)
    else:
        hor_num = row_list[hor-1]
    hor_num = hor_num + int(gap)
    return hor_num

def diagonal(nested_list, row_list, ver, hor, seq1, seq2):
    if nested_list == []:
        diag_num =  (-1)*(hor)
    elif hor == 0:
        diag_num = (ver)*(-1)   
    else:
        diag_num = nested_list[ver-1][hor-1]
    if seq1[ver] == seq2[hor]:
        value = int(match)
    else:
        value = int(mismatch)
    diag_num =  diag_num + value
    return diag_num

def needleman(horSeq, verSeq):
    matrix_list = []
    for i in range(0,len(verSeq)):
        new_list = []
        for j in range(0, len(horSeq)):
            ver = vertical(matrix_list,i, j)
            hor = horizontal(new_list, i, j)
            diag = diagonal (matrix_list, new_list, i, j, verSeq, horSeq)
           
            largest_num = max(ver, hor,diag)
            new_list.append(largest_num)
        matrix_list.append(new_list)

    print matrix_list
    
#needleman("dfadf","dfadaf")
needleman('actcg', 'acagtag')
