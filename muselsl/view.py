
def view(window=5, scale=100, refresh=0.2, figure="15x6", version=2, backend='TkAgg'):
    if version == 4:
    	from . import viewer_v4
    	viewer_v4.view()
    elif version == 3:
    	from . import viewer_v3
    	viewer_v3.view()
    elif version == 2:
        from . import viewer_v2
        viewer_v2.view()
    else:
        from . import viewer_v2
        viewer_v2.view(window, scale, refresh, figure, backend)
