def draw_table():
    header='\t{}'.format('\t'.join(map(str,range(1,10))))
    rows=[]
    for i in range(1,10):
        row='\t'.join(map(str, (i*q for q in range(1,10))))
        rows.append('{}\t{}'.format(i,row))
    return header+'\n'+'\n'.join(rows)    

    
print(draw_table())
                                    