# DESC_BPZ: 

Original Bayesian Photometric Redshifts (BPZ) by Narciso Benítez and Dan Coe, 
updated as described below by the LSST-DESC PZ Working Group. This version 
incorporates minor improvements mainly on the user interface.

To install first create a ``conda`` environment called ``bpz`` and activate it:
```python
conda create -n bpz python
conda activate bpz
```
and then run the ``bpz-env.sh`` script:
```bash
sh bpz-env.sh
```

If you do not want to use a ``conda`` environment then follow the steps listed in 
the original README below.


Original README
---------------

This repo contains a python3 port of the popular BPZ software package 
(https://www.stsci.edu/~dcoe/BPZ/).  The code was modified from the original 
bpz-1.99.3 version available at the given URL, upgraded to be python3 
compatible, and modified to read and write hdf5 files rather than straight 
ascii.  The code is messy in many places, having gone through multiple 
iterations by multiple authors.  No promises are made as to functionality of 
multiple subsystems (e.g. plotting), so use with caution!

If you use this code, please cite [Benitez 
(2000)](https://ui.adsabs.harvard.edu/abs/2000ApJ...536..571B/abstract) and [Coe 
et al. (2006)](https://ui.adsabs.harvard.edu/abs/2006AJ....132..926C/abstract).

In order to run, you should set the environment variable<br>

`BPZDATAPATH` to point to the directory housing the SED, FILTER, and AB files.
<br>

To run traditional command-line `BPZ` use the `bpz.py` file in `scripts`, 
e.g.:<br> `python scripts/bpz.py yourasciicatalog.cat -P yourparameterfile.pars` 
<br> Dan Coe's STScI webpage listed above contains a nice BPZ user guide, for 
more detail on running the code, please check that website.<br>.

However, this package will mainly be used as a library for running "bpz_lite" in 
the DESC PZ RAIL Package, see:<br> https://github.com/LSSTDESC/RAIL
