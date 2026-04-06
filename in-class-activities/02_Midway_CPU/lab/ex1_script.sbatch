#!/bin/bash

#SBATCH --job-name=mpi
#SBATCH --output=mpi.out
#SBATCH --ntasks=4
#SBATCH --partition=amd
#SBATCH --account=macs30113

module load python/anaconda-2022.05 mpich/3.2.1

mpirun python ./mpi_rand_walk.py