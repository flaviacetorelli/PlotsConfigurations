# example of configuration file

tag = '2016_cr'
outputDir = 'rootFile'
treeName = 'Events'

# luminosity to normalize to
lumi = 35.9

# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'variables.py' 

# file with list of cuts
cutsFile = 'cuts.py' 

# file with list of samples
samplesFile = 'samples.py' 

# file with list of plot
plotFile = 'plot.py'

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = '/eos/user/f/fcetorel/www/VBS_OS/test/2016/low_mjj'
# nuisances file for mkDatacards and for mkShape
#nuisancesFile = 'nuisances.py'
