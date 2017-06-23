import secret


contacts = set()


def get_set_from_file(path):
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

contacts -= get_set_from_file('remove.txt')


# combine and convert

with open ('combine_and_convert.txt', 'r') as combine_and_convert_file:

    for line in combine_and_convert_file:
        names = line.split(', ')
        names[-1] = names[-1].strip()
        name_to_keep = names[0]
        names = set(names)
        contacts -= names
        contacts.add(name_to_keep)

# print new contacts

current = get_set_from_file('current.txt')

for contact in sorted(contacts):
    if contact not in current:
        print contact
