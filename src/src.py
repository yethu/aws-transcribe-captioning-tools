from srtUtils import writeTranscriptToSRT
import sys

ifile = sys.argv[1]
ofile = sys.argv[2]
source_language = sys.argv[3]

if __name__ == '__main__':
    with open(ifile, 'r') as f:
        writeTranscriptToSRT(f.read(), source_language, ofile)