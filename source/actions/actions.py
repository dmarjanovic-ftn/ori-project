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
        print Actions.figures[0]
        output_file.write(str(Actions.figures[0]) + "\n")
        Actions.generate_figures()
        canvas.repaint()
        output_file.close()

    @staticmethod
    def reject_example(canvas):
        Actions.generate_figures()
        canvas.repaint()
