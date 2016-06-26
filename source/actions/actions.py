from source.generator.data_generator import DataGenerator


class Actions(object):

    # Staticke promjenljive koje sadrze generator primjera i konkretan primjer
    data_generator = DataGenerator('../docs/generated-examples.csv')
    figures = data_generator.generate_data()

    @staticmethod
    def generate_figures():
        Actions.figures = Actions.data_generator.generate_data()
        return Actions.figures

    @staticmethod
    def accept_example(canvas):
        """
        Funkcija koja prima roditelja na kom se figure iscratavaju.
        Otvara datoteku i upisuje test primjer u fajl.
        """
        output_file = open(Actions.data_generator.output, 'a')

        row_data = ""
        for figure in Actions.figures:
            row_data += str(figure) + ","

        output_file.write(row_data[:-1] + "\n")

        Actions.generate_figures()
        canvas.repaint()
        output_file.close()

    @staticmethod
    def reject_example(canvas):
        Actions.generate_figures()
        canvas.repaint()
