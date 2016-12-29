#document class
class Document:
    def __init__(self, name):    
        self.name = name
 
    def show(self):             
        raise NotImplementedError("Subclass must implement abstract method")

#pdf class inheriting document class
class Pdf(Document):
    def show(self):
        return 'Show pdf contents!'

#word class inheriting document class
class Word(Document):
    def show(self):
        return 'Show word contents!'
 
documents = [Pdf('Document1'),
             Pdf('Document2'),
             Word('Document3')]

#same method from document class is called but different outputs
for document in documents:
    print(document.name + ': ' + document.show())
