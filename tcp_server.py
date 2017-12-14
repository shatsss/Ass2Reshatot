import socket
from datetime import datetime

from DB import DB
from Mappings import Mappings

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '0.0.0.0'
server_port = 80
server.bind((server_ip, server_port))
server.listen(5)


def DeleteParams(data):
    try:
        req = data.split("?")[0]
    except:
        req = data
    return req


def CheckTypeOfRequest(data):
    try:
        strOfData = data = data.split("?")[0]
    except:
        strOfData = data
    try:
        word_list = strOfData.split(".")
        return word_list[-1]
    except:
        return None


def GetRequestFromClient(data):
    try:
        return data.split(" ")[1].split("/", 1)[1]
    except:
        return None


def get_date():
    return datetime.today().strftime('%a, %m %b %Y %H:%M:%S')


def makeStatic(req, type):
    req = DeleteParams(req)
    if type is None or req is None:
        res = CreateResponse('HTTP/1.1', '404 Not Found', 'close', 'text', 'html', 'Not Found', True)
    else:
        if type == 'js':
            type = "javascript"
        try:
            file = open(req, "rb")
            content = file.read()
            res = CreateResponse('HTTP/1.1', '200 OK', 'close', mappings.getMappingsDictionary()[type],
                                 type, content, True)
        except:
            try:
                file = open("Files/" + req, "rb")
                content = file.read()
                res = CreateResponse('HTTP/1.1', '200 OK', 'close', mappings.getMappingsDictionary()[type], type,
                                     content, True)
            except:
                res = CreateResponse('HTTP/1.1', '404 Not Found', 'close', 'text', 'html', 'Not Found', True)
    return res


def trySplitParamsDynamic(req):
    try:
        array = req.split("?")
        try:
            return array[0], array[1].split("=")[1]
        except:
            return array[0], 0
    except:
        return None, 0


def MakeDynamicPage(file, numberOfArticles):
    numberOfArticles = int(numberOfArticles)
    if db.GetLength() < numberOfArticles:
        numberOfArticles = db.GetLength()

    section_Id_Start = '<section id="feature" >'
    section_Id_End = '</section><!--/#feature-->'
    section_Row_Begin = '<div class="row">'
    section_Row_End = '</div><!--/.row-->'

    # get the code we want to duplicate
    # split feature
    before_section_Id_Start, _, after_section_Id_Start = file.partition(section_Id_Start)
    # split end feature
    before_section_Id_End, _, after_section_Id_End = after_section_Id_Start.partition(section_Id_End)
    # split row
    before_section_Row_Begin, _, after_section_Row_Begin = before_section_Id_End.partition(section_Row_Begin)
    # split end row
    before_section_Row_End, _, after_section_Row_End = after_section_Row_Begin.partition(section_Row_End)

    res = ''
    for i in range(numberOfArticles):
        resource = db.GetList(i)
        res += section_Row_Begin + before_section_Row_End.replace('Title', resource.title).replace('Content',
                                                                                                   resource.content).replace(
            'link', resource.link).replace('src=""', 'src="' + resource.picture + '"') + section_Row_End

    # create all the html file
    res = before_section_Id_Start + section_Id_Start + before_section_Row_Begin + \
          res + after_section_Row_End + section_Id_End + after_section_Id_End
    return res


def makeDynamic(numberOfArticles):
    try:
        file = open('Files/template.html', "rb").read()
        if numberOfArticles == 0:
            res = CreateResponse('HTTP/1.1', '200 OK', 'close', 'text', 'html', file, True)
        else:
            data = MakeDynamicPage(file, numberOfArticles)
            res = CreateResponse('HTTP/1.1', '200 OK', 'close', 'text', 'html', data, False)
    except:
        res = CreateResponse('HTTP/1.1', '404 Not Found', 'close', 'text', 'html', 'Not Found', True)
    return res


def SendReq(req, type):
    req1, numberOfArticles = trySplitParamsDynamic(req)
    if req is not None and req1 == "homepage":
        return makeDynamic(numberOfArticles)
    else:
        return makeStatic(req, type)


def Create304Response():
    return CreateResponse('HTTP/1.1', '304 Not Modified', 'close', 'text', 'html', 'Not Modified', True)


def MakeResponse(data):
    if 'If-Modified-Since' in data:
        return Create304Response()
    req = GetRequestFromClient(data)
    type = None
    if req is not None:
        type = CheckTypeOfRequest(req)
    return SendReq(req, type)


def CreateResponse(version, resNum, connection, type1, type2, data, modifiedSinceFlag):
    res = version + ' ' + resNum + '\n' + 'Date: ' + get_date() + ' GMT\n' + 'Content-Length: ' + \
          str(len(data)) + '\n' + 'Connection: ' + connection + '\n'
    if modifiedSinceFlag is True:
        res += 'Last-Modified: ' + startDate + 'GMT\n'
    res += 'Content-Type: ' + type1 + '/' + type2 + '\n\n' + data
    return res


# the main of the program, DNS server- return the answer to the client
def main():
    global db, startDate, mappings
    startDate = get_date()
    db = DB()
    mappings = Mappings()
    # create dict of types
    while True:
        client_socket, client_address = server.accept()
        print "Client Connect: ", client_address
        data = client_socket.recv(1024)
        print data
        while not data == '':
            res = MakeResponse(data)
            client_socket.send(res)
            data = client_socket.recv(1024)
        print('Client disconnected')
        client_socket.close()  # main of the server


# the main of the program
if __name__ == '__main__':
    main()
