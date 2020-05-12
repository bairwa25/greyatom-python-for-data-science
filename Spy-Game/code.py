# --------------
##File path for the file 
file_path 
#function that take 'path' as parameter
def read_file(path):
    file = open(path,'r')
    sentence = file.readline()
    file.close()
    return sentence
#calling the fuction
sample_message = read_file(file_path)
sample_message

#Code starts here


# --------------
########### Message Fusion ###############

#Code starts here
file_path_1 
file_path_2

def read_file(path_1):
    file = open(path_1,'r')
    sentence = file.readline()
    file.close()
    return sentence
#calling the fuction
message_1 = read_file(file_path_1)


def read_file(path_2):
    file = open(path_2,'r')
    sentence = file.readline()
    file.close()
    return sentence

message_2 = read_file(file_path_2)
print(message_1)
print(message_2)


def fuse_msg(message_a,message_b):
    A = int(message_a)
    B = int(message_b)
    quotient = (B//A)
    return str(quotient)


#calling the fuction
secret_msg_1 = fuse_msg(message_1,message_2)
secret_msg_1







# --------------
############## Message Substitution ############3

#Code starts here
#file path
file_path_3
#funtion to store message
def read_file(path_3):
    file = open(path_3,'r')
    sentence = file.readline()
    file.close()
    return sentence
#calling the fuction
message_3 = read_file(file_path_3)
print(message_3)

def substitute_msg(message_c):
    if message_c is 'Red':
        sub = 'Army General'
    elif message_c is 'Blue':
        sub = 'Marine Biologist'
    else:
        sub = 'Data Scientist'
    return sub
#

secret_msg_2 = substitute_msg(message_3)
secret_msg_2



# --------------
############## Message Comparision ############
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here

#funtion to store message path_4
def read_file(path_4):
    
    file = open(path_4,'r')
    sentence = file.readline()
    file.close()
    return sentence
#calling the fuction
message_4 = read_file(file_path_4)

#funtion to store message path_5
def read_file(path_5):
   
    file = open(path_5,'r')
    sentence = file.readline()
    file.close()
    return sentence

#calling the fuction
message_5 = read_file(file_path_5)

#display the message 4  and message 5
print(message_4)
print(message_5) 

#function that Takes message_d and message_e as parameters:
def compare_msg(message_d,message_e):


    #spliting message into words
    a_list = message_d.split()
    b_list = message_e.split()
    #creat list that stores all words are there in 
    #a_list but not in b_list using Comprehensions
    c_list = [i for i in a_list if i not in b_list]

    #combine c_list list words using join()
    final_msg = " ".join(c_list)
    return final_msg

# calling the function
secret_msg_3 = compare_msg(message_4,message_5)
# display the function
secret_msg_3




# --------------
################ Message Filter ###################

#Code starts here
# File path for message 6
file_path_6

#funtion to store message path_6
def read_file(path_6):
    
    file = open(path_6,'r')
    sentence = file.readline()
    file.close()
    return sentence

#calling the fuction
message_6 = read_file(file_path_6)

#display the message 6
print(message_6)

#function that Takes message_f as parameters:
def extract_msg(message_f):

    #spliting message into words
    a_list = message_f.split()
    
    # lambda function for even length of var "x":
    even_word = lambda x : True if len(x)%2==0 else False
    
    # Implements filter() function with function parameter as even_word
    # and sequence parameter as a_list
    b_list = filter(even_word,a_list)
    
    # Combines the words of b_list back to a sentence 
    final_msg = " ".join(b_list)

    # return value of final msg 
    return final_msg

# calling the function
secret_msg_4 = extract_msg(message_6)

# display the msg in function
secret_msg_4
    


    


# --------------
################# Message Writing ##########################

#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


final_path= user_data_dir + '/secret_message.txt'

#Code starts here
# Combine the contents of message_parts into a single sentence
secret_msg = " ".join(message_parts)


# function that Takes secret_msg and path as parameters:
def write_file(secret_msg,path):

    # open file in write mode
    file = open(path,'a+')
    # write secret_msg to the file
    file.write(secret_msg)
    # close file
    file.close()
# Calling the function "write_file()"   
write_file(secret_msg,final_path) 
# display the content of the secret_msg
print(secret_msg)  





