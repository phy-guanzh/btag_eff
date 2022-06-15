exit_on_error() {
    result=$1
    code=$2
    message=$3

    if [ $1 != 0 ]; then
        echo $3
        exit $2
    fi
}
#xrdcp root://eosuser.cern.ch//eos/user/z/zguan/wwg/pyfile/cmssw_setup.sh . || exit_on_error $? 150 "Could not download sandbox1."
source /cvmfs/cms.cern.ch/cmsset_default.sh
#source cmssw_setup.sh


#sandbox_name5="sandbox-CMSSW_10_6_26-8539d32.tar.bz2"
pushd .
scramv1 project CMSSW CMSSW_10_6_29
cd CMSSW_10_6_29/src
eval `scramv1 runtime -sh`
popd 

#xrdcp root://eosuser.cern.ch//eos/user/z/zguan/www/hgc/${sandbox_name5} . || exit_on_error $? 150 "Could not download sandbox1."
#cmssw_setup $sandbox_name5 || exit_on_error $? 151 "Could not unpack sandbox"

xrdcp root://eosuser.cern.ch//eos/user/z/zguan/www/all.py . || exit_on_error $? 150 "Could not download sandbox1."
python all.py -f ${1} -y 2018 

