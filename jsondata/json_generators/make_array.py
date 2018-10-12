import json, string, random, sys

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):

    return ''.join(random.choice(chars) for _ in range(size))


def make_json(size):
    data = {}
    data['Persons'] = []
    print("making json with size" + size)
    for x in range(0,int(size)):
        data['Persons'].append({
            'firstName': id_generator(),
            'lastName': id_generator(),
            'username': id_generator()
            })
    with open('../array.txt', 'w') as outfile:
        json.dump(data,outfile)

if __name__ == "__main__":
    print (sys.argv)
    make_json(sys.argv[1])

