from django import forms

class ConverterForm(forms.Form):
    MEASUREMENTS = (
        ('choice', 'Выберите категорию'),
    )
    input_unit = forms.ChoiceField(choices=MEASUREMENTS)
    input_value = forms.DecimalField(decimal_places=6, required=False)
    output_unit = forms.ChoiceField(choices=MEASUREMENTS)
    output_value = forms.DecimalField(decimal_places=6, required=False)

class InputAndResult(forms.Form):
    input_value = forms.DecimalField(decimal_places=6, required=False, help_text = 'Значение')
    output_value = forms.DecimalField(decimal_places=6, required=False, help_text = 'Результат')

class FormChoice(forms.Form):
    MEASUREMENTS = (
        ('time', 'Время'),
        ('volume', 'Объем'),
        ('pressure', 'Давление'),
        ('mass', 'Масса'),
        ('square', 'Площадь'),
        ('speed', 'Скорость'),
        ('frequency', 'Частота'),
        ('energy', 'Энергия'),
        ('length', 'Длина'),
    )
    choiceVal = forms.ChoiceField(choices=MEASUREMENTS)

class PressureForm(forms.Form):
    MEASUREMENTS = (
        ('atmosphere', 'Атмосфера'),
        ('bar', 'Бар'),
        ('torr', 'Торр'),
        ('pound-force', 'Фунт-сила на квадратный дюйм'),
        ('pascal', 'Паскаль')
    )
    input_unit = forms.ChoiceField(choices=MEASUREMENTS)
    output_unit = forms.ChoiceField(choices=MEASUREMENTS)

class FrequencyForm(forms.Form):
    MEASUREMENTS = (
        ('hertz', 'Герц'),
        ('kilohertz', 'Килогерц'),
        ('megahertz', 'Мегагерц'),
        ('gigahertz', 'Гигагерц')
    )
    input_unit = forms.ChoiceField(choices=MEASUREMENTS)
    output_unit = forms.ChoiceField(choices=MEASUREMENTS)
    
class LengthForm(forms.Form):
    MEASUREMENTS = (
        ('kilometer', 'Километр'),
        ('metr', 'Метр'),
        ('centimeter', 'Сантиметр'),
        ('millimeter', 'Миллиметр'),
        ('micrometer', 'Микрометр'),
        ('nanometer', 'Нанометр'),
        ('mile', 'Миля'),
        ('yard', 'Ярд'),
        ('foot', 'Фут'),
        ('inch', 'Дюйм')
    )
    input_unit = forms.ChoiceField(choices=MEASUREMENTS)
    output_unit = forms.ChoiceField(choices=MEASUREMENTS)

class EnergyForm(forms.Form):
    MEASUREMENTS = (
        ('joule', 'Джоуль'),
        ('kilojoule', 'Килоджоуль'),
        ('gram-calorie', 'Грамм-калория'),
        ('kilocalorie', 'Килокалория'),
        ('watt-hour', 'Ватт-час'),
        ('kilowatt-hour', 'Киловатт-час')
    )
    input_unit = forms.ChoiceField(choices=MEASUREMENTS)
    output_unit = forms.ChoiceField(choices=MEASUREMENTS)

class TimeForm(forms.Form):
    MEASUREMENTS = (
        ('millisecond', 'Миллисекунда'),
        ('second', 'Секунда'),
        ('minute', 'Минута'),
        ('hour', 'Час'),
        ('day', 'День'),
        ('week', 'Неделя'),
        ('month', 'Месяц'),
        ('year', 'Год')
    )
    input_unit = forms.ChoiceField(choices=MEASUREMENTS)
    output_unit = forms.ChoiceField(choices=MEASUREMENTS)

class VolumeForm(forms.Form):
    MEASUREMENTS = (
        ('cubic_metr', 'Кубический метр'),
        ('liter', 'Литр'),
        ('milliliter', 'Миллилитр'),
        ('cubic_foot', 'Кубический фут'),
        ('cubic_inch', 'Кубический дюйм'),
    )
    input_unit = forms.ChoiceField(choices=MEASUREMENTS)
    output_unit = forms.ChoiceField(choices=MEASUREMENTS)

class MassForm(forms.Form):
    MEASUREMENTS = (
        ('ton', 'Тонн'),
        ('kilogram', 'Килограмм'),
        ('gram', 'Грамм'),
        ('milligram', 'Миллиграмм'),
        ('microgram', 'Микрограмм'),
        ('pound', 'Фунт')
    )
    input_unit = forms.ChoiceField(choices=MEASUREMENTS)
    output_unit = forms.ChoiceField(choices=MEASUREMENTS)

class SquareForm(forms.Form):
    MEASUREMENTS = (
        ('square_kilometer', 'Квадратный километр'),
        ('square_metr', 'Квадратный метр'),
        ('square_mile', 'Квадратная миля'),
        ('square_yard', 'Квадратный ярд'),
        ('square_inch', 'Квадратный дюйм'),
        ('hectare', 'Гектар'),
        ('acre', 'Акр'),
    )
    input_unit = forms.ChoiceField(choices=MEASUREMENTS)
    output_unit = forms.ChoiceField(choices=MEASUREMENTS)

class SpeedForm(forms.Form):
    MEASUREMENTS = (
        ('mile_per_hour', 'Миля в час'),
        ('foot_per_second', 'Фут в секунду'),
        ('metr_per_second', 'Метр в секунду'),
        ('kilometr_per_hour', 'Километр в час')
    )
    input_unit = forms.ChoiceField(choices=MEASUREMENTS)
    output_unit = forms.ChoiceField(choices=MEASUREMENTS)