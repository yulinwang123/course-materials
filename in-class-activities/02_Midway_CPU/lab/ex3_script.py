from mpi4py import MPI
import numpy as np
import time

def simple_square_parallel():
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    numbers = None
    if rank == 0:        
        t0 = time.time()
        np.random.seed(rank)
        numbers = np.linspace(1, 100, 100)
    
    # Split up numbers and send equal work to each process
    # via a MPI communication (stored in an array `sub_numbers`)
    # YOUR CODE HERE

    squared_sub_numbers = np.square(sub_numbers)

    # Collect all of the values in `squared_sub_numbers` and
    # send back to rank 0 via a MPI communication
    # YOUR CODE HERE

    if rank == 0:
        max_index = np.argmax(all_squared_numbers)
        max_square = all_squared_numbers[max_index]
        original_number = numbers[max_index]
        elapsed_time = time.time() - t0

        print("Original number with max square:", original_number)
        print("Max square:", max_square)
        print("Computation time:", elapsed_time)

if __name__ == '__main__':
    simple_square_parallel()