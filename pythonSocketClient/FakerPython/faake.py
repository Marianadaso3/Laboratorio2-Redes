from faker import Faker

fakeInstance = Faker()
Faker.seed(4321)

def getRandomSentence():
    return fakeInstance.paragraph(nb_sentences=5)
