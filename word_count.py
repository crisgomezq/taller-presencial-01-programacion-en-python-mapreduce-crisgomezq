import glob
import fileinput
import os.path


def load_input(input_directory):

    sequence = []
    dir_path = input_directory + "/*"
    filenames = glob.glob(dir_path)

    
    with fileinput.input(files=filenames) as f:
        for line in f:
                tupla = (fileinput.filename(), line)
                sequence.append(tupla)

    return sequence
            

def mapper (sequence):
    new_sequence=[]
    for _, text in sequence:
        words = text.split()
        for word in words:
            word= word.replace(",", "")
            word= word.replace(".", "")
            word=word.lower()
            new_sequence.append([word,1])
    
    return new_sequence



def shuffle_and_sort (sequence):
    new_sequence=sorted(sequence, key=lambda x:x[0])
    return new_sequence


def reducer (sequence): 
    diccionario={}

    for key, value in sequence:
        if key not in diccionario.keys():
            diccionario[key]=0
        diccionario[key]+=value

    new_sequence=[]
    for key, value in diccionario.items():
        tupla = (key,value)
        new_sequence.append(tupla)

    return new_sequence
    


def create_output_directory(output_directory):

    if os.path.exists(output_directory):
        raise FileExistsError(f"The directory '{output_directory}' alredy exists.")
    os.makedirs(output_directory)
    

def save_output(output_directory, sequence):
   
   with open(output_directory +"/part-0000", "w") as file:
       for key, value in sequence:
           file.write(f"{key}\t{value}\n")
       

def create_marker(output_directory):
    with open(output_directory +"/_SUCCESS", "w") as file:
        file.write("")


def job(input_directory, output_directory):
    
    sequence =load_input(input_directory)
    sequence = mapper (sequence)
    sequence = shuffle_and_sort (sequence)
    sequence = reducer(sequence)
    create_output_directory(output_directory)
    save_output(output_directory, sequence)
    create_marker(output_directory)


if __name__ == "__main__":
    job(
        "input",
        "output",
    )
    #fin#