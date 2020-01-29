# coding: utf-8

# See: https://forum.omz-software.com/topic/2410/horizonally-scrolling-textview

import string, ui  # noqa

text = string.ascii_letters * 5

scroll_view = ui.ScrollView()
text_view = ui.TextView()
text_view.text = text
scroll_view.add_subview(text_view)
scroll_view.present()
x, y, w, h = scroll_view.bounds
scroll_view.content_size = w * 2, h
text_view.frame = x, y, w * 2, h
