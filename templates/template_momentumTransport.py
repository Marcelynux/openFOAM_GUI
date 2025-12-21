momentumTransport_body = r"""/*--------------------------------*- C++ -*----------------------------------*\
  =========                 |				
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     | Website:  https://openfoam.org
    \\  /    A nd           | Version:  9                                   	
     \\/     M anipulation  |
\*---------------------------------------------------------------------------*/
FoamFile
{
    format      ascii;
    class       dictionary;
    object      momentumTransport;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

simulationType  RAS;

RAS
{{
    RASModel        kOmegaSST;

    turbulence      on;

    printCoeffs     on;

    viscosityModel  powerLaw;
    nuMax           {nuMax};    
    nuMin           8e-07;  //Wasser
    k               {k};
    n               {n};

}}

// ************************************************************************* //
"""