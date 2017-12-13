class Resource:
    def __init__(self, link, picture, title, content):
        self.link = link
        self.picture = picture
        self.title = title
        self.content = content

    def GetLink(self):
        return self.link

    def GetPicture(self):
        return self.picture

    def GetTitle(self):
        return self.title

    def GetContent(self):
        return self.content
