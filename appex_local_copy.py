# coding: utf-8

# Make a local copy of the text file passed in via a share sheet.

# See: https://forum.omz-software.com/topic/2637/is-it-possible-to-read-a-file-say-txt-file-from-other-app

import appex

def main():
    if appex.is_running_extension():
        attachments = appex.get_attachments()
        assert attachments and attachments[0].rstrip(), "Ain't gots no text!!"
        with open('from Goodreader.txt', 'w') as out_file:
            out_file.write(attachments[0])
        print('{} bytes written.'.format(len(attachments[0])))

if __name__ == '__main__':
    main()
