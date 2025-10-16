# ecFlow python notebook

## from HPC

`[ ! -f $HOME/.ecinteractiverc ] && $HOME/.ecinteractiverc <<\!!
module --help > /dev/null && module load python3 && module load ecflow/5.15.0 && module load ecmwf-toolbox && module load troika && module load git;
h=ecflow-gen-$USER-001; ping -c 1 $h && export ECF_HOST=$h || :
h=ecfg-$USER-1; ping -c1 $h && ecflow_client --host $h --ping && export ECF_HOST=$h || :
!!
/usr/local/bin/ecinteractive -j
`
## 
