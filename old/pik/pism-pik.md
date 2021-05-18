# PIK developers and the PISM-PIK model

{=mediawiki}
{{:ant_m5ka_10km_csurf.png?330 }}

## Investigators

* [Prof. Anders Levermann](http://www.pik-potsdam.de/~anders)
  [levermann@pik-potsdam.de](levermann@pik-potsdam.de)
* [Dr. Torsten Albrecht](https://www.pik-potsdam.de/members/albrecht)
  [albrecht@pik-potsdam.de](albrecht@pik-potsdam.de)
* Marianne Haseloff
* [Dr. Maria Martin](http://www.pik-potsdam.de/~martin)
  [martin@pik-potsdam.de](martin@pik-potsdam.de)
* [Dr. Mattias Mengel](http://www.pik-potsdam.de/~mengel)
  [matthias.mengel@pik-potsdam.de](matthias.mengel@pik-potsdam.de)
* [Dr. Ricarda Winkelmann](http://www.pik-potsdam.de/~ricardaw)
  [winkelmann@pik-potsdam.de](winkelmann@pik-potsdam.de)
* [Johannes Feldmann](http://www.pik-potsdam.de/~johfeld)
  [johfeld@pik-potsdam.de](johfeld@pik-potsdam.de)

Processes like ice shelf calving and stress boundary conditions are
important parts of marine ice sheet models, and sea level projections,
due to their effect on the dynamics upstream of the grounding line.
Developers at the Potsdam Institute for Climate Impact Research (PIK),
Germany, introduced modifications of PISM ice shelf and grounding-line
dynamics with a special focus on modeling the Antarctic ice sheet-shelf
system.

Specifically, these PIK developers created the Potsdam Parallel Ice
Sheet Model, PISM-PIK, in 2008--2009 as a derived class of PISM
stable0.2. After joint work with [UAF developers](:about),
changes were made to the PISM base model in spring 2011 so that PISM-PIK
capabilities were part of the stable0.4 release. These capabilities are
now an integral part of PISM itself, and appear in the current and all
future releases.

PIK-added features and applications include:

* changes to the hybrid dynamics, transport schemes, and the
  calving-front stress boundary condition [(Winkelmann et al.
  2011)](:publications#section2011), relative to content in [(Bueler
  and Brown, 2009)](:publications#section2009),
* a mass transport parameterization at the calving front, enabling its
  proper motion [(Albrecht et al. 2011)](:publications#section2011),
* a physically-motivated 2D calving law [(Winkelmann et al.
  2011)](:publications#section2011), [(Levermann et al.
  2012)](:publications#section2012),
* improved parameterization of the grounding line [(Feldmann et al.
  2014)](:publications#section2014), and
* a model for fracture density in ice shelves [(Albrecht and Levermann
  2012)](:publications#section2012), [(Albrecht and Levermann
  2014a)](:publications#section2014).

After adding capabilities to PISM, PIK then published these major
modeling applications:

* a dynamic equilibrium simulation for present-day boundary conditions
  reproduces observed dynamical features of the Antarctic sheet-shelf
  system [(Martin et al. 2011)](:publications#section2011),
* a model of the dynamic effect of snowfall in Antarctica [(Winkelmann
  et al. 2012)](:publications#section2012),
* simplified models based on analysis of PISM model ensembles
  [(Winkelmann and Levermann 2013)](:publications#section2013),
  [(Levermann et al. 2014)](:publications#section2014),
* a model of ice shelf neighbor dynamical interactions [(Albrecht and
  Levermann 2014b)](:publications#section2014), and
* a scenario for basin-wide retreats in East Antarctica [(Mengel and
  Levermann 2014)](:publications#section2014).

Here are three topical pages describing work using and developing PISM
at PIK:

* [Antarctica in PISM](http://www.pik-potsdam.de/~anders/Antarctica.html)
* [Sea level changes in PISM](http://www.pik-potsdam.de/~anders/SeaLevel.html)
* [Iceberg calving in PISM](http://www.pik-potsdam.de/~anders/IcebergCalving.html)
