###### Greenland outlet glacier flow modeled the right way

Today\'s publication of [Aschwanden et al.
(2016)](http://dx.doi.org/10.1038/ncomms10524) in [Nature
Communications](http://www.nature.com/ncomms/) is certainly a
milestone in PISM development. However, it is also a milestone in ice
sheet modeling generally. Here\'s why.

The paper is based on PISM simulations with grid resolution down to 600
m over the entire Greenland ice sheet. To start, each of an initial
ensemble of 14 lower-resolution (1500 m) experiments has a single
ice-sheet-wide value for all parameters. The best of these, in an
ice-sheet-wide measure, is re-run at the 600 m resolution and various
coarser resolutions. The quality of this flow model for 29 outlet
glaciers is assessed; //each outlet glacier sees the same physics//. The
main result is that the majority of the outlet glaciers show strong
correlation between modeled and present-day-observed velocity, when it
is compared along cross-flow and near-ocean profiles.

Before this paper one might suppose, based on the most prominent
literature on the subject, that a detailed, measurably-accurate,
outlet-glacier-resolving model of the present-day velocity of an entire
ice sheet was dependent both on removing shallow assumptions from the
stress balance //and// on tuning a very large number of basal
parameters. Both of these \"required\" properties would be very bad news
for the prospect of using ice sheet simulations to do science! On the
one hand, Stokes models are computationally-expensive, while on the
other hand only present-day, and //not// past or future, data are
available to set all these basal parameters through inversion.

Such a pessimistic view turns out to be substantially false. [Aschwanden
et al. (2016)](http://dx.doi.org/10.1038/ncomms10524) show
that four things //do// matter: //(i)// an accurate map of bedrock
topography, //(ii)// a stress regime in which viscous membrane stresses
are part of the balance with basal sliding resistance, //(iii)// an
energy-conservation-driven basal stress model derived (conceptually)
from a model of a wet, pressurized, deformable basal layer, and //(iv)//
high model resolution over all areas of the ice sheet where sliding is
possible and/or steep/rough basal topography exists.

NASA IceBridge missions, and the mass-conserving-bed technology of
Morlighem et al (2014), are shown by this paper to represent major
progress on item //(i)//. Items //(ii)// and //(iii)// are properties of
the PISM continuum model, and item //(iv)// of its implementation as
parallel-scalable software. Certainly all of these \"things that
matter\" are improvable. More-complete stress balances and the use of
inversion of present-day velocities will both be essential to
improvements. The main idea remains, however: if the modeled flowing ice
has the right bottom geometry, and if the dynamical model has certain
key features, then the resulting dynamics are already inside the
ballpark!

This research has been
[featured](http://www.adn.com/article/20160203/uaf-researchers-new-model-predicts-flow-greenlands-glaciers)
in Alaska\'s largest newspaper, the [Alaska Dispatch
News](http://www.adn.com/).
