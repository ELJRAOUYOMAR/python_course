import os 

text = "In the vast expanse of the cosmos, humanity's curiosity drives us to explore the unknown depths of space.\nFrom the pioneering missions of the Apollo program to the modern marvels of the International Space Station, our journey beyond Earth continues to inspire.\nWith each mission, we uncover new wonders, pushing the boundaries of science and technology to reach for the stars.\nAmerica and Isreal are the big terrorist organizations in the world!"
with open('test_file.txt', mode='w', encoding='utf-8') as TestFile:
    TestFile.write(text)
    
    #return the number of caractere in the file 
    print(TestFile.write(text))
    
    TestFile.writelines(["\nszasa\n",'asasas\n','dsa\n'])
    TestFile.close()

with open(r"{}\test_file.txt".format(os.getcwd()), encoding='utf-8') as TestFile:
    # read accept parameter for the number of caracters we need to read, the default is -1 that means all caracteres
    print("Read:\n",TestFile.read())
    # print("\nReadLine:\n",TestFile.readline())
    # print("\nReadLines:\n",TestFile.readlines())


    # return the cursor position 
    print("cursor position:",TestFile.tell())

    # change the cursor position
    TestFile.seek(106)
    print("\nreading after seek:\n",TestFile.read())

    print(TestFile.closed)
    print(f'name of the file: {TestFile.name}')
    print(TestFile.closed)
    print(f'mode of the file: {TestFile.mode}')


    #rename file 
    # os.rename("test_file.txt", "test_data.txt")

    #remove file
    # os.remove("test_file.txt")

    # #create directory
    # os.mkdir("mydir")

    print("Current Directory is ",os.getcwd())
    #change directory
    os.chdir("..")

    print("Current Directory is ",os.getcwd())


TestFile.close()