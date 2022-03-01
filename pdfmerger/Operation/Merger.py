import PyPDF2


def pdfmerger(loc, lis):
    """
    It will take input as location and list
    """
    if len(lis) < 1:
        return Exception("There is less than 1 files , We can't merge.")
    else:
        merge_file = PyPDF2.PdfFileMerger()
        for item in lis:
            full_path = loc + '\\' + item
            print(full_path)
            merge_file.append(PyPDF2.PdfFileReader(full_path, "rb"))
        merge_file.write("MergedFiles.pdf")
        return "Merged Successfully"
