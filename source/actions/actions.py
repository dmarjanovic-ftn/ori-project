from source.generator.data_generator import DataGenerator


class Actions(object):

    data_generator = DataGenerator('output.txt')
    figures = data_generator.generate_data()

    @staticmethod
    def generate_figures():
        Actions.figures = Actions.data_generator.generate_data()
        return Actions.figures

    @staticmethod
    def accept_example(canvas):
        output_file = open(Actions.data_generator.output, 'a')
        for figure in Actions.figures:
            output_file.write(str(figure) + ", ")
        output_file.write("\n")
        Actions.generate_figures()
        canvas.repaint()
        output_file.close()

    @staticmethod
    def reject_example(canvas):
        Actions.generate_figures()
        canvas.repaint()
