# class that holds our types we can send in HTTP request
class Mappings:
    def __init__(self):
        self.dic = dict()
        self.CreateDict()

    # create our dictionary
    def CreateDict(self):
        # text type
        self.dic["plain"] = "text"
        self.dic["html"] = "text"
        self.dic["css"] = "text"
        self.dic["javascript"] = "text"

        # text image
        self.dic["gif"] = "image"
        self.dic["png"] = "image"
        self.dic["jpeg"] = "image"
        self.dic["bmp"] = "image"
        self.dic["webp"] = "image"
        self.dic["jpg"] = "image"

        # text audio
        self.dic["midi"] = "audio"
        self.dic["mpeg"] = "audio"
        self.dic["webm"] = "audio"
        self.dic["ogg"] = "audio"
        self.dic["wav"] = "audio"

        # text video
        self.dic["webm"] = "video"
        self.dic["ogg"] = "video"

        # text application
        self.dic["octet-stream"] = "application"
        self.dic["pkcs12"] = "application"
        self.dic["vnd.mspowerpoint"] = "application"
        self.dic["xhtml+xml"] = "application"
        self.dic["xml"] = "application"
        self.dic["js"] = "application"

        # text font
        self.dic["otf"] = "font"
        self.dic["eot"] = "font"
        self.dic["svg"] = "font"
        self.dic["ttf"] = "font"
        self.dic["woff"] = "font"

    # get the list that holds our dictionary
    def getMappingsDictionary(self):
        return self.dic
