"""
Batch rename PDFs from Scribd
Strips leading number and dash
For example, '12345678-My-favorite-song.pdf'
becomes 'My-favorite-song.pdf'
Creator: Sam Buchl, 30-Jun-2019
"""

import os


def main():

    #TODO: Insert your directory
    directory = '/your/path/here/'

    for filename in os.listdir(directory):
        old_name = os.path.join(directory, filename)
        new_name = os.path.join(directory, filename[(filename.index('-')+1):])
        os.rename(old_name, new_name)


if __name__ == '__main__':
    main()
