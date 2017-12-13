import socket
from datetime import datetime

from DB import DB

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '0.0.0.0'
server_port = 80
server.bind((server_ip, server_port))
server.listen(5)


def CreateDictionary():
    dic["plain"] = "text"
    dic["html"] = "text"
    dic["css"] = "text"
    dic["javascript"] = "text"

    dic["gif"] = "image"
    dic["png"] = "image"
    dic["jpeg"] = "image"
    dic["bmp"] = "image"
    dic["webp"] = "image"
    dic["jpg"] = "image"

    dic["midi"] = "audio"
    dic["mpeg"] = "audio"
    dic["webm"] = "audio"
    dic["ogg"] = "audio"
    dic["wav"] = "audio"

    dic["webm"] = "video"
    dic["ogg"] = "video"

    dic["octet-stream"] = "application"
    dic["pkcs12"] = "application"
    dic["vnd.mspowerpoint"] = "application"
    dic["xhtml+xml"] = "application"
    dic["xml"] = "application"
    dic["js"] = "application"

    dic["otf"] = "font"
    dic["eot"] = "font"
    dic["svg"] = "font"
    dic["ttf"] = "font"
    dic["woff"] = "font"


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
        res = 'HTTP/1.1 404 Not Found\n' + 'Date: ' + get_date() + ' GMT\r\n' + 'Content-Length: ' + \
              str(len("Not Found\0")) + '\r\n' + 'Connection: close\n' + 'Content-Type: text/html\n\n Not Found'
    else:
        if type == 'js':
            type = "javascript"
        try:
            file = open(req, "rb")
            content = file.read()
            res = 'HTTP/1.1 200 OK\r\n' + 'Date: ' + get_date() + ' GMT\r\n' + 'Content-Length: ' + \
                  str(len(content)) + '\r\n' + 'Connection: close\r\n' + \
                  'Content-Type: ' + dic[type] + '/' + type + '\r\n\r\n' + content
        except:
            try:
                file = open("Files/" + req, "rb")
                content = file.read()
                res = 'HTTP/1.1 200 OK\r\n' + 'Date: ' + get_date() + ' GMT\r\n' + 'Content-Length: ' + \
                      str(len(content)) + '\r\n' + 'Connection: close\r\n' + \
                      'Content-Type: ' + dic[type] + '/' + type + '\r\n\r\n' + content
            except:
                res = 'HTTP/1.1 404 Not Found\n' + 'Date: ' + get_date() + ' GMT\r\n' + 'Content-Length: ' + \
                      str(len("Not Found\0")) + '\r\n' + 'Connection: close\n' + 'Content-Type: text/html\n\n Not Found'
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
        res += before_section_Row_End.replace('Title', resource.title).replace('Content', resource.content).replace(
            'link', resource.link).replace('src=""', 'src="' + resource.picture + '"')

    res = before_section_Id_Start + section_Id_Start + before_section_Row_Begin + section_Row_Begin + res + section_Row_End + after_section_Row_End + section_Id_End + after_section_Id_End
    return res


def makeDynamic(numberOfArticles):
    try:
        file = open('Files/template.html', "rb").read()
        if numberOfArticles == 0:
            res = 'HTTP/1.1 200 OK\r\n' + 'Date: ' + get_date() + ' GMT\r\n' + 'Content-Length: ' + \
                  str(len(file)) + '\r\n' + 'Connection: close\r\n' + \
                  'Content-Type: ' + "text/html\n\n" + file
        else:
            data = MakeDynamicPage(file, numberOfArticles)
            res = 'HTTP/1.1 200 OK\r\n' + 'Date: ' + get_date() + ' GMT\r\n' + 'Content-Length: ' + \
                  str(len(data)) + '\r\n' + 'Connection: close\r\n' + \
                  'Content-Type: ' + "text/html\n\n" + data
    except:
        res = CreateResponse('HTTP/1.1', '404 Not Found', 'close', 'text', 'html', 'Not Found')
        res = 'HTTP/1.1 404 Not Found\n' + 'Date: ' + get_date() + ' GMT\r\n' + 'Content-Length: ' + \
              str(len("Not Found\0")) + '\r\n' + 'Connection: close\n' + 'Content-Type: text/html\n\n Not Found'
    return res


def SendReq(req, type):
    req1, numberOfArticles = trySplitParamsDynamic(req)
    if req is not None and req1 == "homepage":
        return makeDynamic(numberOfArticles)
    else:
        return makeStatic(req, type)


def MakeResponse(data):
    req = GetRequestFromClient(data)
    type = None
    if req is not None:
        type = CheckTypeOfRequest(req)
    print('Received: ', data)
    return SendReq(req, type)


def CreateResponse(version, resNum, connection, type1, type2, data):
    return version + ' ' + resNum + '\n' + 'Date: ' + get_date() + ' GMT\n' + + 'Content-Length: ' + \
           str(len(data)) + '\n' + 'Connection: ' + connection + '\n' + \
           'Content-Type: ' + type1 + '/' + type2 + '\n\n' + data


# the main of the program, DNS server- return the answer to the client
def main():
    global db
    db = DB()
    global dic
    dic = dict()
    # create dict of types
    CreateDictionary()
    while True:
        client_socket, client_address = server.accept()
        data = client_socket.recv(1024)
        while not data == '':
            res = MakeResponse(data)
            client_socket.send(res)
            data = client_socket.recv(1024)
        print('Client disconnected')
        client_socket.close()  # main of the server


# the main of the program
if __name__ == '__main__':
    main()
