import matplotlib as plt
from rootpy.tree import Tree
from rootpy.io import root_open
import matplotlib.pyplot as plt
from rootpy.plotting.style import get_style, set_style
import rootpy.plotting.root2matplotlib as rplt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter
from matplotlib import gridspec
import numpy as np


def watermark(text):
    """
    adds watermark to lower left corner of matplotlib plot

    """
    plt.annotate(s=text, xy=(.005,.007), xycoords='figure fraction',
                 textcoords='figure fraction', color='grey',alpha=0.7)


class Plot:

    def __init__(self, normalize=True, colormap=plt.cm.viridis):
        """generic plotting function
        plot_ratio = instruct it to make the ratio plot or not
        """

        # Set style
        style = get_style('ATLAS')
        set_style(style)

        # Set normal plot
        self.fig = plt.figure(figsize=(7, 5), dpi=100)
        self.axes = plt.axes()
        self.axes.xaxis.set_minor_locator(AutoMinorLocator())
        self.axes.yaxis.set_minor_locator(AutoMinorLocator())



    def add_watermark(self):
        plt.annotate(s='Tyler James Burch', xy=(.005,.007), xycoords='figure fraction',
                    textcoords='figure fraction', color='grey',alpha=0.7)


    def add_legend(self, **kwargs):
        """Add legend to plot. kwargs pass to plt.legend
        Useful kwargs: ncol, fontsize
        """
        self.leg = plt.legend(kwargs)


    def ATLAS_label(self, x, y, type='Internal', fontsize=12, **kwargs):
        """Add ATLAS label. kwargs pass to plt.annotate        
        """
        plt.annotate(s='ATLAS %s' % type, xy=(x,y), xycoords='figure fraction', 
                    textcoords='figure fraction', kwargs)


    def xlabel(self, title):
        # TODO: figureout how to get axes here
        plt.xlabel(title, position=(1, 0), va='bottom', ha='right', labelpad=20)


    def ylabel(self, title, pos=(1,0)):
        # TODO: figureout how to get axes here
        plt.ylabel(title, position=pos, va='top', ha='right', labelpad=20)
        plt.tight_layout()        


    def _finalize(self):
        plt.tight_layout()


class Standard(Plot):
    """ Generic single plot
    """

    def __init__(self,  histarg, normalize=True, colormap=plt.cm.viridis):
        Plot.__init__(normalize, colormap)

        # Plan the colormap
        color = np.linspace(0,0.8,len(histarg)

        # things to do to all histograms
        for i, h in zip(color, histarg):
            if normalize == True:
                h.Scale(1/h.Integral())
            if len(histarg) == 1
                h.linecolor = "cornflower"
            else:
                h.linecolor = colormap(i)
            rplt.errorbar(h, markersize=0)


class Ratio(Plot):
    """ Class for generic Ratio plots """

    def __init__(self, histarg, normalize=True, colormap=plt.cm.viridis):
        Standard.__init__(normalize, colormap) # make the standard plot
        
        # Make sure we have enough hists
        if len(histarg) < 2:
            raise ValueError('Need at least 2 histograms for ratio plot')

        self.reference_hist = histarg[0]
        self.fig = plt.figure(figsize=(7,8))
        gs = gridspec.GridSpec(nrows=2, ncols=1, height_ratios=[3,1])
        
        self.ax0 = plt.subplot(gs[0])
        # Turn off 0 for y axis        
        self.ax0.get_xaxis().set_visible(False)
        yticks = self.ax0.yaxis.get_major_ticks() 
        yticks[0].set_visible(False)
        
        # Position ratio plot just under the actual plot
        self.ax1 = plt.subplot(gs[1])
        self.gs.update(wspace=0, hspace=0) 

        # Fill ratio plot
        for hist in histarg:
            h_ratio = self.reference_hist.divide(self.reference_hist, hist) # This is weird.
            h_ratio.linecolor = 'navy'
            rplt.errorbar(h_ratio, markersize=0)

        plt.axhline(y=1, color='black', linestyle=':')
        plt.tight_layout()

