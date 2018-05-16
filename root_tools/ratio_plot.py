import ROOT
from histogram_tools import set_labels, set_max
from AtlasStyle import AtlasStyle
def ratio_plot(h1, h2, h_ratio, x_label, y_label='Data/MC', logy=False):
    """Plot a ratio plot of 2 TH1 objects
    
    Arguments:
        h1 {TH1, THStack} -- first histogram
        h2 {TH1, THStack} -- second
    
    Returns:
    """
    AtlasStyle()
    
    if type(h1) is ROOT.THStack:
        h1 = h1.GetStack().Last()
    if type(h2) is ROOT.THStack:
        h2 = h2.GetStack().Last()

    ROOT.gStyle.SetOptStat(000000)
    
    canvas = ROOT.TCanvas("c1","c1",600,650)

    #Make top pad
    pad1 = ROOT.TPad("pad1", "pad1",0.,0,1.,1.)
    pad1.Draw()
    pad1.cd()
    if logy:
        pad1.SetLogy(1)
    else:
        h1.SetMinimum(0.001)

    # TODO: generalize for THStack
    h1.Draw('hist')
    h1.GetXaxis().SetLabelOffset(999)
    h2.Draw('hist same')    
    set_max([h1,h2])

    
    pad2 = ROOT.TPad("pad2", "pad2",0.,0.,1.,0.15,0)
    pad2.SetTopMargin(0)
    pad2.Draw()
    pad2.cd()
    pad2.SetBottomMargin(0.25)

    h_ratio.SetTitle("")
    h_ratio.SetLineColor(ROOT.kBlack)
    h_ratio.SetMarkerStyle(20)
    h_ratio.SetMarkerSize(0.5)
    # Y axis ratio plot settings
    h_ratio.GetYaxis().SetTitle(y_label)
    h_ratio.GetYaxis().SetNdivisions(505)
    h_ratio.GetYaxis().SetTitleSize(.1)
    h_ratio.GetYaxis().SetTitleOffset(.5)
    h_ratio.GetYaxis().SetLabelFont(43)
    h_ratio.GetYaxis().SetLabelSize(15)
    h_ratio.GetYaxis().SetRangeUser(0.,3.)

    # X axis ratio plot settings
    h_ratio.GetXaxis().SetTitle(x_label)
    h_ratio.GetXaxis().SetTitleSize(.09)
    h_ratio.GetXaxis().SetTitleOffset(1.2)
    h_ratio.GetXaxis().SetLabelFont(43)
    h_ratio.GetXaxis().SetLabelSize(15)
    h_ratio.Draw("ep")

    # tl = ROOT.TLine(h_ratio.GetXaxis().GetXmin(),1,h_ratio.GetXaxis().GetXmax(),1)
    # tl.SetLineWidth(2)
    # tl.SetLineStyle(2)
    # tl.Draw()

    return canvas