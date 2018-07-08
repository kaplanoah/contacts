"""Utility functions for getting and processing contact names."""

import os


def get_contacts_source(path):
    filename, extension = os.path.splitext(path)

    if extension == '.vcf':
        return 'apple'
    elif 'facebook' in filename:
        return 'facebook'
    else:
        return 'txt'


def is_contact(previous_line, source):
    if source == 'apple':
        return previous_line[0:2] == 'N:'
    elif source == 'facebook':
        return previous_line == 'Friends\n'
    else:
        return True


def process_contact(line, source):
    if source == 'apple':
        return line[3:].strip()
    return line.strip()


def get_contacts_set_from_file(path):
    source = get_contacts_source(path)

    contacts = set()

    with open(path, 'r') as contacts_file:

        previous_line = ''

        for line in contacts_file:

            if is_contact(previous_line, source):
                contact = process_contact(line, source)
                contacts.add(contact)

            previous_line = line

    return contacts
