import jpype
import asposecells
jpype.startJVM()
from asposecells.api import *
import tkinter as tk
from tkinter import filedialog



def conv2pdf():
    # open dialog to select file
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    # Load Excel file
    workbook = asposecells.api.Workbook(file_path)

    # create variable to name new pdf file
    name = file_path.rstrip('.xlsx')
    name = file_path.rstrip('.csv')

    # Convert Excel to PDF
    workbook.save(f'{name}.pdf', SaveFormat.PDF)



if __name__ == '__main__':
    conv2pdf()
