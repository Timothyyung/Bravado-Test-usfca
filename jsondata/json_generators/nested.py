

import json, string, random,sys

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def difficulty_generator():
	difficulty = ['Easy', 'Normal', 'Hard']
	return random.choice(difficulty)

def student_generator(size):
    students = []
    for i in range(size):
        students.append({
	    'studentName': id_generator()
	})
    return students


def make_json(size):
    data = {}
    data['Classes'] = []
    for x in range(0,int(size)):
        data['Classes'].append({
            'className': id_generator(),
            'difficulty': difficulty_generator(),
            'optional': True,
            'students': student_generator(random.choice(range(10)))
        })
    with open('../nested.txt', 'w') as outfile:
        json.dump(data,outfile)


if __name__ == "__main__":
    print (sys.argv)
    make_json(sys.argv[1])

