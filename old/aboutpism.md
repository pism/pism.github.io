\~\~NOTOC\~\~

###### What does PISM do? {#what_does_pism_do}

What is the Parallel Ice Sheet Model for? If you are working in climate
science or the physics of glaciers then you have a sense of what an
\"ice sheet model\" does. But if you are not a scientist, or need the
very basics of ice sheets, these questions and answers might help.

#### What does an ice sheet model do? {#what_does_an_ice_sheet_model_do}

Ice sheets, which are just big, continent-size glaciers, are moving ice
fluids, like the ocean is a fluid and the atmosphere is a fluid.
Glaciers flow downhill, driven by gravity. PISM simulates the movement
of the ice fluid, and its temperature, and so on, just as a weather
forecasting model simulates the atmosphere. Scientists are interested in
how changing climate might affect the ice flow. Ice moves slower than
the ocean or the atmosphere, so they use PISM to simulate decades,
centuries, or millenia of flow, while a weather model works over just
days.

See this [excellent 5 minute
movie](http://imaginary.org/film/the-future-of-glaciers)
introducing what a glacier flow model does. The model shown is not PISM
but a new glacier-scale model by Guillaume Jouvet. PISM does this kind
of thing too, but for each part of a big ice sheet like Greenland or
Antarctica.)

#### Why is it important? {#why_is_it_important}

Ice sheets in Greenland and Antarctica are more than two miles (more
than four kilometers) thick and sitting on land. They contain a large
amount of (frozen) water which is currently above sea level. Note that
ice sheets are not sea ice\-\--sea ice is already floating and changing
its thickness will not change sea level directly.

If ice sheets flow faster or slower, or their flow direction changes,
then this affects the rate at which they can raise sea level. The
potential amount is big\-\--tens of meters\-\--but the question is how
fast these changes can happen. In the past, as the earth went in and out
of the ice ages, there were huge changes over very short periods. In the
future there could be tipping points we don\'t see now. An ice sheet
flow model like PISM is part of understanding such possibilities.

If present-day Antarctic ice sheet flows faster into the ocean during
the next century then sea level will rise. There may be other
relatively-fast effects on the climate. One question is whether sea
level will rise a only a fraction of a meter, or up to one or two
meters, in the next century.

A major part of predicting the ice sheets is to observe them better now
through field work. Computer simulations depend on observations; they
can can only integrate the data we have into a more complete picture,
and they do not create new facts.

#### Are you formally collaborating with international partners? {#are_you_formally_collaborating_with_international_partners}

We have written software which is free and open source. Our
international partners, like the Potsdam Institute (PIK) and other
groups in Denmark, Germany, New Zealand, and the Netherlands, use our
software, and they even add to it. The collaboration is not very formal,
but we have traveled both ways across the pole quite a bit! They have
chosen PISM over the several other available ice sheet models because it
works well for them.

#### What have researchers discovered since adopting the model? {#what_have_researchers_discovered_since_adopting_the_model}

At UAF and PIK we have contributed estimates of the amount of sea level
change coming from changes to the Greenland and Antarctic ice sheets
using PISM. These estimates will be combined into the next report of the
Intergovernmental Panel on Climate Change, which will appear next year
after an extensive evaluation of the current science, including these
model-based estimates. But at UAF we are mostly building the model and
writing code, and trying to understand the physics of glaciers and ice
sheets.

------------------------------------------------------------------------

//In preparation for a radio interview about [a news
item](news:euro_pism), reporter Ariel van Cleave of [KDLG,
Dillingham, Alaska](http://kdlg.org/) asked [Ed
Bueler](about) the above questions, and the above were his
//DRAFT// replies. What he actually was recorded as saying was
different, at least in detail. Hopefully he did not make a big fool of
himself \...//

###### What has PISM been used for? {#what_has_pism_been_used_for}

PISM has been used for modeling every present-day ice sheet (Greenlandic
and Antarctic), many paleo-ice sheets, and many glaciers.

` * The `[`PISM`` ``User's`` ``Manual`](http://www.pism-docs.org/sphinx/manual)` shows some realistic and idealized cases.`\
` * The `[`publications`` ``page`](publications)` shows published applications of PISM from hundreds of different scientists all over the world.`
