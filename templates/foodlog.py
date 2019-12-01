from lib.utils import createTemplate
import sys
import datetime
import calendar
import argparse

parser = argparse.ArgumentParser(description='Daily list markdown text generator')
parser.add_argument('-f', '--file', help='save to file', action='store_true')
parser.add_argument('year')
parser.add_argument('month')
args = parser.parse_args()

cal = calendar.Calendar()

templateYear = int(args.year)
templateMonth = int(args.month)

def generateText(year, month):

  lines = ['# {:d}-{:02d}\n'.format(year, month)]

  days = list(filter(lambda x: x > 0, list(cal.itermonthdays(year, month))))

  for day in days:
    lines.append('## {:s} {:02d}'.format(calendar.month_abbr[int(month)], day))
    lines.append('- \n')

  t = '\n'.join(lines)
  return t

output = generateText(templateYear, templateMonth)

# save to file
if args.file is True:
  templatename='foodlog'
  templatefile = createTemplate(templatename)
  templatefile.write(output)
  templatefile.close()
# otherwise stdout
else:
  print(output)