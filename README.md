# Contacts processor

Take contact names from Apple contacts and Facebook friends, and combines and cleans them up.

## Installing

1. Clone or download the repository

2. Running the script requires Python. (Works with Python 2 and 3. Check for Python in terminal with: `python -V`)

## Using

#### Add Apple contacts

1. Open the Contacts app for mac.

1. Select all the contacts you want to include (for all of them, `⌘A`)

1. Export the contacts as vCards (File > Export > Export vCard)

1. Move the export to the `contacts_files` directory:

    $ mv <path_to_export> <path_to_repo>/contacts_files/

#### Add Facebook friends

1. Go to the Facebook page with all your friends.

1. Scroll to the bottom of the page so all your friends load.

1. Copy the contents of the entire page (`⌘A`)

1. Make a `facebook_friends.txt` file in the `contacts_files` directory.

1. Paste the Facebook page contents into the `facebook_friends.txt' file.

#### Run the script

    python contacts.py

## Testing

From the `contacts` directory, run:

    $ python -m unittest discover tests