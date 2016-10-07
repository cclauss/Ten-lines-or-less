# See: https://omz-forums.appspot.com/pythonista/post/5254558653612032
# and: https://omz-forums.appspot.com/editorial/post/6075976853225472
import json, tempfile, ui  # noqa

_aview = [{"class": "Button", "attributes": {"font_size": 64,
                                             "title": "Tap me!"}}]


def load_view_from_list(view_list):
    with tempfile.NamedTemporaryFile(suffix='.pyui') as temp_file:
        json.dump(view_list, temp_file)
        temp_file.seek(0)  # move the file read cursor back to byte zero
        return ui.load_view(temp_file.name)

view = load_view_from_list(_aview)
view.action = lambda sender: sender.close()
view.present(hide_title_bar=True)
