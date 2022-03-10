#!/bin/usr/env python

import argparse
import os
import sys

parser = argparse.ArgumentParser(
    description="Set up a new project directory for a paper in LaTeX")
parser.add_argument("projpath", nargs=1,
                    help='name for the created directory')
parser.add_argument("-a", "--author", dest="author", nargs='+',
                    help='Name(s) of the authors')
parser.add_argument("-t", "--title", dest="title", nargs='+',
                    help='Title of the paper')
args = parser.parse_args()

if not args.title:
    args.title = ['My', 'Title']
if not args.author:
    args.author = ["A", "Guy", "Who", "Uses", "LaTeX"]

preamble = f"""\\documentclass[12pt]{{article}}
\\usepackage[margin=1in]{{geometry}}

% Refs
\\usepackage[style=nature, backend=bibtex]{{biblatex}}
\\addbibresource{{{''.join(args.title)}.bib}}
\\usepackage[usenames,dvipsnames,svgnames,table]{{xcolor}}

% Math
\\usepackage{{amsmath}}
\\usepackage{{amssymb}}

% Figures
\\usepackage{{graphicx}}
\\newcommand{{\\figref}}[1]{{Fig.~\\ref{{fig:#1}}}}

% subfigures
\\usepackage{{caption}}
\\usepackage{{subcaption}}

% author notes
\\newcommand{{\\note}}[1]{{\\textcolor{{red}}{{[#1]}}}}

\\title{{{' '.join(args.title)}}}
\\author{{{' '.join(args.author)}}}
\\date{{\\today}}"""

the_body = r"""


\begin{document}

\maketitle

\printbibliography
\end{document}
"""
# make the directory
os.mkdir(args.projpath[0])
os.mkdir(f"{args.projpath[0]}/assets")
os.system(f"touch {args.projpath[0]}/{''.join(args.title)}.bib")

# make main.tex
with open(f"{args.projpath[0]}/main.tex", "w") as fout:
    fout.write(preamble)
    fout.write(the_body)
