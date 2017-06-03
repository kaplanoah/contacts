# get contacts from Contacts

with open ('contacts.vcf', 'r') as contacts_file:

    for line in contacts_file:

        if line[0:3] != 'FN:':
            continue

        print line[3:].strip()


# get contacts from Facebook
