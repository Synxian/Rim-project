import os
import numpy
import scipy
from operator import itemgetter
from common import angulos_por_zona

class Searcher:
    """Class that handles the letter search and writes the final result"""
    def __init__(self):
        self.string = ''
        self.current_letter = 0
        self.input_folder = 'inputs'
        self.output_file = 'output.txt'
        self.k = 3
        self.micro_descriptors = self.get_dataset_descriptors('descriptors_micro')
        self.small_descriptors = self.get_dataset_descriptors('descriptors_small')
        self.knn = []

    def get_dataset_descriptors(self, directory):
        """load saved descriptors to a dict"""
        data = {}
        for folder in os.listdir(directory):
            descriptor = numpy.load(f'{directory}/{folder}/descriptores.npy')
            data[folder] = descriptor
        return data

    def get_knn(self):
        """Gets the k nearest neighbors"""
        self.current_descriptor = angulos_por_zona(f'{self.input_folder}/letter_{self.current_letter}.jpg')
        for key, value in self.micro_descriptors.items():
            matriz_distancias = scipy.spatial.distance.cdist([self.current_descriptor], value, metric='cityblock')
            min_idx = numpy.argmin(matriz_distancias)
            if len(self.knn) <= 3:
                self.knn.append((key, matriz_distancias[0][min_idx]))
            else:
                arg_mx = max(self.knn, key=itemgetter(1))
                if arg_mx[1] > matriz_distancias[0][min_idx]:
                    max_ind = self.knn.index(arg_mx)
                    self.knn[max_ind] = (key, matriz_distancias[0][min_idx])

    def search_image(self):
        """Compare image descriptors to get new letter"""
        self.get_knn()
        current_result = ('', numpy.Inf)
        for folder, _ in self.knn:
            matriz_distancias = scipy.spatial.distance.cdist(
                [self.current_descriptor], self.small_descriptors[folder], metric='cityblock'
            )
            min_idx = numpy.argmin(matriz_distancias)
            if current_result[1] > matriz_distancias[0][min_idx]:
                current_result = (folder, matriz_distancias[0][min_idx])
        self.string += current_result[0].lower()

    def add_letter(self, space = False):
        """Updates the current string with the new letter"""
        if space:
            self.string += ' '
            print(self.string)
        else:
            self.search_image()
            print(self.string)
        self.current_letter += 1
        self.knn = []

    def save_output(self):
        """Writes the final result to the output file"""
        with open(self.output_file, 'w') as f:
            f.write(self.string)
