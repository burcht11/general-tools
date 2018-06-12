import matplotlib as plt


def watermark(text):
    """
    adds watermark to lower left corner of matplotlib plot

    """
    plt.annotate(s=text, xy=(.005,.007), xycoords='figure fraction',
                 textcoords='figure fraction', color='grey',alpha=0.7)
