---
title: Citing PISM
subtitle: How to reference PISM?
layout: page
hero_height: is-medium
hero_image: https://images.unsplash.com/photo-1591792111137-5b8219d5fad6
hero_caption: "Photo: <a href='https://unsplash.com/photos/WKp-NWSGWjQ'>J. Eades / Unsplash</a>"
hero_darken: false
show_sidebar: true
---

# Acknowledging PISM funding sources

If you use PISM in a publication then we ask for an acknowledgement of funding and a citation. However, unless PISM developers are involved in the preparation of the publication at the usual co-author level, we do not expect co-authorship on PISM-using papers.

To acknowledge PISM funding please include the statement:

> Development of PISM is supported by NASA grants 20-CRYO2020-0052 and 80NSSC22K0274 and NSF grant OAC-2118285.

## Citing PISM

To cite PISM please use at least one of [Bueler and Brown (2009)](https://doi.org/10.1029/2008JF001179) or [Winkelmann et al. (2011)](https://doi.org/10.5194/tc-5-715-2011), below, as appropriate to the application.

If your results came from source code modifications to PISM then we request that your publication say so explicitly.

If your study relies heavily on certain PISM sub-models (such as hydrology, calving, fracture mechanics, thermodynamics) please contact the corresponding author/developer for information on additional citations.

```
@article {BuelerBrown2009,
  AUTHOR = {E. Bueler and J. Brown},
   TITLE = {Shallow shelf approximation as a "sliding law" in a
            thermodynamically coupled ice sheet model},
 JOURNAL = {J. Geophys. Res.},
  VOLUME = {114},
     DOI = {10.1029/2008JF001179},
    YEAR = {2009},
   PAGES = {F03008},
     URL = {https://doi.org/10.1029/2008JF001179},
}
```

```
@article {Winkelmannetal2011,
  AUTHOR = {Winkelmann, R. and Martin, M. A. and Haseloff, M. and Albrecht, T.
            and Bueler, E. and Khroulev, C. and Levermann, A.},
   TITLE = {The Potsdam Parallel Ice Sheet Model (PISM-PIK)
            Part 1: Model description},
 JOURNAL = {The Cryosphere},
  VOLUME = {5},
     DOI = {10.5194/tc-5-715-2011},
    YEAR = {2011},
   PAGES = {715--726},
     URL = {https://doi.org/10.5194/tc-5-715-2011},
}
```

Please see [ACKNOWLEDGE.rst](https://github.com/pism/pism/blob/main/ACKNOWLEDGE.rst) and [funding.csv](https://github.com/pism/pism/blob/main/doc/funding.csv) for a list of grants supporting PISM development.