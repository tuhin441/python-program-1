class phone():
    def message(self):
        print('This is a text message')

    def call(self):
        print('It is a voice call')

class samsung(phone): #phone class is inherited.
    def camera(self):
        print('You can take picture')

    def youtube(self):
        print('You can watch video content here')

#p = phone()
#p.message()
#p.call()
q=samsung()
q.camera()
q.youtube()
q.message()
q.call()