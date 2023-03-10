S = 'Spam'
#
S.find('pa')
#1
S
#'Spam'
S.replace('pa', 'XYZ')
#'SXYZm'
S
#'Spam'
line = 'aaa,bbb,ccccc,dd'
#
line.split(',')
#['aaa', 'bbb', 'ccccc', 'dd']
S = 'spam'
#
S.upper()
#'SPAM'
S.isalpha() # Content tests: isalpha, isdigit, etc.
#True
line = 'aaa,bbb,ccccc,dd\n'
#
line.rstrip()
#'aaa,bbb,ccccc,dd'
line.rstrip().split(',')
#['aaa', 'bbb', 'ccccc', 'dd']