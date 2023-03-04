
# Make a local copy of the text file passed in via a share sheet.

# See: https://forum.omz-software.com/topic/2637/is-it-possible-to-read-a-file-say-txt-file-from-other-app  # noqa

import appex, datetime  # noqa


def main():
    if appex.is_running_extension():
        attachments = appex.get_attachments()
        assert attachments and attachments[0].rstrip(), "Ain't gots no text!!"
        fmt = "from Goodreader_{:%Y_%m_%d_%H_%M_%S}.txt"
        file_name = fmt.format(datetime.datetime.now())
        with open(file_name, "w") as out_file:
            out_file.write(attachments[0])
        print(f"{len(attachments[0])} bytes written to {file_name}.")


if __name__ == "__main__":
    main()
