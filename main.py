import sys
import run

if __name__ == '__main__':

    sys.argv = ['', 'data_exploration']
    func = sys.argv[1]

    method = run.__dict__.get(func)
    method()



