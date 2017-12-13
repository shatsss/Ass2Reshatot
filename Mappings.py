class Mappings:
    def __init__(self):
        self.dic = dict()
        self.CreateDict()

    def CreateDict(self):
        self.dic["plain"] = "text"
        self.dic["html"] = "text"
        self.dic["css"] = "text"
        self.dic["javascript"] = "text"

        self.dic["gif"] = "image"
        self.dic["png"] = "image"
        self.dic["jpeg"] = "image"
        self.dic["bmp"] = "image"
        self.dic["webp"] = "image"
        self.dic["jpg"] = "image"

        self.dic["midi"] = "audio"
        self.dic["mpeg"] = "audio"
        self.dic["webm"] = "audio"
        self.dic["ogg"] = "audio"
        self.dic["wav"] = "audio"

        self.dic["webm"] = "video"
        self.dic["ogg"] = "video"

        self.dic["octet-stream"] = "application"
        self.dic["pkcs12"] = "application"
        self.dic["vnd.mspowerpoint"] = "application"
        self.dic["xhtml+xml"] = "application"
        self.dic["xml"] = "application"
        self.dic["js"] = "application"

        self.dic["otf"] = "font"
        self.dic["eot"] = "font"
        self.dic["svg"] = "font"
        self.dic["ttf"] = "font"
        self.dic["woff"] = "font"

    def getMappingsDictionary(self):
        return self.dic
