from GmailChatStats.Reports.Diagrams import Year
from GmailChatStats.Reports.Diagrams import Hours
from GmailChatStats.Reports.Diagrams import DaysHours
from GmailChatStats.Reports.Diagrams import MonthsDaysHours

username = ''


sqldb = './data/'+username+'/stats.db'


def generateYear(sqldb, year):
	print "Generating year ", year
	html = "<html><body><table>"
	
	for x in [1,2,3,4,5,6,7,8,9,10,11,12]:
		print x
		MonthsDaysHours(sqldb, year = year,month=x, title = '(' + str(year) +', '+ str(x) + ')', name='img/months_year_'+str(year)+str(x))
		html = html + "<tr><td><img src=\"../img/months_year_"+str(year)+str(x)+".png\"></li></td></tr>"
	html = html + "</table></body></html>"

	f = open('./html/stats_'+str(year)+'.html', 'w')
	f.write(html)
	f.flush()
	f.close()
	

def generate(sqldb, yearmin, yearmax):
	html = "<html><body><table>"
	
	for y in range(yearmin, yearmax+1):
		print "Generating hours..."
		DaysHours(sqldb,yearmax=y, yearmin=y, name="img/year_"+str(y), title = '(' + str(y) + ')')
		generateYear(sqldb, y)
		html = html + "<tr><td><a href=\"html/stats_"+str(y)+".html\"><img src=\"img/year_"+str(y) +".png\"></a></li></td></tr>"
		
	f = open('./stats_'+str(yearmin)+str(yearmax)+'.html', 'w')
	f.write(html)
	f.flush()
	f.close()
	
	
generate(sqldb, 2008, 2012)




