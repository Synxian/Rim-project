import os
from common import vector_de_intensidades

class Searcher:
    """Class that handles the letter search and writes the final result"""
    def __init__(self):
        self.string = ''
        self.current_letter = 0
        self.input_folder = 'input'
        self.output_file = 'output.txt'
        self.k = 3
        self.dataset_descriptors = self.get_dataset_descriptors()
        self.dataset_names = self.get_dataset_names()

    def get_dataset_descriptors(self):
        pass

    def get_dataset_names(self):
        pass

    def get_knn(self):
        """Gets the k nearest neighbors"""
        descriptor = vector_de_intensidades(f'{self.input_folder}/letter_{self.current_letter}')

    def search_image(self):
        """Compare image descriptors to get new letter"""
        knn = self.get_knn()
        pass

    def add_letter(self):
        """Updates the current string with the new letter"""
        if os.listdir(self.input_folder) != self.current_letter + 1:
            self.string += ' '
            print(self.string)
        else:
            self.search_image()
            print(self.string)
        self.current_letter += 1

    def write_result(self):
        """Writes the final result to the output file"""
        with open(self.output_file, 'w') as f:
            f.write(self.string)
    
