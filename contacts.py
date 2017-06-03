import secret


contacts = set()


def set_from_file(path):
    with open(path, 'r') as file:
        return {line.strip() for line in file}


# get contacts from Contacts

with open ('contacts.vcf', 'r') as contacts_file:

    for line in contacts_file:

        if line[0:3] != 'FN:':
            continue

        contact = line[3:].strip()

        contacts.add(contact)


# get contacts from Facebook

with open ('facebook_friends.txt', 'r') as facebook_friends_file:

    for line in facebook_friends_file:

        if 'FriendFriends' not in line:
            continue

        friend = facebook_friends_file.next().strip()

        contacts.add(friend)


# remove contacts

remove = set_from_file('remove.txt')

contacts -= remove


current = set_from_file('current.txt')

for contact in sorted(contacts):
    if contact not in current:
        print contact
