from GmailChatStats.Reports.Diagrams import Year
from GmailChatStats.Reports.Diagrams import Hours
from GmailChatStats.Reports.Diagrams import DaysHours
from GmailChatStats.Reports.Diagrams import MonthsDaysHours

username = ''


sqldb = './data/'+username+'/stats.db'


def generateYear(sqldb, year, people, prefix):
    print "Generating year ", year
    html = "<html><body><table>"
    
    for x in [1,2,3,4,5,6,7,8,9,10,11,12]:
        print x
        MonthsDaysHours(sqldb, year = year,month=x, title = '(' + str(year) +', '+ str(x) + ')', name='img/'+prefix+'months_year_'+str(year)+str(x), peopleInclude=people)
        html = html + "<tr><td><img src=\"../img/"+prefix+"months_year_"+str(year)+str(x)+".png\"></li></td></tr>"
    html = html + "</table></body></html>"

    f = open('./html/stats_'+prefix+'_'+str(year)+'.html', 'w')
    f.write(html)
    f.flush()
    f.close()
    

def generate(sqldb, yearmin, yearmax, people = None, prefix=""):
    html = "<html><body><table>"
    
    for y in range(yearmin, yearmax+1):
        print "Generating hours..."
        DaysHours(sqldb,yearmax=y, yearmin=y, name="img/"+prefix+"year_"+str(y), title = '(' + str(y) + ')', peopleInclude=people)
        generateYear(sqldb, y, people, prefix)
        html = html + "<tr><td><a href=\"html/stats_"+prefix+"_"+str(y)+".html\"><img src=\"img/"+prefix+"year_"+str(y) +".png\"></a></li></td></tr>"
        
    f = open('./stats_'+prefix+'_'+str(yearmin)+str(yearmax)+'.html', 'w')
    f.write(html)
    f.flush()
    f.close()
    

    

print 'Total'
generate(sqldb, 2008, 2012, prefix='total')


