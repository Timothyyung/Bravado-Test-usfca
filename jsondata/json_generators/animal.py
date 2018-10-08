import json, string, random, sys

def id_generator(size=5000, chars=string.ascii_uppercase + string.digits):

    return ''.join(random.choice(chars) for _ in range(size))


def make_json(size):
    data = {}
    data['Animals'] = []
    print("making json with size" + size)
    for x in range(0,int(size)):
        data['Animals'].append({
            'gender':  "undefined",
            'animaltype': "tiger",
            'animalname': id_generator(),
            'id' : 0
            })
    with open('../animal.txt', 'w') as outfile:
        json.dump(data,outfile)

if __name__ == "__main__":
    print (sys.argv)
    make_json(sys.argv[1])
