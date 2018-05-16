import ROOT
from AtlasStyle import ATLASLabel, myLabel

def normalize_histos(histograms):
    """Normalize histograms to 1 and scale appropriately
    
    Arguments:
        histograms {list or dict} -- Filled with TH1F or TH1D
    """
    # Convert accepted argument to list
    if type(histograms) is dict:
        h_list = []
        for key in histograms:
            h_list.append(histograms[key])
    elif type(histograms) is ROOT.TH1F:
        h_list = [histograms]
    elif type(histograms) is list:
        h_list = histograms
    else:
        raise TypeError('normalize_histos requires dictionary, list, or TH1F')

    # Normalize, fix range, set title
    [h.Scale(1 / h.Integral()) for h in h_list]    
    set_max(h_list)            
    [h.GetYaxis().SetTitle('Arbitrary Units (Normalized to 1)') for h in h_list]
        

def set_labels(anchor, lumi, *args):
    """Sets ROOT.TLegend in desired area
    
    Arguments:
        anchor {string} -- "top_right, top, left, right"
        TODO: add more anchors
        lumi {string} -- luminosity
        *args {strings} -- any extra legends

    Returns:
        [ROOT.ROOT.TLegend]
    """

    if anchor is "top_right":
        atlasx = 0.67
        atlasy = 0.75
        leg = ROOT.TLegend(0.73,0.53,0.93,0.94)

    elif anchor is "top":
        atlasx = 0.15
        atlasy = 0.88
        leg = ROOT.TLegend(0.40,0.78,0.93,0.93)

    elif anchor is "left":
        atlasx = 0.15
        atlasy = 0.88
        leg = ROOT.TLegend(0.15,0.35,0.35,0.74)

    elif anchor is "right":
        atlasx = 0.76
        atlasy = 0.88
        leg = ROOT.TLegend(0.73,0.35,0.93,0.74)

    else:
        atlasx = 0.76
        atlasy = 0.88
        leg = ROOT.TLegend(0.75,0.7,0.89,0.89)



    myLabel( atlasx, atlasy + 0.1, 1, "#int L dt = %s fb^{-1}" % lumi)
    myLabel( atlasx, atlasy + 0.04 , 1, "#sqrt{s}= 13 TeV")
    ATLASLabel(atlasx, atlasy, "   Internal", 1)

    for label in args:
        idx = args.index(label)
        myLabel(atlasx, atlasy - (0.05 * idx + 0.1), 1, label)

    return leg

def set_max(h_list):
    max_val = max([h.GetMaximum() for h in h_list])
    [h.SetMaximum(1.25 * max_val) for h in h_list]