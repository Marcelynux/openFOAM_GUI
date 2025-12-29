MRFProperties_body = r"""/*--------------------------------*- C++ -*----------------------------------*\
  =========                 |				
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     | Website:  https://openfoam.org
    \\  /    A nd           | Version:  11                                   	
     \\/     M anipulation  |
\*---------------------------------------------------------------------------*/
FoamFile
{{
    format      ascii;
    class       dictionary;
    object      MRFProperties;
}}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //


{mixer_definition}


// ************************************************************************* //
"""

MRFProperties_mixer_element = r"""{zone}
{{

    cellZone    cell_{mixer_name};
    active      yes;


    origin    ({x_origin} {y_origin} {z_origin});
    axis      ({x_axis} {y_axis} {z_axis});

    rpm       {rpm};

}}"""