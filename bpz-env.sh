for folder in "AB" "FILTER" "SED"
do
if [ ! -d $folder ]
then
    echo "Folder $folder not found. Please make sure you are in the BPZ directory"
    exit 1
fi
done
# current directory = BPZ root directory
bpzdir=`pwd`

if [ ! $(basename $CONDA_PREFIX) = "bpz" ]
then
    echo "Not in bpz environment"
    exit 2
fi

# environment variables
activdir=$CONDA_PREFIX/etc/conda/activate.d
deactivdir=$CONDA_PREFIX/etc/conda/deactivate.d
mkdir -p $activdir
mkdir -p $deactivdir
file=$activdir/env_vars.sh
printf "export BPZDATAPATH=$bpzdir" >> $file
file=$deactivdir/env_vars.sh
printf "unset BPZDATAPATH" >> $file
# install
pip install .

