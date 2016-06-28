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
    def reject_example(canvas, answer_a, answer_b, answer_c, answer_d):
        generated = Actions.generate_figures()
        answers = DataGenerator.create_answers(generated[0], generated[1], generated[2], generated[3], generated[4], generated[5])

        answer_a._figures = generated[6:]
        answer_b._figures = answers[:2]
        answer_c._figures = answers[2:4]
        answer_d._figures = answers[4:]

        answer_a.repaint()
        answer_b.repaint()
        answer_c.repaint()
        answer_d.repaint()

        canvas.repaint()
