# py-seqtest

Task for evaluating sequencing ability in cerebellar ataxia, used in Morgan et al. (2021) [1]. Task and stimuli are adapted from Leggio et al. (2008) [2].



## Installation

### Windows 

Pre-compiled binaries are available for Windows. You can download them [here](https://gitlab.com/ojjo/py-seqtest/tags/v0.1.2).

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
Instructions for administration are detailed in SOP.pdf.

## References
1. Morgan, O. P., Slapik, M. B., Iannuzzelli, K. G., LaConte, S. M., Lisinski, J. M., Nopoulos, P. C., Cochran, A. M., Kronemer, S. I., Rosenthal, L. S., & Marvel, C. L. (2021). The cerebellum and implicit sequencing: Evidence from cerebellar ataxia. The Cerebellum, 20(2), 222–245. https://doi.org/10.1007/s12311-020-01206-7

2. Leggio, M. G., Tedesco, A. M., Chiricozzi, F. R., Clausi, S., Orsini, A., & Molinari, M. (2008). Cognitive sequencing impairment in patients with focal or atrophic cerebellar damage. Brain, 131(5), 1332–1343. https://doi.org/10.1093/brain/awn040
