#!/usr/bin/python
# -*- coding: utf-8 -*-

import PySide
from source.generator.data_generator import DataGenerator
import numpy
from itertools import chain
from operator import itemgetter
from source.enums import AnswerState
from random import shuffle
from PySide import QtGui


class Actions(object):
    # Staticke promjenljive koje sadrze generator primjera i konkretan primjer
    data_generator = DataGenerator('../docs/generated-examples.csv')
    figures = data_generator.generate_data()

    @staticmethod
    def generate_figures():
        Actions.figures = Actions.data_generator.generate_data()
        return Actions.figures

    @staticmethod
    def accept_example(answer_a, answer_b, answer_c, answer_d):
        window = PySide.QtCore.QCoreApplication.instance().main_window
        if window.checked is None:
            QtGui.QMessageBox.information(window, window.tr("Informacija"),
                                          window.tr("Niste selektovali nijedan odgovor"),
                                          QtGui.QMessageBox.Accepted)
        else:
            probabilities = Actions.answers_probability(answer_a, answer_b, answer_c, answer_d)
            sorted_prob = sorted(probabilities.items(), key=itemgetter(1))

            mapped = Actions.mapped_answers(sorted_prob[3][0], answer_a, answer_b, answer_c, answer_d)
            if mapped == window.checked:
                window.checked.state = AnswerState.CORRECT
            else:
                window.checked.state = AnswerState.WRONG
                mapped.state = AnswerState.CORRECT
                mapped.repaint()

            # disable click when user chose answer
            if(answer_a.state == AnswerState.NOT_CHECKED):
                answer_a.state = AnswerState.FINISHED
            if (answer_b.state == AnswerState.NOT_CHECKED):
                answer_b.state = AnswerState.FINISHED
            if (answer_c.state == AnswerState.NOT_CHECKED):
                answer_c.state = AnswerState.FINISHED
            if (answer_d.state == AnswerState.NOT_CHECKED):
                answer_d.state = AnswerState.FINISHED

            window.checked.repaint()

    @staticmethod
    def reject_example(canvas, answer_a, answer_b, answer_c, answer_d):
        generated = Actions.generate_figures()
        answers = DataGenerator.create_answers(generated[0], generated[1], generated[2], generated[3], generated[4],
                                               generated[5])

        shuffled_list = [generated[6:], answers[:2], answers[2:4], answers[4:]]
        shuffle(shuffled_list)

        answer_a._figures = shuffled_list[0]
        answer_b._figures = shuffled_list[1]
        answer_c._figures = shuffled_list[2]
        answer_d._figures = shuffled_list[3]

        answer_a.repaint()
        answer_b.repaint()
        answer_c.repaint()
        answer_d.repaint()

        canvas.repaint()
        Actions.reset_answers()

    @staticmethod
    def predict_answer():
        model = PySide.QtCore.QCoreApplication.instance().model

        figures = list(chain(Actions.figures[:6]))

        input_list = []
        for figure in figures:
            input_list = input_list + figure.get_attributes()

        num_input = numpy.array(input_list)[None]
        return model.predict_on_batch(num_input)[0]

    @staticmethod
    def fifty_help(answer_a, answer_b, answer_c, answer_d):
        probabilities = Actions.answers_probability(answer_a, answer_b, answer_c, answer_d)
        sorted_prob = sorted(probabilities.items(), key=itemgetter(1))

        main_window = PySide.QtCore.QCoreApplication.instance().main_window

        for fig in sorted_prob[:2]:
            figure = Actions.mapped_answers(fig[0], answer_a, answer_b, answer_c, answer_d)
            if figure == main_window.checked:
                main_window.checked = None
            figure.state = AnswerState.INVALID
            figure.repaint()

    @staticmethod
    def mapped_answers(answer, answer_a, answer_b, answer_c, answer_d):
        if answer == "a":
            return answer_a
        elif answer == "b":
            return answer_b
        elif answer == "c":
            return answer_c
        elif answer == "d":
            return answer_d
        else:
            return None

    @staticmethod
    def answers_probability(answer_a, answer_b, answer_c, answer_d):
        predict_values = Actions.predict_answer()

        errors = []
        errors.append(Actions.calc_error(answer_a._figures, predict_values))
        errors.append(Actions.calc_error(answer_b._figures, predict_values))
        errors.append(Actions.calc_error(answer_c._figures, predict_values))
        errors.append(Actions.calc_error(answer_d._figures, predict_values))

        total_inverted = sum(errors)
        inverted_percentages = [i / total_inverted for i in errors]
        percentages = [1 - i for i in inverted_percentages]
        total = sum(percentages)

        final = [i / total for i in percentages]
        return {'a': final[0], 'b': final[1], 'c': final[2], 'd': final[3]}

    @staticmethod
    def calc_error(answer, predict_values):
        figure_ans1 = answer[0]
        figure_ans2 = answer[1]

        diffs = [a - b for a, b in zip(predict_values, (figure_ans1.get_attributes() + figure_ans2.get_attributes()))]

        return sum(x ** 2 for x in diffs)

    @staticmethod
    def reset_answers():
        if not hasattr(PySide.QtCore.QCoreApplication.instance(), 'main_window'):
            return

        window = PySide.QtCore.QCoreApplication.instance().main_window
        answers = window.answers

        for answer in answers:
            if answer.state != AnswerState.NOT_CHECKED:
                answer.state = AnswerState.NOT_CHECKED

        # reset names
        names = ["A", "B", "C", "D"]
        for i in xrange(len(answers)):
            answers[i]._name = names[i]
            answers[i].repaint()

        window.checked = None

    @staticmethod
    def probability_help(answer_a, answer_b, answer_c, answer_d):
        probabilities = Actions.answers_probability(answer_a, answer_b, answer_c, answer_d)
        answer_a._name = str("%.1f%%" % (probabilities["a"] * 100))
        answer_b._name = str("%.1f%%" % (probabilities["b"] * 100))
        answer_c._name = str("%.1f%%" % (probabilities["c"] * 100))
        answer_d._name = str("%.1f%%" % (probabilities["d"] * 100))

        answer_a.repaint()
        answer_b.repaint()
        answer_c.repaint()
        answer_d.repaint()
