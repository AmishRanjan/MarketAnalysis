from scripts.helper.Widgets import Widgets
from scripts.constants import *
from scripts.data_processing.DataProcessor import DataProcessor
from scripts.indicator_calculation.IndicatorCalculator import IndicatorCalculator

dp = DataProcessor()
wg = Widgets()
ic = IndicatorCalculator()

#file_list = DataProcessor.getFileName(dp)

# file_name = Widgets.askToSelectOption(wg,
# 		    file_selection_prompt,
# 		    file_list)
#header_format = Widgets.userEntry(wg, file_format_prompt, header, "OK")

#DataProcessor.imputeData(dp, file_name, header_format, header)

IndicatorCalculator.calculate_indicators(ic, "RELIANCE-I.csv")


