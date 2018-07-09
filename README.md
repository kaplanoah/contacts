# Contacts processor

Take contact names from Apple contacts and Facebook friends, and combines and cleans them up.

<img width="500px" src="https://i.imgur.com/eSLUHLK.png">
<img width="500px" src="https://i.imgur.com/HqCKs86.png">
<img width="500px" src="https://i.imgur.com/xHdkPCa.png">

## Installing

1. Clone or download the repository.

2. Running the script requires Python. (Works with Python 2 and 3. Check for Python in terminal with: `python -V`)


## Using

### Add Apple contacts

1. Open the Contacts app for mac.

1. Select all the contacts you want to include (for all of them, `⌘A`)

1. Export the contacts as vCards (File > Export > Export vCard)

1. Move the export to the `contacts_files` directory:

```
$ mv <path_to_export> <path_to_repo>/contacts_files/
```

The file should contain something like this:

```
N:Russ;Newton;;;
FN:Russ Newton
TEL;type=CELL;type=VOICE;type=pref:
```

### Add Facebook friends

1. Go to the Facebook page that has all your friends.

1. Scroll to the bottom of the page so all your friends load and display.

1. Copy the contents of the entire page (`⌘A`)

1. Make a `facebook_friends.txt` file in the `contacts_files` directory.

1. Paste the Facebook page contents into the `facebook_friends.txt` file.

The file should contain something like this:

```
Close Friend
Friends
Russell Newton
16 mutual friends
```

### Run the script

    $ python contacts.py

The output will be the names from all the contacts and friends.

### Remove names

To remove a name from the output, add a `remove.txt` file to `contacts_files` and put one name on each line:

```
Lorene Stone
Jamie Hansen
```

### Combine names

To combine several names into one name, add a `combine_and_convert.csv` file to `contacts_files` and put comma separated names that you want combined. The output will always use only the first name on each line:

```
Russ Newton, Russell Newton
```


## Testing

From the `contacts` directory, run:

    $ python -m unittest discover tests
