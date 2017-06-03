# get contacts from Contacts

with open ('contacts.vcf', 'r') as contacts_file:

    for line in contacts_file:

        if line[0:3] != 'FN:':
            continue

        print line[3:].strip()


# get contacts from Facebook

with open ('facebook_friends.txt', 'r') as facebook_friends_file:

    for line in facebook_friends_file:

        if 'FriendFriends' not in line:
            continue

        print facebook_friends_file.next().strip()
