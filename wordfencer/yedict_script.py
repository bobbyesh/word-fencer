# yedict_script.py

"""Script for generating two files from the yedict dictionary.  One for traditional 
characters and one for simplified characters.  One word per line.
"""


path = 'data/yedict.txt'
simp_path = 'data/yue-Hans.txt'
trad_path = 'data/yue-Hant.txt'

def main():
    with open(path, 'r') as f:
        with open(simp_path, 'w') as simp_f:
            with open(trad_path, 'w') as trad_f:

                for line in f:
                    trad = line.split()[0]
                    simp = line.split()[1]
                    simp_f.write(simp + '\n')
                    trad_f.write(trad + '\n')



if __name__ == '__main__':
    main()
