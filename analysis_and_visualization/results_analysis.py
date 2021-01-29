from matplotlib import pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
from model_creation.model_manager import ModelManager


class ResultsAnalysis:
    def __init__(self):
        manager = ModelManager(None)
        self.models = manager.load_models()

    @staticmethod
    def plot_results(model, matrix, score, test):
        if test:
            title = 'Against new reviews:\n'
        else:
            title = 'Against training reviews:\n'

        title += f"model : {model.name}\n" \
            f"accuracy score : {round(score * 100, 2)}%"

        cmd = ConfusionMatrixDisplay(matrix, display_labels=['Negative', 'Positive'])
        cmd.plot(cmap='Blues')
        cmd.ax_.set(xlabel='Predicted', ylabel='True')
        plt.title(title)
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')
        plt.show()

    def show_results(self, test):
        for model in self.models:
            if test and model.test_matrix is not None:
                matrix = model.test_matrix
                score = model.test_score
            elif test and model.test_matrix is None:
                continue
            else:
                matrix = model.confusion_matrix
                score = model.score

            self.plot_results(model, matrix, score, test)


def results():
    analyzer = ResultsAnalysis()

    analyzer.show_results(test=False)
    analyzer.show_results(test=True)
