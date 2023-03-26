import analyser as an
import overallStats as os
import times

class CommandLine:
    def __init__(self):
        while True:
            try:
                fileName = input('Please enter the path to your session file: ')
                self.analyser = an.Analyser(fileName)
                break
            except Exception as e:
                print('Invalid file path. Please try again.')
                print(e)
        print('\nEnter \'help\' to get a list of all available commands.')
        while True:
            userInput = input().split(' -') # todo: this throws an error if it cant split
            command = userInput[0]
            args = userInput[1] if len(userInput) > 1 else ''
            if command == 'help':
                self.Help()
            elif command == 'timesgraph':
                if args != '':
                    ao = []
                    for i in args.split(','):
                        ao.append(int(i))
                    self.analyser.ShowTimesGraph(ao)
                else:
                    self.analyser.ShowTimesGraph()
            elif command == 'solvesbydate':
                self.analyser.ShowSolvesByDayGraph()
            elif command =='exit':
                break
            else:
                print('Invalid command')

    def Help(self):
        print('timesgraph -args     -Shows a graph of all singles times and averages specificed in args (e.g. timesgraph -5,12,100)\n',
              'solvesbydate     -Shows a graph of solves and total times by date\n',
              'exit    -Exits the program\n',
              'help     -List of all commands\n',
              sep='')


if __name__ == '__main__':
    CommandLine()