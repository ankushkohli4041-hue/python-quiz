score=0
print("_______________________________quiz_____________________________")
print("1. Which keyword is used to define a function in Python?")
print("A. function")
print("B. def")
print("C. define")
print("D. fun")
answer=input("enter your answer")
if answer.upper()=="B":
    print("currect answer")
    score+=1
else:
    print("not a correct answer")
print("______________________________________________________________")
print("2. Which of the following is a valid Python variable name?")
print("A. class")
print("B. 2num")
print("C. class roll no")
print("D. name_")
answer=input("enter your answer")
if answer.upper()=="D":
    print("currect answer")
    score+=1
else:
    print("not a correct answer")
print("____________________________________________________________")
print("3. What is the output of print(2 + 3 * 4)?")
print("A. 34")
print("B. 20")
print("C. 14")
print("D. 10")
answer=input("enter your answer")
if answer.upper()=="C":
    print("currect answer")
    score+=1
else:
    print("not a correct answer")
print("_____________________________________________________________")
print("4. Which data type is used to store True or False?")
print("A. int")
print("B. float")
print("C. str")
print("D. bool")
answer=input("enter your answer")
if answer.upper()=="D":
    print("currect answer")
    score+=1
else:
    print("not a correct answer")
print("_____________________________________________________________")
print("5. What is the output of print(len(''Python''))?")
print("A. len")
print("B. 3")
print("C. 6")
print("D. error")
answer=input("enter your answer")
if answer.upper()=="C":
    print("currect answer")
    score+=1
else:
    print("not a correct answer")
print("______________________________________________________________")
print("6. Which symbol is used for a single-line comment in Python?")
print("A. //")
print("B. /*")
print("C. __")
print("D. #")
answer=input("enter your answer")
if answer.upper()=="D":
    print("currect answer")
    score+=1
else:
    print("not a correct answer")
print("_______________________________________________________________")
print("7. Which of the following is a Python list?")
print("A. (1, 2, 3)")
print("B. {1, 2, 3}")
print("C. [1, 2, 3]")
print("D. <1, 2, 3>")
answer=input("enter your answer")
if answer.upper()=="C":
    print("currect answer")
    score+=1
else:
    print("not a correct answer")
print("________________________________________________________________")
print("8. What is the output of print(10 // 3)?")
print("A. 3.33")
print("B. 3")
print("C. 4")
print("D. 1")
answer=input("enter your answer")
if answer.upper()=="B":
    print("currect answer")
    score+=1
else:
    print("not a correct answer")
print("________________________________________________________________")
print("9. Which operator is used for exponentiation in Python?")
print("A. ^")
print("B. **")
print("C. //")
print("D. %%")
answer=input("enter your answer")
if answer.upper()=="B":
    print("currect answer")
    score+=1
else:
    print("not a correct answer")
print("________________________________________________________________")
print("10. Which function is used to take input from the user?")
print("A. get()")
print("B. scan()")
print("C. input()")
print("D. read()")
answer=input("enter your answer")
if answer.upper()=="C":
    print("currect answer")
    score+=1
else:
    print("not a correct answer")
print("________________________________________________________________")
print("TOTAL QUESTION = 10")
print("OBTAIN MARKS=",score)
print("WRONG ANSWER=",10-score)