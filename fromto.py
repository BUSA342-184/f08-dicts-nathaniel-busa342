#!/usr/bin/env python3

'''
This program will take the specified mbox-short.txt file and count 
the email addresses based on the direction of the correspondence.
[To or From]
'''
__author__ = 'Nathaniel Weeks'
__date__ = '9/16/2018'


# To access STDOUT
import sys
# To access writerows method
import csv


def main():
    # Open the file in read mode
    with open('mbox-short.txt') as f:
        # Create four empty dictionaries to hold the email counts
        from_user, from_host, to_user, to_host = {}, {}, {}, {}
        # Loop through all the lines of the text file
        for line in f:
            # If the line starts with either 'From:' or 'To:'
            if line.startswith('From:') or line.startswith('To:'):
                # Split the line into a list
                words = line.split() 
                # Assume the index of 1 is the email address
                email = words[1]
                # Split the email into the user and host portions
                user, host = email.split('@')
                # If the line starts with 'From:'
                if line.startswith('From:'):
                    # Set the default count to zero if this is the first
                    # time the user or host is being added to the dict
                    from_user[user] = from_user.get(user, 0) + 1
                    from_host[host] = from_host.get(host, 0) + 1
                # If the line starts with 'To:'
                elif line.startswith('To:'):
                    # Set the default count to zero if this is the first
                    # time the user or host is being added to the dict
                    to_user[user] = to_user.get(user, 0) + 1
                    to_host[host] = to_host.get(host, 0) + 1
    
    # Create a csv writer that writes to stdout
    cw = csv.writer(sys.stdout)
    # Print each section
    # Sort the output for each dictionary by the key and print out the 
    # key value pair using the csv writer
    print('--- FROM USER ---')
    cw.writerows(sorted(from_user.items()))
    print('--- FROM HOST ---')
    cw.writerows(sorted(from_host.items()))
    print('--- TO USER ---')
    cw.writerows(sorted(to_user.items()))
    print('--- TO HOST ---')
    cw.writerows(sorted(to_host.items()))


if __name__ == '__main__':
    main()
