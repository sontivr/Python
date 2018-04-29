from operator import itemgetter

def person_lister(f):
    def inner(people):
      # complete the function
      for i in range(len(people)):
        people[i][2] = int(people[i][2])

      people.sort(key = itemgetter(2))
      for person in people:
        yield f(person)
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
    #print(people)


'''
3
Mike Thomson 20 M
Robert Bustle 32 M
David Mugabe 32 M
Andria Bustle 30 F
'''
