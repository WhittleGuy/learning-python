#!/bin/python

################################################################################
# Programmer: Whittle
# File: str_split.py
# Purpose: Learn to split strings
# Date: February 26, 2022
################################################################################

def main():
    authors = "Audre Lorde, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

    author_names = authors.split(',')

    author_last_names = []
    for name in author_names:
      # Got -> "Audre Lorde"
      # Want -> Lorde
        author_last_names.append(name.split(' ')[-1])

      # name -> is a string (i.e. "Audre Lorde")
      # .split(' ') -> splits string on spaces (i.e. "Audre Lorde" -> ['Audre', 'Lorde'])
      # <list>[-1] -> gets last item of list (i.e. ['Audre', 'Lorde'][-1] -> 'Lorde')

    print(author_last_names)


if __name__ == '__main__':
    main()
