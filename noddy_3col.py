text = "I am Noddy, I dont like to focus but I like to smoke weed every day Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

text_list = text.split(" ")

space = 3

A = []
B = []
C = []
flag = 1                            #Flag 1 for A, 2 for B, 3 for C
for i, word in enumerate(text_list):
    if flag==1:
        para = A
    elif flag==2:
        para = B
    elif flag==3:
        para = C

    para.append(word)
    i+=1
    if (i%space)== 0 :
        flag+1
    if flag==4:
        flag = 1

        print("i {} flag {} para {} ----- {}%{} = {}".format(i,flag,para,i+1,space,i%space))

print(A)
print(B)
print(C)

A_string = " ".join(A)
B_string = " ".join(B)
C_string = " ".join(C)

print("A_string\n")
print(A_string)
print("B_string\n")
print(B_string)
print("C_string\n")
print(C_string)
print("\n")
