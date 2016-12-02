FUNCTION ADDITION (B,C)
    for i in range of length B
        for n in range of length B[0]
            Answer1[i][n] <- b[i][n] + C[i][n]
    return  to function Multiplication(B,C,Answer1)
FUNCTION MULTIPLICATION(B,C, ANSWER1)
    for i in range of length B
        for n in range of length C[0]
            for x in range of length C
                Answer2[i][n] <- Answer2[i][n] + B[i][x] * B[x][n]
    for i in range of length answer1
        for n in range of length Answer1[0]
            Asnwer3[i][n] <- Answer[i][n] * 2
    return to function subtract(Answer2,Answer3)
FUNCTION SUBTRACT(ANSWER2,ANSWER3)
    for i in range of length Answer2
        for n in range of length Answer2[0]
            Answer[i][n] <- Answer2[i][n] - Answer3[i][n]
    return Answer 
    
    
    
    
