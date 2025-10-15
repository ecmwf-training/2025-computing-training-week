#### Links:
- [Online training course: Introduction to ECMWF computing services (including MARS)](https://events.ecmwf.int/event/480/overview)
- [Exercise files](https://sites.ecmwf.int/repository/opencharts-sample-data/2025_computing/)
- [GitHub repo for training](https://github.com/ecmwf-training/2025-computing-training-week)
- [ecCodes releases](https://github.com/ecmwf/eccodes/releases)
- [ecCodes documentation](https://confluence.ecmwf.int/display/ECC)
- [ECMWF Open Data Portal](https://data.ecmwf.int/)
- [Dissemination File-naming convention](https://confluence.ecmwf.int/display/DAC/File+naming+convention+and+format+for+real-time+data)

#### Preliminaries
```bash
# In order to copy exercise files to your $SCRATCH, on ATOS HPC do the following:
$ cd $SCRATCH
$ tar -xvf /home/trx/grib_decoding.tar
$ cd grib_decoding/demo
# or access online:
# https://sites.ecmwf.int/repository/opencharts-sample-data/2025_computing/
```

```bash
# contents
$ ll
20251012000000-114h-enfo-cf.grib2
A1S10071800100815001
nvo_x1_aifs-single_ai_oper_fc_20251011T060000Z_20251011T120000Z_6h
output.grib1
python_eccodes.py
```

#### Installing on ATOS HPC and locally
```bash
# On ATOS HPC
$ module load ecmwf-toolbox/new
$ codes_info
ecCodes Version 2.44.0
Default definition files path is used: /MEMFS/definitions
Definition files path can be changed by setting the ECCODES_DEFINITION_PATH environment variable.
Default samples path is used: /MEMFS/samples
Samples path can be changed by setting the ECCODES_SAMPLES_PATH environment variable.

$ which grib_ls
```

Local:
```bash
# Install locally via conda-forge
$ conda install -c conda-forge eccodes
# or
$ conda create -n eccodes_grib_training eccodes cfgrib earthkit-data earthkit-geo earthkit-utils xarray

# Install locally via PyPI
$ pip install eccodes
```

#### ecCodes Introduction commands
- ecCodes is available in C, Fortran 90, and Python APIs.

```bash
# Basic help
$ grib_ls
$ grib_ls 20251012000000-114h-enfo-cf.grib2
$ grib_ls A1S10071800100815001
$ grib_ls output.grib1
$ grib_ls -p paramId 20251012000000-114h-enfo-cf.grib2
$ grib_ls -P paramId 20251012000000-114h-enfo-cf.grib2

# Namespaces
$ grib_ls -n mars output.grib1
statistics
parameter
	data
	geography
	ls
	time
	vertical

$ grib_ls -p centre,dataDate,shortName,paramId,typeOfLevel,level 20251012000000-114h-enfo-cf.grib2
$ grib_ls -w shortName=t 20251012000000-114h-enfo-cf.grib2
$ grib_ls -w level=0 20251012000000-114h-enfo-cf.grib2
$ grib_ls -w count=3 20251012000000-114h-enfo-cf.grib2
$ grib_ls -j output.grib1
```

```bash
# grib_dump
$ grib_dump 20251012000000-114h-enfo-cf.grib2
# WMO Octet mode
$ grib_dump -O 20251012000000-114h-enfo-cf.grib2 
$ grib_dump -O -w shortName=t 20251012000000-114h-enfo-cf.grib2
```

```bash
# grib_get_data
$ grib_get_data output.grib1
$ grib_get_data -F "%.4f" output.grib1 | head -n 10
$ grib_get_data -F "%.4f" -w stepRange=0 output.grib1 | head -n 10
```

```bash
# CodesUI (standalone interactive tool)
# CodesUI allows inspection of the overall structure of GRIB and BUFR files
# and examination of data and metadata of individual messages
# (available for x64 CPUs, run it on VDI)
```

---

#### Second Part of the demo
```bash
# grib_copy
$ grib_copy -w edition=1 A1S10071800100815001 edition1.grib
$ grib_copy -w edition=2 A1S10071800100815001 edition2.grib
$ grib_ls edition1.grib edition2.grib
$ cat edition1.grib edition2.grib > edition1+2
$ grib_ls edition1+2

$ grib_copy A1S10071800100815001 "A1S10071800100815001_[shortName]"
$ grib_ls -p shortName A1S10071800100815001_*

$ grib_ls A1S10071800100815001
$ grib_copy -w count=3 A1S10071800100815001 3.grib
```

```bash
#grib_set
$ grib_set -s date=17751017,stepRange=9999 nvo_x1_aifs-single_ai_oper_fc_20251011T060000Z_20251011T120000Z_6h time_travel.grib2
$ grib_ls time_travel.grib2

$ grib_ls nvo_x1_aifs-single_ai_oper_fc_20251011T060000Z_20251011T120000Z_6h
$ grib_set -w shortName=t -s shortName=pt nvo_x1_aifs-single_ai_oper_fc_20251011T060000Z_20251011T120000Z_6h out_pt.grib2
$ grib_ls out_pt.grib2
$ grib_ls -w shortName=pt -n parameter out_pt.grib2
```

```bash
# grib_to_netcdf
$ grib_copy -w count=1 20251012000000-114h-enfo-cf.grib2 1.grib
$ grib_to_netcdf -o out1.nc 1.grib
$ ncdump out1.nc | head -n 60
```

```bash
# Python
$ module load python3
$ cd ../python
$ cat eccodes_demo.py
$ python3 eccodes_demo.py
```
