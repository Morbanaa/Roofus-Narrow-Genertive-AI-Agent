import json

def main():
    while True:
                
        print("Would you:")
        print("1 enter data:")
        print("2 clear data:")
        print("3 create sentence:")
        print("4 exit programm:")
        choice = input("Choose: ")
        
        if choice == "1":
            enter_data()
        elif choice == "2":
            clear_data()
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        else:
            print("Not a valid option")
            continue
						
def enter_data():

    with open("brain.json","r") as file:          
        word_counts = json.load(file)
   
    sentence = input("Enter stuff here(Q to Quit): ").upper()
        
    sentence = sentence.replace(",","").replace(".","")
    words = sentence.split()
    
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]

        if current_word not in word_counts:
            word_counts[current_word] = {}
        if next_word not in word_counts[current_word]:
            word_counts[current_word][next_word] = 0

        word_counts[current_word][next_word] += 1
            
    with open("brain.json","w") as file:
            json.dump(word_counts,file,indent=4,sort_keys=True)
			

def clear_data():
    with open("brain.json","w") as file:
        json.dump({},file,indent=4)

        
if __name__ == "__main__":
		main()

