from watermark import pdf_set_watermark




if __name__ == "__main__":
    source_file = "data/EFEO B110.VII ភិក្ខុបាដិមោក្ខ.pdf"
    target_file = "output.pdf"
    pdf_set_watermark(source_file, target_file, target_size=None)




