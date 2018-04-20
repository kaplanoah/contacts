import os


def is_contact_apple(previous_line):
    return previous_line[0:2] == 'N:'

def is_contact_facebook(previous_line):
    return previous_line == 'Friends\n'

def is_contact_default(previous_line):
    return True

def process_contact_default(line):
    return line.strip()

def process_contact_apple(line):
    return line[3:].strip()


def get_contacts_set_from_file(path):

    contacts = set()

    filename, extension = os.path.splitext(path)

    if extension == '.vcf':
        is_contact = is_contact_apple
        process_contact = process_contact_apple
    elif 'facebook' in filename:
        is_contact = is_contact_facebook
        process_contact = process_contact_default
    else:
        is_contact = is_contact_default
        process_contact = process_contact_default

    with open (path, 'r') as contacts_file:

        previous_line = ''

        for line in contacts_file:

            if is_contact(previous_line):
                contact = process_contact(line)
                contacts.add(contact)

            previous_line = line

    return contacts
