import numpy as np
import os
import argparse


def file_len(filename):
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def sample(population_file, sampling_file, population_size, sampling_size):
    sample_lines = np.random.choice(xrange(population_size), size=sampling_size)
    print("Population size {}".format(population_size))

    with open(sampling_file, 'w') as f:
        pop_reader = open(population_file)
        if args.header:
            f.write(pop_reader.readline())
        for i, line in enumerate(pop_reader):
            if i in sample_lines:
                f.write(line)

if __name__ == "__main__":

    np.random.seed(12345)
    parser = argparse.ArgumentParser(description='Sample a file using Reservoir Sampling.')
    parser.add_argument('datapath', help='file to be sampled')
    parser.add_argument('samplepath', help='output file')
    parser.add_argument('size', type=int, help='output file')
    parser.add_argument('header', type=bool, help='should write the header on the output file')
    args = parser.parse_args()

    pop_file = args.datapath
    sample_file = args.samplepath
    population = file_len(pop_file)
    sample_size = args.size
    sample(pop_file, sample_file, population, sample_size)