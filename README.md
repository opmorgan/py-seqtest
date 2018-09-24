# py-seqtest

Task for evaluating sequencing ability in cerebellar ataxia. Task and stimuli are adapted from Leggio et al., 2008. [1]



## Installation

### Windows / macOS / Linux

Pre-compiled binaries are available for Windows, macOS, and Linux. You can download them [here](https://gitlab.com/ojjo/py-seqtest/tags/v0.1.1).

### From Source

> py-seqtest requires Python ^3.6. Be sure you have it installed before performing the steps below. 

1. Install dependencies with pip.

```bash
$ pip install pygame && pip install pyinstaller

```

2. Run / Build

```bash
# Run for development: 
$ python main.py 

# Build binary for your system: 
$ pyinstaller seqtest.spec 
```

## Administration
Instructions for administration are detailed in SOP.txt.


[1]: Leggio MG, Tedesco AM, Chiricozzi FR, Clausi S, Orsini A, Molinari M. Cognitive sequencing impairment in patients with focal or atrophic cerebellar damage. Brain. 2008 Mar 11;131(5):1332-43.
