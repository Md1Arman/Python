#Given a text file, write a program to create another text file deleting the words ‘a’, ‘the’, ‘an’ and replacing each one of 
# them with a blank space
# Words to remove
lst1 = {'a', 'an', 'the'}



with open("sample2.txt", 'r') as infile, open("hello3.txt", 'w') as outfile:
    for line in infile:
       
        words = line.split()

        cleaned_words = [word for word in words if word.lower() not in lst1]

        outfile.write(' '.join(cleaned_words) + '\n')

print("Finished processing. Cleaned text saved to output.txt")
