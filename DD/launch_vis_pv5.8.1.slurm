#!/bin/bash

#SBATCH -A CMB124
#SBATCH -J viz
#SBATCH -N 1
##SBATCH -p gpu
#SBATCH -o viz.o%J
#SBATCH -e viz.e%J
#SBATCH -t 01:00:00

cd $SLURM_SUBMIT_DIR

./run_vis_osmesa_pv5.8.1.sh $initFrame $endFrame 1920 1080


