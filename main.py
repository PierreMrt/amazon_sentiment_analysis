import sys
import run

if __name__ == '__main__':

    # sys.argv = ['', 'test_model']
    func = sys.argv[1]

    try:
        method = run.__dict__.get(func)
        method()
    except TypeError:
        print("Selected functionality does not exist. Please select from the following:\n"
              "* scraping\n"
              "* cleaning\n"
              "* create_models\n"
              "* test_model\n"
              "* data_exploration\n"
              "* analyze_results\n\n"
              "Syntax: python main.py scraping")

