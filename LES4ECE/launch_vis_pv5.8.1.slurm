#!/bin/bash

#SBATCH -A CMB124
#SBATCH -J viz
#SBATCH -N 1
#SBATCH -o viz_gEqnPlusKinetics_b1_14_b3_6_LES_map_b1_14_cycle1.o%J
#SBATCH -e viz_gEqnPlusKinetics_b1_14_b3_6_LES_map_b1_14_cycle1.o%J
#SBATCH -t 01:00:00

cd $SLURM_SUBMIT_DIR

./run_vis_osmesa_pv5.8.1.sh $initFrame $endFrame 1920 1080 gEqnPlusKinetics_b1_14_b3_6_LES_map_b1_14_cycle1


