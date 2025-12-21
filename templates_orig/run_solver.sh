#!/bin/bash

nprocs=20
foamDictionary system/decomposeParDict -entry numberOfSubdomains -set $nprocs

decomposePar -force
#mpirun -np $nprocs renumberMesh -overwrite -noFunctionObjects -parallel | tee log.decomposepar
#mpirun -np $nprocs foamRun -parallel | tee log.solver
mpirun -np $nprocs foamRun -parallel > log.solver &
#foamMonitor -l postProcessing/residuals/0/residuals.dat 
#mpirun -np $nprocs foamPostProcess -func Q -parallel | tee log.Q
#reconstructPar