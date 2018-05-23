# -*- coding: utf-8 -*-
import time
import os
print time.strftime("%Y-%m-%d %H:%M:%S")

def makeChange(str, num):
    #print str
    print "num is", num
    num = int(num)
    print "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
    #print str
    #flag = False
    after = ""
    lines = str.split('\n')
    for line in lines:
        if "Title" in line:
            line = line.replace("Title", articles[num]['title'])
        if "link" in line:
            line = line.replace("link", articles[num]['link'])
        if "img src" in line:
            toReplace = "\"" + articles[num]['img'] + "\""
            line = line.replace("\"\"", toReplace)
        if "Content" in line:
            line = line.replace("Content", articles[num]['content'])

        after = after + line + '\n'
        # if "</div>" in line:
        #     flag = True
        # # if int(num) == 0:
        #     after = after + line + '\n'
        # elif flag == True:
        #     after = after + line + '\n'
    print "z2z"
    print after
    return after
    # for line in after:
    #     print line
        #for i in range(0, num):


def addFields(file_path, size):
    status = "HTTP/1.1 200 OK"
    currDate = "Date: Mon, 18 Dec 2017 12:28:53 GMT"
    length = "Content-Length: " + size
    filename, file_extension = os.path.splitext(file_path)
    types = {
        '.gif': 'image/gif',
        '.htm': 'text/html',
        '.html': 'text/html',
        '.jpeg': 'image/jpeg',
        '.jpg': 'image/jpg',
        '.js': 'text/javascript',
        '.png': 'image/png',
        '.text': 'text/plain',
        '.txt': 'text/plain',
        '.css': 'text/css',
    }
    content_type = "Content-Type: " + types[file_extension]
    conn = "Connection: Closed"
    serv = "Server: Amir's Server"
    lMdf = "Last-Modified: " + time.strftime("%Y-%m-%d %H:%M:%S")
    cAll = status + '\n' + currDate + '\n' + serv + '\n' + lMdf+ '\n' + length + '\n' + content_type +  '\n' + conn + '\n'
    #print cAll
    respone = """\
    """+status +"""
    """+currDate+"""
    """+content_type +"""
    """+length
    #print respone

    return cAll
def makeArticles():
    # -*- coding: utf-8 -*-
    ARTICLE1 = {
        'link': 'http://www.ynet.co.il/articles/0,7340,L-4713571,00.html',
        'img': 'https://images1.ynet.co.il/PicServer4/2014/08/05/5506384/52203970100690640360no.jpg',
        'title': 'החוש הדומיננטי שיעזור לכם בלימודים',
        'content': 'החוש הדומיננטי שיעזור לכם￼￼￼ בלימודים. אילו טיפים של שימוש בחושים יעזרו לכם?',
    }

    ARTICLE2 = {
        'link': 'http://www.ynet.co.il/articles/0,7340,L-4713571,00.html',
        'img': 'https://images1.ynet.co.il/PicServer5/2017/11/23/8172884/817287001000100980704no.jpg',
        'title': '"כ"ט בנובמבר: "שמחה שנמשכה ימים ולילות,￼ הייתה אופוריה"',
        'content': 'ב-1947 הם היו ילדים או צעירים￼￼￼￼￼￼ בתחילת דרכם, אבל את היום הגורלי ב-29 בנובמבר הם לא\
                  שוכחים עד היום. "כולם היו צמודים לרדיו. אני זוכרת את התפרצות השמחה, ריקודים\
                  והתחבקויות".',
    }

    ARTICLE3 = {
        'link': 'https://www.calcalist.co.il/world/articles/0,7340,L-3726321,00.html',
        'img': 'https://images1.calcalist.co.il/PicServer3/2017/11/30/775736/2_l.jpg',
        'title': 'רוצים נייר טואלט? הזדהו: כך משפרים הסינים￼ את מצב השירותים הציבוריים',
        'content': 'שבוע קרא נשיא סין שי ג‘ינפינג￼￼￼￼￼￼ להמשיך את מהפכת השירותים הציבוריים עליה הכריז ב-2015.ֿֿ\
                    עד כה שופצו ונבנו 68 אלף מתקנים',
    }

    ARTICLE4 = {
        'link': 'http://www.nrg.co.il/online/13/ART2/902/962.html',
        'img': 'http://www.nrg.co.il/images/archive/465x349/1/646/416.jpg',
        'title': 'מחקו לכם הודעה בווטסאפ? עדיין תוכלו לקרוא אותה',
        'content': 'פליקציה בשם Noti cation History מאפשרת למשתמשי  אנדרואיד לקרוא את הנתונים הזמניים הנשמרים ביומן הפעילות של הסמארטפון, כולל הודעות מחוקות.'
    }

    ARTICLE5 = {
        'link': 'http://www.nrg.co.il/online/55/ART2/904/542.html',
        'img': 'http://www.nrg.co.il/images/archive/465x349/1/795/429.jpg',
        'title': 'גם בחורף: זה בדיוק הזמן לקפוץ לאילת',
        'content': 'העיר הדרומית נעימה לנופש גם￼￼￼￼￼ בחודשי החורף. כעת מוצעים מחירים אטרקטיביים במיוחד בחבילות שכוללות מגוון אטרקציות, לינה וטיסות'
    }

    ARTICLE6 = {
        'link': 'https://food.walla.co.il/item/3113079',
        'img': 'https://img.wcdn.co.il/f_auto,w_700/2/5/1/3/2513314-46.jpg',
        'title': '12 בתי קפה שמתאימים לעבודה עם לפטופ',
        'content': 'בין אם אתם סטודנטים או￼￼￼ עצמאיים, זה תמיד סיפור למצוא בית קפה נעים וטעים לרבוץ בו. קיבצנו עבורכם 12 מקומות אהובים בדיוק למטרה זו, בארבע הערים הגדולות'
    }

    ARTICLE7 = {
        'link': 'https://news.walla.co.il/item/3114145',
        'img': 'https://img.wcdn.co.il/f_auto,w_700/2/4/9/5/2495334-46.jpg',
        'title': 'שותק על אזריה, נלחם באהוד ברק: בנט מנסה להיבנות כימין ממלכתי',
        'content': 'כשרגב נלחמת ברעש בתאטרון￼￼￼ יפו, בנט משנה בשקט את נהלי סל התרבות כך שהחומרים "השמאלנים" ייפלטו. כשהקשת הפוליטית מתרעמת על דיווחי ה"דיל" של טראמפ עם הפלסטינים, בנט שותק עד שהרשות תסרב.'
    }

    ARTICLE8 = {
        'link': 'https://news.walla.co.il/item/3114283',
        'img': 'https://img.wcdn.co.il/f_auto,w_700/2/5/1/4/2514588-46.jpg',
        'title': 'רצח בכל שלושה ימים: צרפת יוצאת למאבק￼￼ באלימות נגד נשים',
        'content': 'אחרי ש-126 נשים נרצחו בידי בני￼￼￼ זוגן בשנה שעברה, הציג מקרון צעדים חדשים למלחמה בתופעה. "זאת בושה לצרפת", אמר הנשיא שאחת מהבטחות הבחירות שלו הייתה להשיג שוויון מגדרי.'
    }

    ARTICLES = [ARTICLE1, ARTICLE2, ARTICLE3, ARTICLE4, ARTICLE5, ARTICLE6, ARTICLE7, ARTICLE8]
    return ARTICLES
