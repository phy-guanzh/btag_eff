# Btag-Eff Calculation

##Step1:
fix condor_for_postproc.py datasets part, change the samples you want.

in condor_for_postproc.py, it import the Das search python file to search all the data samples
root files to submit. the files path name will be stored in 
"filepath_"+args.name+"_"+args.year+".txt" 

##Step2:
then, fix condor_for_postproc.py "prepare submit code" part.
prepare submit code one by one.

##Step3: 
then, fix condor_for_postproc.py "prepare shell" part.
prepare shell to be consistent with wrapper.sh.

##Step4:
hadd all output files

##Step5:
use eff.py to plot btag-eff plot
