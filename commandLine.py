import analyser as an

class CommandLine:
    def __init__(self):
        while True:
            try:
                fileName = input('Please enter the path to your session file: ')
                self.analyser = an.Analyser(fileName)
                break
            except:
                print('Invalid file path. Please try again.')
        print('\nEnter \'help\' to get a list of all available commands.')
        while True:
            userInput = input('> ').split(' ')
            command = userInput[0]
            args = userInput[1] if len(userInput) > 1 else ''

            if command == 'help':
                self.Help()

            elif command == 'timesgraph':
                if args != '':
                    try:
                        ao = []
                        for i in args.split(','):
                            ao.append(int(i))
                        self.analyser.ShowTimesGraph(ao)
                    except:
                        print('Invalid arguments. Please make your you didn\'t put spaces between them.')
                else:
                    self.analyser.ShowTimesGraph()

            elif command == 'solvesbydate':
                self.analyser.ShowSolvesByDayGraph()

            elif command == 'load':
                if args != '':
                    self.LoadFile(args)
                else:
                    print('Please specify the file path.')

            elif command =='exit':
                break

            else:
                print('Invalid command')

    def LoadFile(self, path):
        try:
            self.analyser = an.Analyser(path)
        except:
            print('Invalid file path. Please try again.')

    def Help(self):
        print('timesgraph args     -Shows a graph of all singles times and averages specificed in args (e.g. timesgraph 5,12,100). If arguments are left empty it defaults to 5 and 12',
              'solvesbydate     -Shows a graph of solves and total times by date',
              'load path     -Loads the session csv file at the given path (e.g. load 3x3.csv)'
              'exit    -Exits the program',
              'help     -List of all commands',
              sep='\n')


if __name__ == '__main__':
    CommandLine()