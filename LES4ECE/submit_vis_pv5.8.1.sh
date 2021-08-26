#!/bin/bash

export initFrame=48
export endFrame=65
sbatch launch_vis_pv5.8.1.slurm

export initFrame=66
export endFrame=83
sbatch launch_vis_pv5.8.1.slurm

export initFrame=607
export endFrame=620
sbatch launch_vis_pv5.8.1.slurm

export initFrame=621
export endFrame=637
sbatch launch_vis_pv5.8.1.slurm
