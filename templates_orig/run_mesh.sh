#!/bin/bash

nprocs=20
foamDictionary system/decomposeParDict -entry numberOfSubdomains -set $nprocs

foamCleanTutorials
rm -rf 0 > /dev/null 2>&1
cp -r 0_org 0 > /dev/null 2>&1

surfaceFeatures
blockMesh
decomposePar
mpirun -np $nprocs snappyHexMesh -parallel -overwrite | tee log.shm

#reconstructPar -mergeTol 1e-06 -constant
reconstructPar -constant

checkMesh | tee log.checkmesh

touch foam.foam
