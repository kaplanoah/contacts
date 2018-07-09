"""Combines and cleans contact names from Apple and Facebook."""

from utils import get_contacts_set_from_file


contacts = set()

# Apple
contacts.update(get_contacts_set_from_file('contacts.vcf'))

# Facebook
contacts.update(get_contacts_set_from_file('facebook_friends.txt'))

# remove
contacts.difference_update(get_contacts_set_from_file('remove.txt'))

# combine and convert
with open('combine_and_convert.txt', 'r') as combine_and_convert_file:

    for line in combine_and_convert_file:
        names = line.strip().split(',')
        name_to_keep = names[0]
        contacts.difference_update(set(names))
        contacts.add(name_to_keep)

# print new contacts
current = get_contacts_set_from_file('current.txt')

for contact in sorted(contacts):
    if contact not in current:
        print(contact)
