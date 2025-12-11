#!/bin/bash

foamPostProcess -solver incompressibleFluid -func forcesIncompressible | tee log.Schub 
foamPostProcess -func triSurfaceVolumetricFlowRate | tee log.Umwälzmenge
foamPostProcess -func triSurfaceAverage | tee log.Austrittsgeschwindigkeit