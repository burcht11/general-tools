import ROOT

def normalize_histos(histograms):
    """Normalize histograms to 1 and scale appropriately
    
    Arguments:
        histograms {list or dict} -- Filled with TH1F or TH1D
    Returns:
        None - All actions taken on objects
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
    max_val = max([h.GetMaximum() for h in h_list])
    [h.SetMaximum(1.25 * max_val) for h in h_list]
    [h.GetYaxis().SetTitle('Arbitrary Units (Normalized to 1)') for h in h_list]
        

