import numpy as np


def convolve_1d(kernel, reference, boundary = 'none'):

    convolution = list()
    flipped = kernel[-1::-1]
    if boundary == None or boundary =='none':
        for i in range(len(reference)-len(kernel)+1):
            convolution.append( np.sum(flipped*reference[i:i+len(kernel)]) )
    elif boundary == 'zero_pad':
        ## less memory efficient, but fine for a beginner like me 
        ## might want to look into how they implement the convolution in the space 
        ## in these public libraries
        reference = np.hstack( (np.zeros(len(kernel) -1 ),  reference, np.zeros(len(kernel) -1 ) )  ) 
        for i in range(len(reference) - len(kernel) -1):
            convolution.append( np.sum(flipped*reference[i:i+len(kernel)]) )
    elif boundary == 'periodic':
        for i in range(len(reference)):
            convolution.append( np.sum(flipped*reference[i:i+len(kernel)]) )
    return convolution

if __name__ == '__main__':

    boundary = 'zero_pad'
    kernel = [0, 1, 2]
    kernel = np.array(kernel)
    print(f'Kernel is: {kernel}, shape: {kernel.shape}.')

    reference = [1, 3 ,4 ,4 ,5 ,5, 6, 7, 0]
    reference = np.array(reference)
    print(f'reference is: {reference}, shape: {reference.shape}.')

    convolution_result = convolve_1d(kernel, reference, boundary)
    print(f'The result of the convolution is: {convolution_result}, shape = {len(convolution_result)}')