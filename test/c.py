#coding:utf-8
country=['America','German','English','France','Russia','Italy']
for A in country:
    for B in country:
        for C in country:
            for D in country:
                for E in country:
                    for F in country:
                        if A=='America' or A=='German' or A=='Russia':
                           continue
                        if E=='America' or E=='German' or E=='Russia':
                           continue
                        if C=='America' or C=='German' or C=='Russia':
                           continue
                        if B=='German':
                           continue
                        if F=='German':
                           continue
                        if A=='France':
                           continue
                        if C=='Italy':
                           continue
                        if B=='America':
                           continue
                        if C=='France':
                           continue
                        LIST=[A,B,C,D,E,F]
                        if len(LIST)==len(set(LIST)):
                            print(A,B,C,D,E,F)