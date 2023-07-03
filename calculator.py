from PyQt6.QtCore import Qt, QSize
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QFont, QIcon

import sys
import re
from math import *
import ctypes


# additional functions

# factorial function


def fact(x):
    res = 1
    for i in range(1, x + 1):
        res *= i
    return res

# cotangens function


def cot(x):
    return 1 / tan(x)

# secans function


def sec(x):
    return 1 / cos(x)

# cosecans function


def csc(x):
    return 1 / sin(x)

# rounding to 5 digits after point (for degree trigonometry funtions) functions


def round5(x):
    return round(x, 5)

# square root function


def sqrt(x):
    return pow(x, 0.5)


class Window(QMainWindow):
    def __init__(self) -> None:
        super(Window, self).__init__()

        # sizing and position

        self.width = 500
        self.height = 525
        self.x = int((1920 - self.width) / 2)
        self.y = int((1080 - self.height) / 2)

        self.mode = {
            'default': 1,
            'engineeric': 0
        }

        # variables

        self.curr_number = '0'
        self.buffer = ''
        self.curr_action = None
        self.sign = ''

        # application icon

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QtGui.QIcon('./img/calculator.svg'))
        appicon = 'mycompany.myproduct.subproduct.version'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appicon)

        # textbar

        self.textbar = QtWidgets.QLabel(self, text=self.curr_number)
        self.textbar.autoFillBackground()
        self.textbar.setStyleSheet("background-color: #fff")
        self.font = self.textbar.font()
        self.font.setPointSize(48)
        self.textbar.setFont(self.font)
        self.textbar.setAlignment(Qt.AlignmentFlag.AlignRight |
                                  Qt.AlignmentFlag.AlignVCenter)

        # buttons

        # number buttons

        self.one_button = QtWidgets.QPushButton(self, text='1')
        self.two_button = QtWidgets.QPushButton(self, text='2')
        self.three_button = QtWidgets.QPushButton(self, text='3')
        self.four_button = QtWidgets.QPushButton(self, text='4')
        self.five_button = QtWidgets.QPushButton(self, text='5')
        self.six_button = QtWidgets.QPushButton(self, text='6')
        self.seven_button = QtWidgets.QPushButton(self, text='7')
        self.eight_button = QtWidgets.QPushButton(self, text='8')
        self.nine_button = QtWidgets.QPushButton(self, text='9')
        self.zero_button = QtWidgets.QPushButton(self, text='0')
        self.point_button = QtWidgets.QPushButton(self, text='.')
        self.sign_button = QtWidgets.QPushButton(self, text='+/-')

        self.one_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.two_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.three_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.four_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.five_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.six_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.seven_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.eight_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.nine_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.zero_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.point_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.sign_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)

        # action buttons

        # default mode

        self.plus_button = QtWidgets.QPushButton(self, text='+')
        self.minus_button = QtWidgets.QPushButton(self, text='-')
        self.multiply_button = QtWidgets.QPushButton(self, text='×')
        self.division_button = QtWidgets.QPushButton(self, text='÷')
        self.equalty_button = QtWidgets.QPushButton(self, text='=')
        self.sqrt_button = QtWidgets.QPushButton(self, text='√x')
        self.sqr_button = QtWidgets.QPushButton(self, text='x^2')
        self.one_by_number_button = QtWidgets.QPushButton(self, text='1/x')
        self.percent_button = QtWidgets.QPushButton(self, text='%')
        self.ce_button = QtWidgets.QPushButton(self, text='CE')
        self.c_button = QtWidgets.QPushButton(self, text='C')
        self.backspace_button = QtWidgets.QPushButton(self, text='<=')
        self.swap_mode_button = QtWidgets.QPushButton(self)
        self.swap_mode_button.setIcon(QIcon('img/swap.svg'))
        self.swap_mode_button.setIconSize(QSize(30, 30))

        self.plus_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.minus_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.multiply_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.division_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.equalty_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.sqrt_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.sqr_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.one_by_number_button.setFocusPolicy(
            Qt.FocusPolicy.TabFocus.NoFocus)
        self.percent_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.ce_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.c_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.backspace_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.swap_mode_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)

        # engineeric mode

        self.left_bracket_button = QtWidgets.QPushButton(self, text='(')
        self.right_bracket_button = QtWidgets.QPushButton(self, text=')')
        self.pi_button = QtWidgets.QPushButton(self, text='π')
        self.sin_button = QtWidgets.QPushButton(self, text='sin')
        self.cos_button = QtWidgets.QPushButton(self, text='cos')
        self.pow_button = QtWidgets.QPushButton(self, text='x^y')
        self.rad_deg_swap_button = QtWidgets.QPushButton(self, text='rad')
        self.fact_button = QtWidgets.QPushButton(self, text='x!')
        self.ln_button = QtWidgets.QPushButton(self, text='ln')
        self.lg_button = QtWidgets.QPushButton(self, text='lg')
        self.pow10_button = QtWidgets.QPushButton(self, text='10^x')
        self.e_button = QtWidgets.QPushButton(self, text='e')
        self.abs_button = QtWidgets.QPushButton(self, text='|x|')
        self.sec_button = QtWidgets.QPushButton(self, text='sec')
        self.csc_button = QtWidgets.QPushButton(self, text='csc')
        self.tan_button = QtWidgets.QPushButton(self, text='tan')
        self.cot_button = QtWidgets.QPushButton(self, text='cot')

        self.set_default_mode()

        # logic

        # number buttons

        self.one_button.clicked.connect(self.add_number_1)
        self.two_button.clicked.connect(self.add_number_2)
        self.three_button.clicked.connect(self.add_number_3)
        self.four_button.clicked.connect(self.add_number_4)
        self.five_button.clicked.connect(self.add_number_5)
        self.six_button.clicked.connect(self.add_number_6)
        self.seven_button.clicked.connect(self.add_number_7)
        self.eight_button.clicked.connect(self.add_number_8)
        self.nine_button.clicked.connect(self.add_number_9)
        self.zero_button.clicked.connect(self.add_number_0)
        self.sign_button.clicked.connect(self.change_sign)
        self.point_button.clicked.connect(self.add_point)

        # action butttons

        self.plus_button.clicked.connect(self.plus)
        self.minus_button.clicked.connect(self.minus)
        self.division_button.clicked.connect(self.division)
        self.multiply_button.clicked.connect(self.multiply)
        self.equalty_button.clicked.connect(self.equals)
        self.sqr_button.clicked.connect(self.sqr)
        self.sqrt_button.clicked.connect(self.sqrt)
        self.one_by_number_button.clicked.connect(self.one_by_number)
        self.percent_button.clicked.connect(self.percent)
        self.ce_button.clicked.connect(self.ce)
        self.c_button.clicked.connect(self.c)
        self.backspace_button.clicked.connect(self.backspace)
        self.swap_mode_button.clicked.connect(self.swap_mode)

        # logic

        self.fact_button.clicked.connect(self.fact_input)
        self.left_bracket_button.clicked.connect(self.left_bracket)
        self.right_bracket_button.clicked.connect(self.right_bracket)
        self.abs_button.clicked.connect(self.abs_input)
        self.sin_button.clicked.connect(self.sin_input)
        self.cos_button.clicked.connect(self.cos_input)
        self.tan_button.clicked.connect(self.tan_input)
        self.cot_button.clicked.connect(self.cot_input)
        self.sec_button.clicked.connect(self.sec_input)
        self.csc_button.clicked.connect(self.csc_input)
        self.pi_button.clicked.connect(self.pi_input)
        self.e_button.clicked.connect(self.e_input)
        self.lg_button.clicked.connect(self.lg_input)
        self.ln_button.clicked.connect(self.ln_input)
        self.pow10_button.clicked.connect(self.pow10_input)
        self.pow_button.clicked.connect(self.pow_input)
        self.rad_deg_swap_button.clicked.connect(self.rad_deg_swap)

        self.fact_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.left_bracket_button.setFocusPolicy(
            Qt.FocusPolicy.TabFocus.NoFocus)
        self.right_bracket_button.setFocusPolicy(
            Qt.FocusPolicy.TabFocus.NoFocus)
        self.abs_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.sin_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.cos_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.tan_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.cot_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.sec_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.csc_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.pi_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.e_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.lg_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.ln_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.pow10_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.pow_button.setFocusPolicy(Qt.FocusPolicy.TabFocus.NoFocus)
        self.rad_deg_swap_button.setFocusPolicy(
            Qt.FocusPolicy.TabFocus.NoFocus)

    # modes

    def swap_mode(self):
        if self.mode['default']:
            self.set_engineeric_mode()
            self.textbar.setText(self.user_input)
        elif self.mode['engineeric']:
            self.set_default_mode()
            self.textbar.setText(self.sign + self.curr_number)

    def set_default_mode(self):

        # swap to default mode

        self.mode['default'] = 1
        self.mode['engineeric'] = 0
        self.width = 500
        self.height = 525
        self.x = int((1920 - self.width) / 2)
        self.y = int((1080 - self.height) / 2)

        # variables

        self.curr_number = '0'
        self.buffer = ''
        self.curr_action = None
        self.sign = ''

        # fonts

        QtWidgets.QPushButton.setFont(self, QFont('Times', 32))

        # main window

        self.setGeometry(self.x, self.y, self.width, self.height)

        # calculator textbar

        self.textbar.setGeometry(0, 0, self.width, 75)

        # buttons

        self.sign_button.setEnabled(True)
        self.one_by_number_button.setEnabled(True)

        # number buttons

        self.one_button.setGeometry(0, 375, 125, 75)
        self.two_button.setGeometry(125, 375, 125, 75)
        self.three_button.setGeometry(250, 375, 125, 75)
        self.four_button.setGeometry(0, 300, 125, 75)
        self.five_button.setGeometry(125, 300, 125, 75)
        self.six_button.setGeometry(250, 300, 125, 75)
        self.seven_button.setGeometry(0, 225, 125, 75)
        self.eight_button.setGeometry(125, 225, 125, 75)
        self.nine_button.setGeometry(250, 225, 125, 75)
        self.zero_button.setGeometry(125, 450, 125, 75)
        self.point_button.setGeometry(250, 450, 125, 75)
        self.sign_button.setGeometry(0, 450, 125, 75)

        # action buttons

        self.plus_button.setGeometry(375, 375, 125, 75)
        self.minus_button.setGeometry(375, 300, 125, 75)
        self.multiply_button.setGeometry(375, 225, 125, 75)
        self.division_button.setGeometry(375, 150, 125, 75)
        self.equalty_button.setGeometry(375, 450, 125, 75)
        self.sqrt_button.setGeometry(250, 150, 125, 75)
        self.sqr_button.setGeometry(125, 150, 125, 75)
        self.one_by_number_button.setGeometry(0, 150, 125, 75)
        self.percent_button.setGeometry(0, 75, 125, 75)
        self.ce_button.setGeometry(125, 75, 125, 75)
        self.c_button.setGeometry(250, 75, 125, 75)
        self.backspace_button.setGeometry(375, 75, 125, 75)
        self.swap_mode_button.setGeometry(0, 0, 75, 75)

        # engineeric buttons hide

        self.left_bracket_button.hide()
        self.right_bracket_button.hide()
        self.pi_button.hide()
        self.sin_button.hide()
        self.cos_button.hide()
        self.pow_button .hide()
        self.rad_deg_swap_button.hide()
        self.fact_button.hide()
        self.ln_button.hide()
        self.lg_button.hide()
        self.pow10_button.hide()
        self.e_button.hide()
        self.abs_button.hide()
        self.sec_button.hide()
        self.csc_button.hide()
        self.tan_button.hide()
        self.cot_button.hide()

    def set_engineeric_mode(self):

        # swap to engineeric mode

        self.mode['default'] = 0
        self.mode['engineeric'] = 1
        self.width = 875
        self.height = 525
        self.x = int((1920 - self.width) / 2)
        self.y = int((1080 - self.height) / 2)

        # variables

        self.user_input = ''
        self.formatted_input = ''
        self.deg_rad = {
            'rad': 1,
            'deg': 0
        }

        # fonts

        QtWidgets.QPushButton.setFont(self, QFont('Times', 32))

        # main window

        self.setGeometry(self.x, self.y, self.width, self.height)

        # calculator textbar

        self.textbar.setGeometry(0, 0, self.width, 75)
        self.textbar.setText(self.user_input)

        # buttons

        # number buttons

        self.one_button.setGeometry(375, 375, 125, 75)
        self.two_button.setGeometry(500, 375, 125, 75)
        self.three_button.setGeometry(625, 375, 125, 75)
        self.four_button.setGeometry(375, 300, 125, 75)
        self.five_button.setGeometry(500, 300, 125, 75)
        self.six_button.setGeometry(625, 300, 125, 75)
        self.seven_button.setGeometry(375, 225, 125, 75)
        self.eight_button.setGeometry(500, 225, 125, 75)
        self.nine_button.setGeometry(625, 225, 125, 75)
        self.zero_button.setGeometry(500, 450, 125, 75)
        self.point_button.setGeometry(625, 450, 125, 75)
        self.sign_button.setGeometry(375, 450, 125, 75)

        # action buttons

        self.plus_button.setGeometry(750, 375, 125, 75)
        self.minus_button.setGeometry(750, 300, 125, 75)
        self.multiply_button.setGeometry(750, 225, 125, 75)
        self.division_button.setGeometry(750, 150, 125, 75)
        self.equalty_button.setGeometry(750, 450, 125, 75)
        self.sqrt_button.setGeometry(625, 150, 125, 75)
        self.sqr_button.setGeometry(500, 150, 125, 75)
        self.one_by_number_button.setGeometry(375, 150, 125, 75)
        self.percent_button.setGeometry(375, 75, 125, 75)
        self.ce_button.setGeometry(500, 75, 125, 75)
        self.c_button.setGeometry(625, 75, 125, 75)
        self.backspace_button.setGeometry(750, 75, 125, 75)
        self.swap_mode_button.setGeometry(0, 75, 125, 75)

        # engineeric buttons show

        self.left_bracket_button.show()
        self.right_bracket_button.show()
        self.pi_button.show()
        self.sin_button.show()
        self.cos_button.show()
        self.pow_button .show()
        self.rad_deg_swap_button.show()
        self.fact_button.show()
        self.ln_button.show()
        self.lg_button.show()
        self.pow10_button.show()
        self.e_button.show()
        self.abs_button.show()
        self.sec_button.show()
        self.csc_button.show()
        self.tan_button.show()
        self.cot_button.show()

        # +/- button and 1/n button disable

        self.sign_button.setEnabled(False)
        self.one_by_number_button.setEnabled(False)

        # engineeric action buttons

        self.left_bracket_button.setGeometry(125, 75, 125, 75)
        self.right_bracket_button.setGeometry(250, 75, 125, 75)
        self.pi_button.setGeometry(125, 450, 125, 75)
        self.sin_button.setGeometry(0, 225, 125, 75)
        self.cos_button.setGeometry(0, 300, 125, 75)
        self.sec_button.setGeometry(125, 225, 125, 75)
        self.csc_button.setGeometry(125, 300, 125, 75)
        self.tan_button.setGeometry(0, 375, 125, 75)
        self.cot_button.setGeometry(125, 375, 125, 75)
        self.pow_button .setGeometry(250, 225, 125, 75)
        self.rad_deg_swap_button.setGeometry(0, 450, 125, 75)
        self.fact_button.setGeometry(125, 150, 125, 75)
        self.ln_button.setGeometry(250, 450, 125, 75)
        self.lg_button.setGeometry(250, 375, 125, 75)
        self.pow10_button.setGeometry(250, 300, 125, 75)
        self.e_button.setGeometry(0, 150, 125, 75)
        self.abs_button.setGeometry(250, 150, 125, 75)

    # keybinds

    '''
    default and engineeric mode:

    0-9 - numbers
    + - plus
    - - minus
    / - division
    * - multiply
    . - point
    = / Enter - equals
    % - percent (n/100)* * - in enginneric mode only for result
    Escape - clear current input
    Shift + Escape - close application
    Tab - swap mode

    default mode:

    ^ - square

    engineeric mode:

    ! - factorial
    | - module
    () - brackets
    ^ - power input
    E - exponent number
    P - pi number
    '''

    def keyPressEvent(self, event):

        match event.key():
            case Qt.Key.Key_0:
                self.add_number_0()
            case Qt.Key.Key_1:
                self.add_number_1()
            case Qt.Key.Key_2:
                self.add_number_2()
            case Qt.Key.Key_3:
                self.add_number_3()
            case Qt.Key.Key_4:
                self.add_number_4()
            case Qt.Key.Key_5:
                self.add_number_5()
            case Qt.Key.Key_6:
                self.add_number_6()
            case Qt.Key.Key_7:
                self.add_number_7()
            case Qt.Key.Key_8:
                self.add_number_8()
            case Qt.Key.Key_9:
                self.add_number_9()
            case Qt.Key.Key_Period:
                self.add_point()
            case Qt.Key.Key_Equal | Qt.Key.Key_Return:
                self.equals()
            case Qt.Key.Key_Plus:
                self.plus()
            case Qt.Key.Key_Minus:
                self.minus()
            case Qt.Key.Key_Slash:
                self.division()
            case Qt.Key.Key_Asterisk:
                self.multiply()
            case Qt.Key.Key_Backspace:
                self.backspace()
            case Qt.Key.Key_Percent:
                self.percent()
            case Qt.Key.Key_Escape:
                if event.modifiers() == Qt.KeyboardModifier.NoModifier:
                    self.c()
                elif event.modifiers() == Qt.KeyboardModifier.ShiftModifier:
                    sys.exit()
            case Qt.Key.Key_Tab:
                self.swap_mode()

        if self.mode['default']:
            if event.key() == Qt.Key.Key_AsciiCircum:
                self.sqr()
        elif self.mode['engineeric']:
            match event.key():
                case Qt.Key.Key_Exclam:
                    self.fact_input()
                case Qt.Key.Key_Bar:
                    self.abs_input()
                case Qt.Key.Key_ParenLeft:
                    self.left_bracket()
                case Qt.Key.Key_ParenRight:
                    self.right_bracket()
                case Qt.Key.Key_AsciiCircum:
                    self.pow_input()
                case Qt.Key.Key_E:
                    self.e_input()
                case Qt.Key.Key_P:
                    self.pi_input()

    # numbers, point, sign input

    def add_number_1(self):
        if self.mode['default']:
            if len(self.curr_number) < 10:
                if self.curr_number == '0':
                    self.curr_number = '1'
                else:
                    self.curr_number += '1'
            self.textbar.setText(self.sign + self.curr_number)
        elif self.mode['engineeric']:
            if self.user_input[-1:] == ')' or self.user_input[-1:] == '|' or self.user_input[-1:] == '!' or self.user_input[-1:] == 'e' or self.user_input[-1:] == 'π':
                self.user_input += '*'
                self.formatted_input += '*'
            if self.user_input == '':
                self.user_input = '1'
                self.formatted_input = '1'
            else:
                self.user_input += '1'
                self.formatted_input += '1'
            self.textbar.setText(self.user_input)

    def add_number_2(self):
        if self.mode['default']:
            if len(self.curr_number) < 10:
                if self.curr_number == '0':
                    self.curr_number = '2'
                else:
                    self.curr_number += '2'
            self.textbar.setText(self.sign + self.curr_number)
        elif self.mode['engineeric']:
            if self.user_input[-1:] == ')' or self.user_input[-1:] == '|' or self.user_input[-1:] == '!' or self.user_input[-1:] == 'e' or self.user_input[-1:] == 'π':
                self.user_input += '*'
                self.formatted_input += '*'
            if self.user_input == '':
                self.user_input = '2'
                self.formatted_input = '2'
            else:
                self.user_input += '2'
                self.formatted_input += '2'
            self.textbar.setText(self.user_input)

    def add_number_3(self):
        if self.mode['default']:
            if len(self.curr_number) < 10:
                if self.curr_number == '0':
                    self.curr_number = '3'
                else:
                    self.curr_number += '3'
            self.textbar.setText(self.sign + self.curr_number)
        elif self.mode['engineeric']:
            if self.user_input[-1:] == ')' or self.user_input[-1:] == '|' or self.user_input[-1:] == '!' or self.user_input[-1:] == 'e' or self.user_input[-1:] == 'π':
                self.user_input += '*'
                self.formatted_input += '*'
            if self.user_input == '':
                self.user_input = '3'
                self.formatted_input = '3'
            else:
                self.user_input += '3'
                self.formatted_input += '3'
            self.textbar.setText(self.user_input)

    def add_number_4(self):
        if self.mode['default']:
            if len(self.curr_number) < 10:
                if self.curr_number == '0':
                    self.curr_number = '4'
                else:
                    self.curr_number += '4'
            self.textbar.setText(self.sign + self.curr_number)
        elif self.mode['engineeric']:
            if self.user_input[-1:] == ')' or self.user_input[-1:] == '|' or self.user_input[-1:] == '!' or self.user_input[-1:] == 'e' or self.user_input[-1:] == 'π':
                self.user_input += '*'
                self.formatted_input += '*'
            if self.user_input == '':
                self.user_input = '4'
                self.formatted_input = '4'
            else:
                self.user_input += '4'
                self.formatted_input += '4'
            self.textbar.setText(self.user_input)

    def add_number_5(self):
        if self.mode['default']:
            if len(self.curr_number) < 10:
                if self.curr_number == '0':
                    self.curr_number = '5'
                else:
                    self.curr_number += '5'
            self.textbar.setText(self.sign + self.curr_number)
        elif self.mode['engineeric']:
            if self.user_input[-1:] == ')' or self.user_input[-1:] == '|' or self.user_input[-1:] == '!' or self.user_input[-1:] == 'e' or self.user_input[-1:] == 'π':
                self.user_input += '*'
                self.formatted_input += '*'
            if self.user_input == '':
                self.user_input = '5'
                self.formatted_input = '5'
            else:
                self.user_input += '5'
                self.formatted_input += '5'
            self.textbar.setText(self.user_input)

    def add_number_6(self):
        if self.mode['default']:
            if len(self.curr_number) < 10:
                if self.curr_number == '0':
                    self.curr_number = '6'
                else:
                    self.curr_number += '6'
            self.textbar.setText(self.sign + self.curr_number)
        elif self.mode['engineeric']:
            if self.user_input[-1:] == ')' or self.user_input[-1:] == '|' or self.user_input[-1:] == '!' or self.user_input[-1:] == 'e' or self.user_input[-1:] == 'π':
                self.user_input += '*'
                self.formatted_input += '*'
            if self.user_input == '':
                self.user_input = '6'
                self.formatted_input = '6'
            else:
                self.user_input += '6'
                self.formatted_input += '6'
            self.textbar.setText(self.user_input)

    def add_number_7(self):
        if self.mode['default']:
            if len(self.curr_number) < 10:
                if self.curr_number == '0':
                    self.curr_number = '7'
                else:
                    self.curr_number += '7'
            self.textbar.setText(self.sign + self.curr_number)
        elif self.mode['engineeric']:
            if self.user_input[-1:] == ')' or self.user_input[-1:] == '|' or self.user_input[-1:] == '!' or self.user_input[-1:] == 'e' or self.user_input[-1:] == 'π':
                self.user_input += '*'
                self.formatted_input += '*'
            if self.user_input == '':
                self.user_input = '7'
                self.formatted_input = '7'
            else:
                self.user_input += '7'
                self.formatted_input += '7'
            self.textbar.setText(self.user_input)

    def add_number_8(self):
        if self.mode['default']:
            if len(self.curr_number) < 10:
                if self.curr_number == '0':
                    self.curr_number = '8'
                else:
                    self.curr_number += '8'
            self.textbar.setText(self.sign + self.curr_number)
        elif self.mode['engineeric']:
            if self.user_input[-1:] == ')' or self.user_input[-1:] == '|' or self.user_input[-1:] == '!' or self.user_input[-1:] == 'e' or self.user_input[-1:] == 'π':
                self.user_input += '*'
                self.formatted_input += '*'
            if self.user_input == '':
                self.user_input = '8'
                self.formatted_input = '8'
            else:
                self.user_input += '8'
                self.formatted_input += '8'
            self.textbar.setText(self.user_input)

    def add_number_9(self):
        if self.mode['default']:
            if len(self.curr_number) < 10:
                if self.curr_number == '0':
                    self.curr_number = '9'
                else:
                    self.curr_number += '9'
            self.textbar.setText(self.sign + self.curr_number)
        elif self.mode['engineeric']:
            if self.user_input[-1:] == ')' or self.user_input[-1:] == '|' or self.user_input[-1:] == '!' or self.user_input[-1:] == 'e' or self.user_input[-1:] == 'π':
                self.user_input += '*'
                self.formatted_input += '*'
            if self.user_input == '':
                self.user_input = '9'
                self.formatted_input = '9'
            else:
                self.user_input += '9'
                self.formatted_input += '9'
            self.textbar.setText(self.user_input)

    def add_number_0(self):
        if self.mode['default']:
            if len(self.curr_number) < 10:
                if self.curr_number == '0':
                    self.curr_number = '0'
                else:
                    self.curr_number += '0'
            self.textbar.setText(self.sign + self.curr_number)
        elif self.mode['engineeric']:
            if self.user_input[-1:] == ')' or self.user_input[-1:] == '|' or self.user_input[-1:] == '!' or self.user_input[-1:] == 'e' or self.user_input[-1:] == 'π':
                self.user_input += '*'
                self.formatted_input += '*'
            if self.user_input == '':
                self.user_input = '0'
                self.formatted_input = '0'
            else:
                self.user_input += '0'
                self.formatted_input += '0'
            self.textbar.setText(self.user_input)

    def change_sign(self):
        if self.mode['default']:
            if not self.curr_number == '0':
                if self.sign == '':
                    self.sign = '-'
                else:
                    self.sign = ''
            self.textbar.setText(self.sign + self.curr_number)

    def add_point(self):
        if self.mode['default']:
            if len(self.curr_number) < 9:
                if '.' not in self.curr_number:
                    self.curr_number += '.'
                self.textbar.setText(self.sign + self.curr_number)
        else:
            if self.user_input[-1:].isdigit():
                self.buffer = re.split(
                    r'[(|)|||+|-|*|/]', self.formatted_input)[-1]
                if '.' not in self.buffer:
                    self.user_input += '.'
                    self.formatted_input += '.'
                    self.textbar.setText(self.user_input)

    # action buttons

    def plus(self):
        if self.mode['default']:
            self.buffer = self.sign + self.curr_number
            self.sign = ''
            self.curr_number = '0'
            self.curr_action = '+'
            self.textbar.setText(self.sign + self.curr_number)
        elif self.mode['engineeric']:
            if self.user_input[-1:] != '+' and self.user_input != '' and (self.user_input[-1].isdigit() or self.user_input[-1] == '!' or self.user_input[-1] == 'π' or self.user_input[-1] == 'e' or self.user_input[-1] == ')' or self.user_input[-1] == '|'):
                self.user_input += '+'
                self.formatted_input += '+'
            self.textbar.setText(self.user_input)

    def minus(self):
        if self.mode['default']:
            self.buffer = self.sign + self.curr_number
            self.sign = ''
            self.curr_number = '0'
            self.curr_action = '-'
            self.textbar.setText(self.sign + self.curr_number)
        elif self.mode['engineeric']:
            if self.user_input[-1:] != '-':
                self.user_input += '-'
                self.formatted_input += '-'
            self.textbar.setText(self.user_input)

    def multiply(self):
        if self.mode['default']:
            self.buffer = self.sign + self.curr_number
            self.sign = ''
            self.curr_number = '0'
            self.curr_action = '*'
            self.textbar.setText(self.sign + self.curr_number)
        elif self.mode['engineeric']:
            if self.user_input[-1:] != '*' and self.user_input != '' and (self.user_input[-1].isdigit() or self.user_input[-1] == '!' or self.user_input[-1] == 'π' or self.user_input[-1] == 'e' or self.user_input[-1] == ')' or self.user_input[-1] == '|'):
                self.user_input += '*'
                self.formatted_input += '*'
            self.textbar.setText(self.user_input)

    def division(self):
        if self.mode['default']:
            self.buffer = self.sign + self.curr_number
            self.sign = ''
            self.curr_number = '0'
            self.curr_action = '/'
            self.textbar.setText(self.sign + self.curr_number)
        elif self.mode['engineeric']:
            if self.user_input[-1:] != '*' and self.user_input != '' and (self.user_input[-1].isdigit() or self.user_input[-1] == '!' or self.user_input[-1] == 'π' or self.user_input[-1] == 'e' or self.user_input[-1] == ')' or self.user_input[-1] == '|'):
                self.user_input += '/'
                self.formatted_input += '/'
            self.textbar.setText(self.user_input)

    def equals(self):
        if self.mode['default']:
            try:
                if self.curr_action != None:
                    self.curr_number = str(eval(
                        self.buffer + self.curr_action + self.curr_number))
            except ZeroDivisionError:
                self.curr_number = '0'

            if self.curr_number[0] == '-':
                self.sign, self.curr_number = self.curr_number[0], self.curr_number[1:]
            else:
                self.sign = ''

            if len(self.curr_number) >= 11:
                self.curr_number = '%.4e' % float(self.curr_number)

            if '.' in self.curr_number and self.curr_number[-1] == '0':
                self.curr_number = self.curr_number.split('.')[0]

            self.buffer = ''
            self.curr_action = None
            self.textbar.setText(self.sign + self.curr_number)
        else:
            while self.formatted_input.count('(') > self.formatted_input.count(')'):
                self.user_input += ')'
                self.formatted_input += ')'
            try:
                self.user_input = str(eval(self.formatted_input))
            except:
                self.user_input = ''
            self.formatted_input = self.user_input
            if len(self.user_input) > 15:
                self.user_input = '%.4e' % float(self.user_input)
            self.textbar.setText(self.user_input)
            try:
                self.user_input = '%.5f' % float(self.user_input)
            except:
                self.user_input = ''

    def sqr(self):
        if self.mode['default']:
            self.curr_number = str(float(self.curr_number) ** 2)
            self.sign = ''
            if '.' in self.curr_number and self.curr_number[-1] == '0':
                self.curr_number = self.curr_number.split('.')[0]
            if len(self.curr_number) >= 11:
                self.curr_number = '%.4e' % float(self.curr_number)
            self.textbar.setText(self.sign + self.curr_number)
        else:
            self.user_input += '^2'
            self.formatted_input += '**2'
            self.textbar.setText(self.user_input)

    def sqrt(self):
        if self.mode['default']:
            self.curr_number = str(
                pow(float(self.sign + self.curr_number), 1/2))
            if '.' in self.curr_number and self.curr_number[-1] == '0':
                self.curr_number = self.curr_number.split('.')[0]
            if len(self.curr_number) >= 11:
                self.curr_number = '%.4e' % float(self.curr_number)
            self.textbar.setText(self.sign + self.curr_number)
        else:
            if self.user_input[-1].isdigit() or self.user_input[-1] == 'e' or self.user_input[-1] == 'π':
                self.user_input += '*'
                self.formatted_input += '*'
            self.user_input += '√'
            self.formatted_input += 'sqrt('
            self.textbar.setText(self.user_input)

    def one_by_number(self):
        if self.mode['default']:
            self.curr_number = str(1 / float(self.curr_number))
            if '.' in self.curr_number and self.curr_number[-1] == '0':
                self.curr_number = self.curr_number.split('.')[0]
            if len(self.curr_number) >= 11:
                self.curr_number = '%.4e' % float(self.curr_number)
            self.textbar.setText(self.sign + self.curr_number)

    def percent(self):
        if self.mode['default']:
            self.curr_number = str(float(self.curr_number) / 100)
            if '.' in self.curr_number and self.curr_number[-1] == '0':
                self.curr_number = self.curr_number.split('.')[0]
            if len(self.curr_number) >= 11:
                self.curr_number = '%.4e' % float(self.curr_number)
            self.textbar.setText(self.sign + self.curr_number)
        else:
            if self.formatted_input.replace('.', '').isdigit():
                self.formatted_input = self.user_input = str(round5(
                    float(self.formatted_input) / 100))
                self.textbar.setText(self.user_input)

    def c(self):
        if self.mode['default']:
            self.curr_number = '0'
            self.sign = ''
            self.textbar.setText(self.sign + self.curr_number)
        else:
            self.user_input = ''
            self.formatted_input = ''
            self.textbar.setText(self.user_input)

    def ce(self):
        if self.mode['default']:
            self.curr_number = '0'
            self.buffer = ''
            self.sign = ''
            self.action = None
            self.textbar.setText(self.sign + self.curr_number)
        else:
            self.user_input = ''
            self.formatted_input = ''
            self.textbar.setText(self.user_input)

    def backspace(self):
        if self.mode['default']:
            if 'e' in self.curr_number:
                self.curr_number = str('%.4f' % float(self.curr_number))[:9]
            if '-' in self.curr_number and len(self.curr_number) == 2:
                self.curr_number = '0'
            elif len(self.curr_number) == 1:
                self.curr_number = '0'
            elif self.curr_number[-2] == '.':
                self.curr_number = self.curr_number[:-2]
            else:
                self.curr_number = self.curr_number[:-1]
            self.textbar.setText(self.sign + self.curr_number)
        else:
            if self.user_input[-1:] == '!':
                self.formatted_input = ''.join(
                    self.formatted_input.rsplit('fact(', 1))
                self.formatted_input = self.formatted_input[:-1]
            elif self.user_input[-1:] == 'π' or self.user_input[-1:] == '^':
                self.formatted_input = self.formatted_input[:-2]
            elif self.user_input[-1:] == '√':
                self.formatted_input = self.formatted_input.rsplit('sqrt(', 1)[
                    0]
            elif self.user_input[-3:] == 'ln(':
                self.formatted_input = self.formatted_input.rsplit('log(', 1)[
                    0]
                self.user_input = self.user_input[:-2]
            elif self.user_input[-3:] == 'lg(':
                self.formatted_input = self.formatted_input.rsplit('log10(', 1)[
                    0]
                self.user_input = self.user_input[:-2]
            elif self.user_input[-4:] == 'sin(':
                self.formatted_input = self.formatted_input.rsplit('sin(', 1)[
                    0]
                self.user_input = self.user_input[:-3]
            elif self.user_input[-4:] == 'cos(':
                self.formatted_input = self.formatted_input.rsplit('logcos10(', 1)[
                    0]
                self.user_input = self.user_input[:-3]
            elif self.user_input[-4:] == 'tan(':
                self.formatted_input = self.formatted_input.rsplit('tan(', 1)[
                    0]
                self.user_input = self.user_input[:-3]
            elif self.user_input[-4:] == 'cot(':
                self.formatted_input = self.formatted_input.rsplit('cot(', 1)[
                    0]
                self.user_input = self.user_input[:-3]
            elif self.user_input[-4:] == 'sec(':
                self.formatted_input = self.formatted_input.rsplit('sec(', 1)[
                    0]
                self.user_input = self.user_input[:-3]
            elif self.user_input[-4:] == 'csc(':
                self.formatted_input = self.formatted_input.rsplit('csc(', 1)[
                    0]
                self.user_input = self.user_input[:-3]
            elif self.user_input[-1:] == '|':
                if self.user_input.count('|') % 2:
                    self.formatted_input = self.formatted_input.rsplit('abs(', 1)[
                        0]
                else:
                    self.formatted_input = self.formatted_input[:-1]
            elif self.formatted_input[-1:] == ')' and self.user_input[-1:] != ')' and self.user_input[-1:] != '|':
                self.formatted_input = self.formatted_input[-1]
                self.user_input += ')'
            else:
                self.formatted_input = self.formatted_input[:-1]
            self.user_input = self.user_input[:-1]
            self.textbar.setText(self.user_input)

    # engineeric action buttons

    def left_bracket(self):
        if self.mode['engineeric']:
            if self.user_input[-1:].isdigit():
                self.user_input += '*'
                self.formatted_input += '*'
            self.user_input += '('
            self.formatted_input += '('
            self.textbar.setText(self.user_input)

    def right_bracket(self):
        if self.mode['engineeric']:
            self.user_input += ')'
            self.formatted_input += ')'
            self.textbar.setText(self.user_input)

    def fact_input(self):
        if self.mode['engineeric']:
            self.buffer = re.split(r'[(|)|||+|-|/|*]',
                                   self.user_input.rsplit('!', 1)[0])[-1]
            if self.user_input != '' and self.user_input[-1:] != '!' and self.buffer.isdigit():
                self.user_input += '!'
                self.formatted_input = self.formatted_input[:self.formatted_input.rfind(
                    self.buffer)] + f'fact({self.buffer})'
                self.textbar.setText(self.user_input)

    def sin_input(self):
        if self.user_input[-1:].isdigit():
            self.user_input += '*'
            self.formatted_input += '*'
        self.user_input += 'sin('
        if self.deg_rad['deg']:
            self.formatted_input += 'round5(sin(radians('
        else:
            self.formatted_input += 'sin('
        self.textbar.setText(self.user_input)

    def cos_input(self):
        if self.user_input[-1:].isdigit():
            self.user_input += '*'
            self.formatted_input += '*'
        self.user_input += 'cos('
        if self.deg_rad['deg']:
            self.formatted_input += 'round5(cos(radians('
        else:
            self.formatted_input += 'cos('
        self.textbar.setText(self.user_input)

    def tan_input(self):
        if self.user_input[-1:].isdigit():
            self.user_input += '*'
            self.formatted_input += '*'
        self.user_input += 'tan('
        if self.deg_rad['deg']:
            self.formatted_input += 'round5(tan(radians('
        else:
            self.formatted_input += 'tan('
        self.textbar.setText(self.user_input)

    def cot_input(self):
        if self.user_input[-1:].isdigit():
            self.user_input += '*'
            self.formatted_input += '*'
        self.user_input += 'cot('
        if self.deg_rad['deg']:
            self.formatted_input += 'round5(cot(radians('
        else:
            self.formatted_input += 'cot('
        self.textbar.setText(self.user_input)

    def sec_input(self):
        if self.user_input[-1:].isdigit():
            self.user_input += '*'
            self.formatted_input += '*'
        self.user_input += 'sec('
        if self.deg_rad['deg']:
            self.formatted_input += 'round5(sec(radians('
        else:
            self.formatted_input += 'sec('
        self.textbar.setText(self.user_input)

    def csc_input(self):
        if self.user_input[-1:].isdigit():
            self.user_input += '*'
            self.formatted_input += '*'
        self.user_input += 'csc('
        if self.deg_rad['deg']:
            self.formatted_input += 'round5(csc(radians('
        else:
            self.formatted_input += 'csc('
        self.textbar.setText(self.user_input)

    def ln_input(self):
        if self.user_input[-1:].isdigit():
            self.user_input += '*'
            self.formatted_input += '*'
        self.user_input += 'ln('
        self.formatted_input += 'log('
        self.textbar.setText(self.user_input)

    def lg_input(self):
        if self.user_input[-1:].isdigit():
            self.user_input += '*'
            self.formatted_input += '*'
        self.user_input += 'lg('
        self.formatted_input += 'log10('
        self.textbar.setText(self.user_input)

    def abs_input(self):
        if self.mode['engineeric']:
            if self.formatted_input.count('abs(') == self.user_input.count('|') / 2:
                if self.user_input[-1:].isdigit():
                    self.user_input += '*'
                    self.formatted_input += '*'
                self.user_input += '|'
                self.formatted_input += 'abs('
            else:
                self.user_input += '|'
                self.formatted_input += ')'
            self.textbar.setText(self.user_input)

    def pi_input(self):
        if self.mode['engineeric']:
            if self.user_input[-1:] != 'π':
                if self.user_input[-1:].isdigit() or self.user_input[-1:] == ')' or self.user_input[-1:] == '|':
                    self.user_input += '*'
                    self.formatted_input += '*'
                self.user_input += 'π'
                self.formatted_input += 'pi'
            self.textbar.setText(self.user_input)

    def e_input(self):
        if self.mode['engineeric']:
            if self.user_input[-1:] != 'e':
                if self.user_input[-1:].isdigit() or self.user_input[-1:] == ')' or self.user_input[-1:] == '|':
                    self.user_input += '*'
                    self.formatted_input += '*'
                self.user_input += 'e'
                self.formatted_input += 'e'
            self.textbar.setText(self.user_input)

    def pow10_input(self):
        if self.user_input[-1:].isdigit():
            self.user_input += '*'
            self.formatted_input += '*'
        self.user_input += '10^'
        self.formatted_input += '10**'
        self.textbar.setText(self.user_input)

    def pow_input(self):
        if self.user_input[-1:] != '^':
            self.user_input += '^'
            self.formatted_input += '**'
        self.textbar.setText(self.user_input)

    def rad_deg_swap(self):
        if self.deg_rad['rad']:
            self.deg_rad['rad'] = 0
            self.deg_rad['deg'] = 1
            self.rad_deg_swap_button.setText('deg')
        elif self.deg_rad['deg']:
            self.deg_rad['deg'] = 0
            self.deg_rad['rad'] = 1
            self.rad_deg_swap_button.setText('rad')


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    application()
