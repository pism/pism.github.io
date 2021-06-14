###### Nothing to stop WAIS deglaciation after Amundsen Sea retreat?

A [new paper in the Proceedings of the National Academy of
Sciences](http://www.pnas.org/content/early/2015/10/28/1512482112)
by J. Feldmann and A. Levermann, of the Potsdam Institute for Climate
Impact Research, uses PISM simulations to show that nearly-complete WAIS
collapse is triggered by present-day melt rates in the Amundsen Sea.
Modeled WAIS deglaciation follows after relatively-short (60--200a)
periods in which the present-day sub-shelf (i.e. ocean-caused) melt
rates are sustained.

The simulations use conservative assumptions about, and (necessarily)
modeling of, the interaction of the ice sheet with the ocean and
atmosphere. In particular, subshelf melt rates for the present ice shelf
geometry are taken from Finite Element Sea Ice-Ocean Model (FESOM)
results. These are then extended to the evolving cavity geometry by a
diffusive algorithm into regions below sea level, but with a pressure
adjustment using the ice shelf base elevation. This leads to melt rates
further inland that are similar to corresponding
present-day-cavity-geometry-induced melt rates.

In most other ways this application of PISM is as expected, though at
high (5km) resolution and using a full suite of marine ice sheet
submodels: 50ka spinup, [SIA+SSA model with plastic
till](http://dx.doi.org/10.1029/2008JF001179), [subgrid
motion of the calving
front](http://www.the-cryosphere.net/5/35/2011/tc-5-35-2011.html),
[ocean-water stress boundary condition at the calving
front](http://www.the-cryosphere.net/5/715/2011/tc-5-715-2011.pdf),
[the "eigen-calving" calving
law](http://www.the-cryosphere.net/6/273/2012/tc-6-273-2012.html),
and [an interpolated grounding
line](http://dx.doi.org/10.3189/2014JoG13J093).

The results of the simulations are most easily understood by seeing what
happens:

* fast collapse after long (200 a) melt phase
   * first 1700a of simulation:  `[`ice`` ``thinning`](http://www.pik-potsdam.de/~anders/movies/WAIS_feldmann_levermann_thinning_200yr_melt_1700yr.avi)`  `[`ice`` ``velocity`](http://www.pik-potsdam.de/~anders/movies/WAIS_feldmann_levermann_velo_200yr_melt_1700yr.avi)
   * full 10ka simulation:  `[`ice`` ``thinning`](http://www.pik-potsdam.de/~anders/movies/WAIS_feldmann_levermann_thinning_200yr_melt_10kyr.avi)`  `[`ice`` ``velocity`](http://www.pik-potsdam.de/~anders/movies/WAIS_feldmann_levermann_velo_200yr_melt_10kyr.avi)
* slow collapse after short (60 a) melt phase
   * full 15ka simulation:  `[`ice`` ``thinning`](http://www.pik-potsdam.de/~anders/movies/WAIS_feldmann_levermann_thinning_60yr_melt_13kyr.avi)`  `[`ice`` ``velocity`](http://www.pik-potsdam.de/~anders/movies/WAIS_feldmann_levermann_velo_60yr_melt_13kyr.avi)

This work appeared today, 2 November 2015. It is already featured in
commentaries at the [Washington
Post](https://www.washingtonpost.com/news/energy-environment/wp/2015/11/02/scientists-confirm-their-fears-about-west-antarctica-that-its-inherently-unstable/),
[The
Guardian](http://www.theguardian.com/world/2015/nov/02/melting-ice-in-west-antarctica-could-raise-seas-by-3m-warns-study),
and [Bloomberg Business
News](http://www.bloomberg.com/news/articles/2015-11-03/west-antarctic-s-melting-plugs-may-trigger-3-meter-rise-in-seas).
It is also featured in [Nature journal's
"<News:Explainer>"](http://www.nature.com/news/antarctic-coast-meltdown-could-trigger-ice-sheet-collapse-1.18688),
and in [Science magazine's "Latest
News"](http://news.sciencemag.org/climate/2015/11/just-nudge-could-collapse-west-antarctic-ice-sheet-raise-sea-levels-3-meters).

The last of these includes this high-level view from two well-known
students of the behavior of Amundsen Sea-sector glaciers:

> "This paper does confirm what we hypothesized, that knocking out the
Pine Island Glacier and Thwaites takes down the rest of the West
Antarctic Ice Sheet," says Ian Joughin, a glaciologist at the University
of Washington, Seattle, who co-authored last year's Science paper. He
adds, however, that the model's weakness is its [temporal] resolution;
it shows the destabilization of the glaciers occurring roughly 60 years
from now, whereas present observations suggest that collapse is already
underway. As a result, Joughin says, the model's time scale for the
collapse is probably too long. "It's more likely measured in centuries
rather than millennia."

> Indeed, "the jury is still out" on whether Feldmann and Levermann's
study got the time scale right, [Eric] Rignot [of the University of
California, Irvine] says. The long-term evolution of an ice sheet "is a
very complex modeling problem. Some of the variables controlling the
models are not all that well known," he adds, including forces such as
winds, ocean circulation, and how icebergs calve. "There is not a model
out there that is getting it right, because they all have caveats. I
think the discussion is ongoing, and is only going to be more
interesting with time."
