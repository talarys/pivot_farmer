def click(p, w, device):
    if not p:
        return
    x, y = p[0]*1920/w.width, p[1]*1080/w.height
    device.shell(f'input tap {x+20} {y+20}')
