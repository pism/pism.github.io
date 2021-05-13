###### PISM stable0.3 is released {#pism_stable0.3_is_released}

PISM version *stable0.3* is available. See the [stable version
page](:stable_version) to check out a copy of the source
code. Send email to [help\@pism-docs.org](help@pism-docs.org)
for help with any version of PISM.

Compared to *stable0.2*, the new version

` * uses a polythermal, enthalpy-based energy conservation scheme`\
` * includes improved atmosphere, surface processes and ocean model structure`\
` * puts all model parameters and physical constants in a configuration file which can be changed without re-compiling PISM`\
` * has a better ``{{:manual.pdf|User's Manual}}`{=mediawiki}\
` * comes with a command-line option ``{{:cheatsheet.pdf|Cheat-Sheet}}`{=mediawiki}\
` * has a better HTML ``{{http://www.pism-docs.org/doxy/html/index.html|PISM Source Code Browser}}`{=mediawiki}\
` * supports saving scalar, 2D and 3D diagnostics at given times during the run`\
` * allows climate forcing using spatially-varying "anomalies" (near-surface air temperature and precipitation)`\
` * includes better metadata handling`\
` * can be stopped and restarted without affecting results of a run`\
` * has more software tests (including regression tests)`\
` * has an automatic vertical grid extension mechanism`\
` * performs area and volume calculations using WGS84 datum to correct projection error`\
` * makes the computation of the age of the ice optional, for efficiency`\
` * has easier-to-extend source code`\
` * comes with three worked examples: `[`Antarctica`](:worked-searise-antarctica-uaf)`, `[`Greenland`](:worked-searise-greenland)`, `[`Storglaciaren`](:worked-storglaciaren)
