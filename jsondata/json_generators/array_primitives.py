import json, string, random, sys

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):

    return ''.join(random.choice(chars) for _ in range(size))

def make_json(size):
    data = {}
    data['guests'] = []
    print("making json with size" + size)
    for x in range(0,int(size)):
        data['guests'].append(id_generator())
    with open('../array_primitives10k.txt', 'w') as outfile:
        json.dump(data,outfile)

if __name__ == "__main__":
    print (sys.argv)
    make_json(sys.argv[1])
