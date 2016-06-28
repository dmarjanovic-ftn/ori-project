# -*- coding: utf-8 -*-

from numpy import random
from random import randint
from source.model.figures import Figure
from source.enums import *
from copy import deepcopy

class DataGenerator:
    def __init__(self, output):
        self.output = output
        self.top_left_quadrant = []
        self.top_right_quadrant = []
        self.bottom_left_quadrant = []
        self.bottom_right_quadrant = []
        
    def generate_data(self):
        figure_tlq1, figure_tlq2 = self.get_random_figures(randint(0, 4), randint(0, 4))

        figure_trq1, figure_trq2 = self.get_random_figures(randint(0, 4), randint(0, 4))
        figure_trq1._type = DataGenerator.get_random_mapped_types(figure_tlq1._type)
        figure_trq2._type = DataGenerator.get_random_mapped_types(figure_tlq2._type)
                
        # postavljanje figura iz donjeg lijevog kvadranta na iste pozicije kao u gornjem lijevom
        figure_blq1, figure_blq2 = DataGenerator.get_random_figures(figure_tlq1._position, figure_tlq2._position)

        # analogna figura
        figure_brq1, figure_brq2 = DataGenerator.create_analog(figure_tlq1, figure_tlq2, figure_trq1, figure_trq2, figure_blq1, figure_blq2)

        return [figure_tlq1, figure_tlq2, figure_trq1, figure_trq2, figure_blq1, figure_blq2, figure_brq1, figure_brq2]

    @staticmethod
    def get_random_figures(pos1, pos2):
        figure_pos1 = FigurePosition(pos1)
        figure_orient1 = FigureOrientation(randint(1, 4))
        
        figure_pos2 = FigurePosition(pos2)
        figure_type2 = FigureType(randint(1, 6))
        figure_orient2 = FigureOrientation(randint(1, 4))
        
        if figure_pos1 == figure_pos2:
            figure_type1 = FigureType(random.choice([1, 2, 3, 4]))
            figure_size1 = FigureSize(randint(2, 3))
            figure_size2 = FigureSize(randint(1, 2))

            if figure_size1 == figure_size2:
                figure_size2 = FigureSize(1)
                
        else:
            figure_type1 = FigureType(randint(1, 6))
            figure_size1 = FigureSize(randint(1, 3))
            figure_size2 = FigureSize(randint(1, 3))
        
        figure1 = Figure(figure_type1, figure_pos1, figure_size1, figure_orient1)
        figure2 = Figure(figure_type2, figure_pos2, figure_size2, figure_orient2)

        return [figure1, figure2]

    @staticmethod
    def get_random_mapped_types(fig_type):
        if fig_type == FigureType.ARROW or fig_type == FigureType.LINE:
            return [FigureType.LINE, FigureType.ARROW][randint(0, 1)]
        if fig_type == FigureType.CIRCLE or fig_type == FigureType.SQUARE:
            return [FigureType.CIRCLE, FigureType.SQUARE][randint(0, 1)]
        else:
            return [FigureType.TRIANGLE, FigureType.PIE][randint(0, 1)]

    @staticmethod
    def get_mapped_types(fig_type):
        if fig_type == FigureType.SQUARE:
            return FigureType.CIRCLE
        elif fig_type == FigureType.CIRCLE:
            return FigureType.SQUARE
        elif fig_type == FigureType.ARROW:
            return FigureType.LINE
        elif fig_type == FigureType.LINE:
            return FigureType.ARROW
        elif fig_type == FigureType.PIE:
            return FigureType.TRIANGLE
        else:
            return FigureType.PIE

    @staticmethod
    def create_analog(figure_tl1, figure_tl2, figure_tr1, figure_tr2, figure_bl1, figure_bl2):
        analog_type1 = figure_bl1._type
        analog_position1 = figure_tr1._position
        analog_orientation1 = figure_tr1._orientation 
        
        analog_type2 = figure_bl2._type
        analog_position2 = figure_tr2._position
        analog_orientation2 = figure_tr2._orientation 
         
        f1 = Figure(analog_type1, analog_position1, 0, analog_orientation1)
        f2 = Figure(analog_type2, analog_position2, 0, analog_orientation2)

        DataGenerator.size_translation(figure_tl1, figure_tr1, figure_bl1, f1)
        DataGenerator.size_translation(figure_tl2, figure_tr2, figure_bl2, f2)
        DataGenerator.orientation_analogy(figure_tl1, figure_tr1, figure_bl1, f1)
        DataGenerator.orientation_analogy(figure_tl2, figure_tr2, figure_bl2, f2)
        DataGenerator.type_analogy(figure_tl1, figure_tr1, figure_bl1, f1)
        DataGenerator.type_analogy(figure_tl2, figure_tr2, figure_bl2, f2)

        return [f1, f2]

    @staticmethod
    def type_analogy(in_figure1, in_figure2, in_figure3, out_figure):
        if in_figure1._type == in_figure2._type:
            out_figure._type = in_figure3._type
        else:
            out_figure._type = DataGenerator.get_mapped_types(in_figure3._type)

    @staticmethod
    def size_translation(in_figure1, in_figure2, in_figure3, out_figure):
        """
        Postavljanje analogne velicine za procijenjenu figuru        
        
        Args:        
            in_figure1: figura iz gornjeg lijevog kvadranta
            in_figure2: figura iz gornjeg desnog kvadranta
            in_figure3: figura iz lijevog donjeg kvadranta
            out_figure: izlazna figura
        """
        diff = in_figure1._size.value - in_figure2._size.value
        out_figure._size = in_figure3._size.value - diff

        if out_figure._size < 1:
            out_figure._size = 0
        if out_figure._size > 3:
            out_figure._size = 4

        out_figure._size = FigureSize(out_figure._size)

    @staticmethod
    def orientation_analogy(in_figure1, in_figure2, in_figure3, out_figure):
        """
        Postavljanje analogne velicine za procijenjenu figuru

        Args:
            in_figure1: figura iz gornjeg lijevog kvadranta
            in_figure2: figura iz gornjeg desnog kvadranta
            in_figure3: figura iz lijevog donjeg kvadranta
            out_figure: izlazna figura
        """
        if in_figure1._type == FigureType.SQUARE or in_figure2._type == FigureType.SQUARE or \
           in_figure1._type == FigureType.CIRCLE or in_figure2._type == FigureType.CIRCLE:
            in_figure1._orientation = in_figure2._orientation
            out_figure._orientation = in_figure3._orientation
            return

        diff = in_figure1._orientation.value - in_figure2._orientation.value
        if diff == 0:
            out_figure._orientation = in_figure3._orientation
            return
        out_figure._orientation = FigureOrientation(abs((in_figure3._orientation.value - diff - 1) % 4) + 1)

    @staticmethod
    def create_answers(figure_tl1, figure_tl2, figure_tr1, figure_tr2, figure_bl1, figure_bl2):
        t1, t2 = DataGenerator.create_analog(figure_tl1, figure_tl2, figure_tr1, figure_tr2, figure_bl1, figure_bl2)
        a1, a2 = deepcopy(t1), deepcopy(t2)
        b1, b2 = deepcopy(t1), deepcopy(t2)
        c1, c2 = deepcopy(t1), deepcopy(t2)

        a1._type = FigureType((a1._type.value + 2) % 6 + 1)
        a2._size = FigureSize((a2._size.value + 1) % 5)

        b1._orientation = FigureOrientation((b1._orientation.value + 1) % 4 + 1)
        b2._position = FigurePosition((b2._position.value + 1) % 5)

        c1._position = FigurePosition((c1._position.value + 1) % 5)
        c2._type = FigureType((c2._type.value + 2) % 6 + 1)

        return [a1, a2, b1, b2, c1, c2]

if __name__ == "__main__":
    dg = DataGenerator('../../docs/generated-test-examples.csv')

    output_file = open(dg.output, 'w')
    for i in xrange(1):
        my_str = ''
        for figure in dg.generate_data():
            my_str += str(figure) + ","
        output_file.write(my_str[:-1] + "\n")

    output_file.close()


    generated = dg.generate_data()
    for figure in generated:
        print figure

    print "answers"
    for answer in DataGenerator.create_answers(generated[0], generated[1], generated[2], generated[3], generated[4], generated[5]):
        print answer
