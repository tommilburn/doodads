from lib.utils import createTemplate
import sys
import datetime
import calendar
import argparse


parser = argparse.ArgumentParser(description='A calendar generator')
parser.add_argument('year')
parser.add_argument('month')

args = parser.parse_args()

templatename='foodlog'
templatefile = createTemplate(templatename)

cal = calendar.Calendar()
today = datetime.date.today()

templateYear = args.year or '2019'
templateMonth = args.month or '12'

def generateText(year, month):
  lines = [str('# ' + str(year) + '-' + str(month)) + '\n']

  days = list(filter(lambda x: x > 0, list(cal.itermonthdays(2019, 12))))

  for day in days:
    lines.append('## ' + calendar.month_abbr[int(month)] + ' ' + str(day).rjust(2, '0'))
    lines.append('- \n')

  t = '\n'.join(lines)
  print(t) # it's nice to `| pbcopy`
  return t

templatefile.write(generateText(templateYear, templateMonth))
templatefile.close()