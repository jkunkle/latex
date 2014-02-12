import sys
import os
from datetime import datetime

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument( '--name', default=None, dest='name', help='name of package (date will be appended) ' )

options = parser.parse_args()

if options.name is None :
    print 'Must provide a package name via --name'
    sys.exit(-1)
	

year = datetime.today().year
month = datetime.today().month
day = datetime.today().day

titledatestr = datetime.strftime(datetime.today(), '%Y_%m_%d')

pname = '%s_%s' %( options.name, titledatestr)


os.mkdir( pname )
os.system( 'echo "include ../Makefile.global" >> %s/Makefile' %pname )

# get the tex file and replace the DATE and TITLE fields
infile = open( 'Template/template.tex', 'r' )
intext = infile.read()

infile.close()
datestr = datetime.strftime(datetime.today(), '%B %d, %Y')
intext = intext.replace('DATE', datestr )
intext = intext.replace('TITLE', options.name )

outfile = open( '%s/%s.tex' %(pname, options.name), 'w' )
outfile.write(intext)
outfile.close()

os.system( 'cd %s ; make ; cd ..' %pname )

print 'If the above compilation was successful you\'re good to go ^.^'

