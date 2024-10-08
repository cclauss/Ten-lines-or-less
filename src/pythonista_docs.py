import sys

import ui

if __name__ == "__main__":
    docs_path = f"file://{sys.executable}/../Documentation/index.html"
    # webbrowser.open(docs_path)
    web_view = ui.WebView(name="Pythonista Documentation")
    web_view.load_url(docs_path)
    web_view.present()  # present Pythonista docs in a ui.WebView
