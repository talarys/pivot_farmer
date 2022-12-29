import mss


def screenshot(tw):
    with mss.mss() as sct:
        window = {"top": tw.top, "left": tw.left,
                  "width": tw.width, "height": tw.height}
        return sct.grab(window)
