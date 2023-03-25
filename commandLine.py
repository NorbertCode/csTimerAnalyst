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
            except:
                print('Invalid file path. Please try again.')
        print('\nEnter \'help\' to get a list of all available commands.')
        while True:
            command, args = input().split(' -') # todo: this throws an error if it cant split
            if command == 'help':
                self.Help()
            elif command == 'timesgraph':
                ao = []
                for i in args.split(','):
                    ao.append(int(i))
                self.analyser.ShowTimesGraph(ao)
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