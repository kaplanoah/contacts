"""Combines and cleans contact names from Apple and Facebook."""

from utils import get_contacts_set_from_file, get_path, combine_and_convert


contacts = set()

# Apple
contacts.update(get_contacts_set_from_file('contacts.vcf'))

# Facebook
contacts.update(get_contacts_set_from_file('facebook_friends.txt'))

# combine and convert
combine_and_convert(contacts)

# remove
contacts.difference_update(get_contacts_set_from_file('remove.txt'))

# print new contacts
current = get_contacts_set_from_file('current.txt')

for contact in sorted(contacts):
    if contact not in current:
        print(contact)
