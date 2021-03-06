# example of configuration file
tag = 'WH_3l_2017nano_HTXS1p1'

treeName= 'Events'

# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'variables.py'

# file with list of cuts
cutsFile = 'cuts.py'

# file with list of samples
samplesFile = 'samples.py'

# file with plot configuration
plotFile = 'plot.py'

# luminosity to normalize to (in 1/fb)
lumi = 41.86

# structure file for datacard
structureFile = 'structure.py'

# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'

# used by mkShape to define output directory for root files
outputDir = 'rootFiles_'+tag

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = 'plot_'+tag

# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards_'+tag