#####START######

#config=utf-8
import socket, threading
import os.path
articles = []
articles = makeArticles()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '0.0.0.0'
server_port = 80
server.bind((server_ip, server_port))
server.listen(5)

while True:
    client_socket, client_address = server.accept()
    print 'Connection from: ', client_address
    data = client_socket.recv(1024)
    #print data

    line = data.split('\n')
    flag1 = False
    # print data
    if len(line) >= 3:
        flag1 = True
        lastLine = line[-3]
        #    print lastLine
    line = line[0] #Take only the GET request
    print line
    file_path = line.split(' ')
    if len (file_path) <= 2:
        client_socket.close()
        continue
    file_path = file_path[1]  #take only the request
    file_path = file_path[1:] #no / at start


    isHomepage = False
    num = 0
    if not file_path.startswith('Files/') and not file_path.startswith('files/'):
        if file_path.startswith('homepage'):
            isHomepage = True
            if "?id=" in file_path:
                num = file_path.split('=') #Split it to get id
                num = num[1] #take the id
            file_path = "template.html"

            #print isHomepage
        file_path = 'Files/' + file_path
    print file_path
    try:
        with open(file_path, "rb") as f:
            print "yes for ", file_path
            output = f.read()
            size = str(len(output))

            # In case that we just reload, the browser will ask if the file was modified.
            # I decided to return that the file wasn't modified for all "normal reloads".
            # Of course, in real-process we need to check wether the file has changed or not,
            # But thats not the point of the exc., so I decided to send 304 for each time the browser
            # has a version of the file in it's cache
            if flag1:
                print "DDDDDDDD"
                print lastLine
                if lastLine.startswith('If-Modified-Since'):
                    status = "304 Not Modified"
                    # header = addFields(status, file_path, size)
                    # print status
                    header = """HTTP/1.1 304 Not Modified
Connection: close
Content-Type: text/html

<html>
  <body>
  </body>
</html>"""
                    client_socket.send(header)
                    print "Waiting for a massage"
                    client_socket.close()
                    continue

            if isHomepage:
                if "<div class=\"row\">" in output:
                    # print "Yes CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC"
                    parts = output.split("<section id=\"feature\" >")
                    firstPart = parts[0]
                    parts = parts[1].split("</div><!--/.row-->")
                    thirdPart = parts[1]
                    secondPart = "<section id=\"feature\" >" + parts[0] + "</div><!--/.row-->"
                    # print secondPart
                    dynamicPart = secondPart.split("</div>", 1)
                    secondPart = dynamicPart[0] + "</div>"
                    #                    print secondPart
                    dynamicPart = dynamicPart[1]  # take only from <div class = "row">
                    # dynamicPart = dynamicPart[2:] #skipping the '\n' that created by split
                    # parts = parts[0]
                    # print dynamicPart
                    # print "PPPPPPPPPPPPPP"
                    s = "\n"
                    for i in range (0, int(num)):
                        duplicate = makeChange(dynamicPart, i)
                        s += duplicate
                        s = s.strip()
                    print "AD KANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN"
                    print s
                    print "NNNNNNNNNN"
                    l = []
                    l.append(firstPart)
                    l.append(secondPart)
                    l.append(s)
                    l.append(thirdPart)
                    output = ''.join(l)
                else:
                    print "no CCCCCCCCCCCCCCCCCCC"
            size = str(len(output))
            #print output
            print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
            header = addFields(file_path, size)
            cAll = header + '\n' + output
            #print cAll
            #print http_respone
            client_socket.send(cAll)
    except:
        print "no for",file_path
        status = "HTTP/1.1 404 Not Found"
        header = """HTTP/1.1 404 Not Found
Connection: close
Content-Type: text/html

<html>
  <body>
      Not Found
  </body>
</html>"""
        # header = addFields(status, file_path, '0')
        # print status
        # print header
        client_socket.send(header)
        #print status
        #client_socket.send(status)


    print "Waiting for a massage"
    client_socket.close()

