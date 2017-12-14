import socket
from datetime import datetime

from DB import DB
from Mappings import Mappings

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '0.0.0.0'
server_port = 80
server.bind((server_ip, server_port))
server.listen(5)


# delete the params of the static request
def DeleteParams(data):
    try:
        req = data.split("?")[0]
    except:
        req = data
    return req


# check the type of the request
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


# get the path the client asks
def GetRequestFromClient(data):
    try:
        return data.split(" ")[1].split("/", 1)[1]
    except:
        return None


# get the time now
def get_date():
    return datetime.today().strftime('%a, %m %b %Y %H:%M:%S')


# make static response to the client
def makeStatic(req, type):
    req = DeleteParams(req)
    if type is None or req is None:
        res = CreateResponse('HTTP/1.1', '404 Not Found', 'close', 'text', 'html', 'Not Found')
    else:
        if type == 'js':
            type = "javascript"
        try:
            filePath = open(req, "rb")
            content = filePath.read()
            res = CreateResponse('HTTP/1.1', '200 OK', 'close', mappings.getMappingsDictionary()[type],
                                 type, content)
        except:
            try:
                filePath = open("Files/" + req, "rb")
                content = filePath.read()
                res = CreateResponse('HTTP/1.1', '200 OK', 'close', mappings.getMappingsDictionary()[type], type,
                                     content)
            except:
                res = CreateResponse('HTTP/1.1', '404 Not Found', 'close', 'text', 'html', 'Not Found')
    return res


# try to get params for dynamic request
def trySplitParamsDynamic(req):
    try:
        array = req.split("?")
        try:
            return array[0], array[1].split("=")[1]
        except:
            return array[0], 0
    except:
        return None, 0


# create the dynamic page with numberOfArticles articles
def MakeDynamicPage(filePath, numberOfArticles):
    numberOfArticles = int(numberOfArticles)
    if db.GetLength() < numberOfArticles:
        numberOfArticles = db.GetLength()

    # the lines in html we split with their help
    section_Id_Start = '<section id="feature" >'
    section_Id_End = '</section><!--/#feature-->'
    section_Row_Begin = '<div class="row">'
    section_Row_End = '</div><!--/.row-->'

    # get the code we want to duplicate

    # split feature
    before_section_Id_Start, _, after_section_Id_Start = filePath.partition(section_Id_Start)
    # split end feature
    before_section_Id_End, _, after_section_Id_End = after_section_Id_Start.partition(section_Id_End)
    # split row
    before_section_Row_Begin, _, after_section_Row_Begin = before_section_Id_End.partition(section_Row_Begin)
    # split end row
    before_section_Row_End, _, after_section_Row_End = after_section_Row_Begin.partition(section_Row_End)

    res = ''
    # add the articles to the html page
    for i in range(numberOfArticles):
        resource = db.GetList(i)
        res += section_Row_Begin + \
               before_section_Row_End. \
                   replace('Title', resource.title). \
                   replace('Content', resource.content). \
                   replace('link', resource.link). \
                   replace('src=""', 'src="' + resource.picture + '"') + section_Row_End

    # create all the html filePath
    res = before_section_Id_Start + section_Id_Start + before_section_Row_Begin + \
          res + after_section_Row_End + section_Id_End + after_section_Id_End
    return res


# if its dynamic request that create dynamic request
def makeDynamic(numberOfArticles):
    try:
        filePath = open('Files/template.html', "rb").read()
        if numberOfArticles == 0:
            res = CreateResponse('HTTP/1.1', '200 OK', 'close', 'text', 'html', filePath)
        else:
            data = MakeDynamicPage(filePath, numberOfArticles)
            res = CreateResponse('HTTP/1.1', '200 OK', 'close', 'text', 'html', data)
    except:
        res = CreateResponse('HTTP/1.1', '404 Not Found', 'close', 'text', 'html', 'Not Found')
    return res


# check if its dynamic request or static
def SendReq(req, type):
    req1, numberOfArticles = trySplitParamsDynamic(req)
    if req is not None and req1 == "homepage":
        return makeDynamic(numberOfArticles)
    else:
        return makeStatic(req, type)


# create is-modified response to the client' because the client have this filePath
def Create304Response():
    return CreateResponse('HTTP/1.1', '304 Not Modified', 'close', 'text', 'html', 'Not Modified')


# check if the filePath in the cache of the client or not
# if not we take the filePath and the type and search
def MakeResponse(data):
    # check if in the cache
    if 'If-Modified-Since' in data:
        return Create304Response()
    req = GetRequestFromClient(data)
    type = None
    if req is not None:
        type = CheckTypeOfRequest(req)
    return SendReq(req, type)


# the format we send response to the client side
def CreateResponse(version, resNum, connection, type1, type2, data):
    res = version + ' ' + resNum + '\n' + 'Date: ' + get_date() + ' GMT\n' + 'Content-Length: ' + \
          str(len(data)) + '\n' + 'Connection: ' + connection + '\n' + \
          'Last-Modified: ' + get_date() + 'GMT\n' + 'Content-Type: ' + type1 + '/' + type2 + '\n\n' + data
    return res


# the main of the program, our Server side application
def main():
    global db, mappings
    db = DB()
    # create dict of types
    mappings = Mappings()
    while True:
        client_socket, client_address = server.accept()
        print "Client Connect: ", client_address
        data = client_socket.recv(1024)
        print data
        while not data == '':
            # make the response in HTTP protocol to the client
            res = MakeResponse(data)
            client_socket.send(res)
            data = client_socket.recv(1024)
        print('Client disconnected')
        client_socket.close()  # main of the server


# the main of the program
if __name__ == '__main__':
    main()
