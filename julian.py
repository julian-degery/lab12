#input two lists or tuples and return a list of nested tuples
def lists2tuples(L1,L2):
    
    tupL = tuple()
    temptup = tuple()
    L = list()

    for i in range(len(L1)):
        temptup2 = (L1[i],L2[i])
        L.append(temptup2)
    
    L = tuple(L)
    
    return L

# input a list or tuple and calculate the average increase as a float
def avg_inc(T):
    try:
        L  = list()
        prev = T[0][1]
    
        for i in range(len(T)):
            inc = T[i][1]-prev
            L.append(inc)
            prev = T[i][1]
        
        L.remove(L[0])
        # return the average of the resulting list
        return round(sum(L)/len(L),2)
    except:
        print('Error: avg_inc() failed to execute properly. Check that incoming list or tuple is of the format T = ((year1,value1),(year2,value2)... etc)')
        return None
    
# takes the raw dictionaries with all possible years and removes years before 1973 and after 2014
def crop_data(D):
    CD = dict()
    for k,v in D.items():
        if k >= 1973:
            if k<= 2014:
                CD[k]=D[k]
            else:
                None
        else:
            None
    return CD
    
# final output to be used in visual representations
def finished_calcs_dict():
    calcs_dict = {
'wage':{'ann_avg' : 100.1, 'p_inc' : 1.2, 'avg_inc' : 100.5, 'L_trend' : (1,2,3,4)}, 
'veg':{'ann_avg' : 200.2, 'p_inc' : 2.3, 'avg_inc' : 200.6, 'L_trend' : (4,7,10,13)},
'cattle':{'ann_avg' : 300.3, 'p_inc' : 3.4, 'avg_inc' : 300.7, 'L_trend' : (1,3,8,20)}, 
'college':{'ann_avg' : 400.4, 'p_inc' : 4.5 , 'avg_inc' : 400.8, 'L_trend' : (100,215,350,400)}}
    return calcs_dict

#print out the contents of the final dictionary
def print_results(D):
    for k,v in D.items():
        print(k,':')
        print('anual average from 1973 to 2014 =',"$"+str(D[k]['ann_avg']))
        print('% increase from 1973 to 2014 =',str(D[k]['p_inc'])+"%")
        print('anual average increase from 1973 to 2014 =',"$"+str(D[k]['avg_inc']))
        print('the linear trend is =',D[k]['L_trend'])
        print("")
    return None

#guide to using the julian module
def julians_instructions():
    
    
    fcd = finished_calcs_dict()

    print('keys for each dictionary are:')

    for k,v in fcd.items():
        print(k)

    print('')    
    print('sub keys in each dictionary are:')

    D = fcd['wage']
    for k,v in D.items():
        print(k)
    
    print('')
    print('output for "julian.finished_calcs_dict()" =',fcd)
    print('')
    print('you can output the full dictionary to whatever variable you like, for example fcd')
    print('')
    print("fcd['wage'] =", fcd['wage'])
    print('')
    
    return None