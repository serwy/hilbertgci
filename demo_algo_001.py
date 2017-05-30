from pylab import *
from numpy import *
ion()

## Example of GADFLI and QuickGCI processing
import pyglottal as pyg
import corpus_loader

# Replace with path to full APLAWD database
aplawd = corpus_loader.APLAWD('./mini_aplawd')

a = aplawd.load(2)
gci_gadfli = pyg.gadfli(a.e, fmin=20, fmax=1500, fs=a.fs,
                        m=0.25, tau=-0.25,
                        theta=0, reps=2,
                        )

gci_quick = pyg.quick_gci(a.e, fmin=50, fmax=1500, fs=a.fs,
                          reps=2,
                          gamma=1)

fig = figure(1)
clf()

ax = subplot(111)
title('APLAWD waveform: %s' % a.name)

t = arange(len(a.d)) / a.fs
plot(t, a.d, alpha=0.5,
     label='DEGG')

plot(t[gci_gadfli], 0*gci_gadfli, 'o', ms=10, alpha=0.5,
     label='GADFLI')

plot(t[gci_quick], 0*gci_quick, '^', ms=10, alpha=0.5,
     label='QuickGCI')

legend(loc='lower right', fancybox=True, framealpha=0.5)
ylabel('DEGG')

xlabel('Time (s)')
tight_layout()

show(block=True)
