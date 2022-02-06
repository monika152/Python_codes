
from PyPDF2 import PdfFileMerger

def my_pdf_merger(pdf_files_list:list, output_file_name:str):
    """Takes a list of file names and generate a single pdf file

    Args:
        pdf_files_list (list): exaample:['T1.pdf','T2.pdf']
        output_file_name (str): example "result3.pdf"
    """


    pdf_list = pdf_files_list

    # Instance
    merger = PdfFileMerger()


    for pdf in pdf_list:
        merger.append(pdf)

    merger.write(output_file_name)
    print("File merged successfully!")