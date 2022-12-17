def leggi_file(filename):
    try:
        data = []
        file = open(filename, 'r', encoding='utf-8')
        for line in file:
            line = line.replace('\n', '')
            if len(line.split(' ')) != 1:
                data.append(line.split(' '))
            else:
                data.append(line)
        file.close()
        return data
    except IOError:
        exit(f'Impossibile aprire il file {filename}')


def main():
    classes = leggi_file('classes.txt')
    classes_data = dict()

    for klass in classes:
        classes_data[klass] = leggi_file(f'{klass}.txt')

    student_id = input('Student ID: ')

    for klass in classes_data:
        data = classes_data[klass]

        for record in data:
            if record[0] == student_id:
                print(klass, record[1])


if __name__ == '__main__':
    main()
