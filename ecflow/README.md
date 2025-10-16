# ecFlow course 2025

[Tutorial](https://ecflow.readthedocs.io/en/latest/tutorial/tutorial.html)
[Glossary](https://ecflow.readthedocs.io/en/latest/glossary.html)
[Sources](https://github.com/ecmwf/ecflow)

```# HPC
module load ecflow

ecflow_client --host ecfg-${USER}-1 --ping
ecflow_client --host ecfg-${USER}-1 --load /${SUITE:=test} test.def
ecflow_client --host ecfg-${USER}-1 --replace /${NODE:=test} test.def
```

- in order to submit jobs on HPC, add variables in the definition file
  or on the top node with the GUI ecflow_ui

  ```# definition
     edit SCHOST hpc
     edit ECF_JOB_CMD 'troika submit -o %ECF_JOBOUT% %SCHOST% %ECF_JOB%'
     edit ECF_KILL_CMD 'troika kill -o %ECF_JOBOUT% %SCHOST% %ECF_JOB%'
     edit ECF_STATUS_CMD 'troika status -o %ECF_JOBOUT% %SCHOST% %ECF_JOB%'
```

  ```# $HOME/ecflow_servers/include/head.h
# ...
module load ecflow
```

- as_conda: a container to practice the tutorial locally
- as_debian: a container to compile ecflow and practice the tutorial locally
- as_ksh: an example of shell suite definition script following the tutorial
- notebook: a jupyter notebook to practice the tutorial with a local install
