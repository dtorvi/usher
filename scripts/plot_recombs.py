import matplotlib.pyplot as plt
import numpy as np
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plot recombinants')
    parser.add_argument("-v", type=str,
                        help="VCF containing donor, acceptor and recombinant"
                        " node")
    parser.add_argument("-l", type=int,
                        help="genome length")
    parser.add_argument("-s1", type=int,
                        help="start low")
    parser.add_argument("-s2", type=int,
                        help="start high")
    parser.add_argument("-e1", type=int,
                        help="end low")
    parser.add_argument("-e2", type=int,
                        help="end high")
    parser.add_argument("-o", type=str,
                        help="output filename")
    parser.add_argument("-r", type=str,
                        help="recombinant name")


    args = vars(parser.parse_args())
    vcf_filename = args.get('v', '')
    output_filename = args.get('o', '')
    recomb = args.get('r', '')
    length = args.get('l', '')
    s1 = args.get('s1', '')
    e1 = args.get('e1', '')
    s2 = args.get('s2', '')
    e2 = args.get('e2', '')
    
    fig = plt.figure()
    ax = plt.axes()
    
    
    xr = [0, length]
    yr = [1, 1]
    ax.plot(xr, yr);
    yr = [0, 0]
    ax.plot(xr, yr);
    yr = [-1, -1]
    ax.plot(xr, yr);

    x1 = []
    x2 = []
    x3 = []

    header_found = False
    num_words = 0
    recomb_idx = -1
    for line in open(vcf_filename):
        words=line.split()
        if ((not header_found) and (len(words) >2) and (words[1] == "POS")):
            header_found = True
            num_words = len(words)
            if (words[num_words-3] == recomb):
                recomb_idx = 0
            if (words[num_words-2] == recomb):
                recomb_idx = 1
            if (words[num_words-1] == recomb):
                recomb_idx = 2
        elif (header_found and ((int(words[num_words-3]) == 
                    int(words[num_words-2])) and (int(words[num_words-3]) == 
                                                  int(words[num_words-1])))):
                      continue
        elif (header_found):
            if (int(words[num_words-3]) > 0):
                x1.append(int(words[1]))
            if (int(words[num_words-2]) > 0):
                x2.append(int(words[1]))
            if (int(words[num_words-1]) > 0):
                x3.append(int(words[1]))

    y1 = [1 for tmp in x1]
    y2 = [0 for tmp in x2]
    y3 = [-1 for tmp in x3]

    lab = ''
    if (recomb_idx == 0):
        lab = 'recomb'
    ax.scatter(x1, y1, marker='o', label = lab)
    
    lab = ''
    if (recomb_idx == 1):
        lab = 'recomb'
    ax.scatter(x2, y2, marker='o', label = lab)
    
    lab = ''
    if (recomb_idx == 2):
        lab = 'recomb'
    ax.scatter(x3, y3, marker='o', label = lab)

    print (x1)
    print (x2)
    print (x3)
    
    ax.legend()

    ax.plot([s1,s1],[-10, 10],'k')
    ax.plot([s2,s2],[-10, 10],'k')
    ax.plot([e1,e1],[-10, 10],'k')
    ax.plot([e2,e2],[-10, 10],'k')

    plt.ylim([-10, 10])
    plt.savefig(output_filename)
