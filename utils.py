"""Utility functions for getting and processing contact names."""

import os

CONTACTS_FILES_PATH = 'contacts_files/'


def get_path(file_name):
    return'{}{}'.format(CONTACTS_FILES_PATH, file_name)


def get_contacts_source(file_name):
    filename, extension = os.path.splitext(file_name)

    if extension == '.vcf':
        return 'apple'
    elif 'facebook' in filename:
        return 'facebook'
    else:
        return 'txt/csv'


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


def get_contacts_set_from_file(file_name):
    source = get_contacts_source(file_name)

    contacts = set()

    with open(get_path(file_name), 'r') as contacts_file:

        previous_line = ''

        for line in contacts_file:

            if is_contact(previous_line, source):
                contact = process_contact(line, source)
                contacts.add(contact)

            previous_line = line

    return contacts
