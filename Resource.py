# class that represents dynamic resource
class Resource:
    def __init__(self, link, picture, title, content):
        self.link = link
        self.picture = picture
        self.title = title
        self.content = content

    # get the link of the resource
    def GetLink(self):
        return self.link

    # get the picture of the resource
    def GetPicture(self):
        return self.picture

    # get the title of the resource
    def GetTitle(self):
        return self.title

    # get the content of the resource
    def GetContent(self):
        return self.content
