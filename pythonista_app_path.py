import os, traceback, ui

def pythonista_app_path():
    try:
        os.chdir(os.path.expanduser('~/..'))
        os.path.abspath(os.curdir)
        print('Did not throw.  Are you on Pythonista?')
    except OSError as e:
        for word in traceback.format_exc(e).split('"'):
            if '/Pythonista.app/' in word:
                return word[:-19]
    return ''

if __name__ == '__main__':
    print('pwd:', os.path.abspath(os.curdir))
    print('app:', pythonista_app_path())
    fmt = 'file://{}/Documentation/index.html'
    web_view = ui.WebView(name='Pythonista Documentation')
    web_view.load_url(fmt.format(pythonista_app_path()))
    web_view.present()  # present Pythonista docs in a ui.WebView
