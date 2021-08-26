#!/bin/bash

hostname
PV_PATH='/gpfs/alpine/proj-shared/cmb124/Paraview/ParaView-5.8.1-osmesa-MPI-Linux-Python3.7-64bit/bin'
if  [ "$1" = "" ]; then
  echo
  echo 'Usage: '
  echo -e '\t run_vis.sh first_frame last_frame'
  echo
  exit 0
fi 

for i in $(eval echo {$1..$2})
do
  echo 'Frame ' $i
  date
  #${PV_PATH}/pvbatch --force-offscreen-rendering preViz_slice_vel_temp.py $i
  ${PV_PATH}/pvbatch --force-offscreen-rendering everest/viz_iso_EQN_TRANS_multiview_step_pv5.8.1.py $i $3 $4
  date
  #sleep 4m
done
