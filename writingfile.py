import random

SAMPLES_FILE = 'samples.txt'


def main():
    """ Call generate_random_samples with the range of samples to generate
    (low, high), as well as the quantity of samples to produce """
    generate_random_samples(0, 10, 100)
    

#i understand that there is an error with the type that is trying to be added to the outfile
def generate_random_samples(low, high, samples):
    """ Generate the quantity of random integer samples in the range 
    specified (low, high) and write to text file """
    
    try:
        out_file = open(SAMPLES_FILE, 'w')
        #changed this part of the code!!!
        ###
        for num in range(0,100):
            val = random.randint(0,10)
            value = str(val)
        ####
            out_file.write(value + '\n')
        out_file.close()
    except IOError:
        print('Error opening file.')
    except ValueError:
        print('Invalid values provided.')
    except TypeError:
        print('Error writing samples to file.')
    else:
        print('Success: Data written to file.')


if __name__ == '__main__':
    main()


