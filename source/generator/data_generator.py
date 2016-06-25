# -*- coding: utf-8 -*-

from random import randint
from source.model.figures import Figure
from source.enums import *

class DataGenerator():
    def __init__(self, output):
        self.output = output
        self.top_left_quadrant = []
        self.top_right_quadrant = []
        self.bottom_left_quadrant = []
        self.bottom_right_quadrant = []
        
    def generate_data(self):
        figure_tlq1, figure_tlq2 = self.get_random_figures(randint(0,4), randint(0,4))

        figure_trq1, figure_trq2 = self.get_random_figures(randint(0,4), randint(0,4))
        figure_trq1._type = DataGenerator.get_random_mapped_types(figure_tlq1._type)
        figure_trq2._type = DataGenerator.get_random_mapped_types(figure_tlq2._type)
                
        #postavljanje figura iz donjeg lijevog kvadranta na site pozicije kao u gornjem lijevom         
        figure_blq1, figure_blq2 = self.get_random_figures(figure_tlq1._position, figure_tlq2._position)

        #analogna figura
        figure_brq1, figure_brq2 = self.create_analog(figure_tlq1, figure_tlq2, figure_trq1, figure_trq2, figure_blq1, figure_blq2)

        return [figure_tlq1, figure_tlq2, figure_trq1, figure_trq2, figure_blq1, figure_blq2, figure_brq1, figure_brq2]   
    
    def get_random_figures(self, pos1, pos2):
        figure_pos1 = FigurePosition(pos1)
        figure_orient1 = FigureOrientation(randint(1,4))
        
        figure_pos2 = FigurePosition(pos2)
        figure_type2 = FigureType(randint(1,6))
        figure_orient2 = FigureOrientation(randint(1,4))
        
        if(figure_pos1 == figure_pos2):
            figure_type1 = FigureType(randint(1,3))
            figure_type2 = FigureType(randint(4,6))
            figure_size1 = FigureSize(randint(2,3))
            figure_size2 = FigureSize(randint(1,2))

            if(figure_size1 == figure_size2):                
                figure_size2 = FigureSize(1)
                
        else:
            figure_type1 = FigureType(randint(1,6))
            figure_size1 = FigureSize(randint(1,3))
            figure_size2 = FigureSize(randint(1,3))
        
        figure1 = Figure(figure_type1, figure_pos1, figure_size1, figure_orient1)
        figure2 = Figure(figure_type2, figure_pos2, figure_size2, figure_orient2)

        return [figure1, figure2]

    @staticmethod
    def get_random_mapped_types(fig_type):
        if fig_type == FigureType.ARROW or fig_type == FigureType.LINE:
            return [FigureType.LINE, FigureType.ARROW][randint(0,1)]
        if fig_type == FigureType.CIRCLE or fig_type == FigureType.SQUARE:
            return [FigureType.CIRCLE, FigureType.SQUARE][randint(0,1)]
        else:
            return [FigureType.TRIANGLE, FigureType.PIE][randint(0,1)]

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

    def create_analog(self, figure_tl1, figure_tl2, figure_tr1, figure_tr2, figure_bl1, figure_bl2):
        analog_type1 = figure_bl1._type
        analog_position1 = figure_tr1._position
        analog_orientation1 = figure_tr1._orientation 
        
        analog_type2 = figure_bl2._type
        analog_position2 = figure_tr2._position
        analog_orientation2 = figure_tr2._orientation 
         
        f1 = Figure(analog_type1, analog_position1, 0, analog_orientation1)
        f2 = Figure(analog_type2, analog_position2, 0, analog_orientation2)

        self.size_translation(figure_tl1, figure_tr1, figure_bl1, f1)
        self.size_translation(figure_tl2, figure_tr2, figure_bl2, f2)
        self.orientation_analogy(figure_tl1, figure_tr1, figure_bl1, f1)
        self.orientation_analogy(figure_tl2, figure_tr2, figure_bl2, f2)
        DataGenerator.type_analogy(figure_tl1, figure_tr1, figure_bl1, f1)
        DataGenerator.type_analogy(figure_tl2, figure_tr2, figure_bl2, f2)

        return [f1, f2]

    @staticmethod
    def type_analogy(in_figure1, in_figure2, in_figure3, out_figure):
        if in_figure1._type == in_figure2._type:
            out_figure._type = in_figure3._type
        else:
            out_figure._type = DataGenerator.get_mapped_types(in_figure3._type)


    def size_translation(self, in_figure1, in_figure2, in_figure3, out_figure):
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
            out_figure._size = 1
        if out_figure._size > 3:
            out_figure._size = 3
        
        out_figure._size = FigureSize(out_figure._size)
        
    def orientation_analogy(self, in_figure1, in_figure2, in_figure3, out_figure):
        """
        Postavljanje analogne velicine za procijenjenu figuru

        Args:
            in_figure1: figura iz gornjeg lijevog kvadranta
            in_figure2: figura iz gornjeg desnog kvadranta
            in_figure3: figura iz lijevog donjeg kvadranta
            out_figure: izlazna figura
        """
        if in_figure1._type == FigureType.SQUARE or in_figure2 == FigureType.SQUARE or \
           in_figure1._type == FigureType.CIRCLE or in_figure2._type == FigureType.CIRCLE:
            out_figure._orientation = in_figure3._orientation
            return

        diff = in_figure1._orientation.value - in_figure2._orientation.value
        if diff == 0:
            out_figure._orientation = in_figure3._orientation
            return
        out_figure._orientation = FigureOrientation(abs((in_figure3._orientation.value - diff - 1) % 4) + 1)

if __name__ == "__main__":
    dg = DataGenerator('output.txt')
    
    box = dg.generate_data()
    for figure in box:
        print(figure)