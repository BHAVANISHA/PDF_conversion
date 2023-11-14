import PyPDF2
import os


def compress_pdf(input_path, output_path, target_size_kb):
    with open( input_path, 'rb' ) as file:
        pdf_reader = PyPDF2.PdfReader( file )
        pdf_writer = PyPDF2.PdfWriter()

        for page_num in range( len( pdf_reader.pages ) ):
            page = pdf_reader.pages[page_num]
            page.compress_content_streams()
            pdf_writer.add_page( page )

        temp_output_path = 'temp_output.pdf'
        with open( temp_output_path, 'wb' ) as temp_output_file:
            pdf_writer.write( temp_output_file )

        # Adjust the compression settings to achieve the target size
        while os.path.getsize( temp_output_path ) > target_size_kb * 1024:
            # Reduce image quality (you may need to adjust this based on your requirements)
            pdf_writer.compressContentStreams = False
            pdf_writer.compress = True
            with open( temp_output_path, 'wb' ) as temp_output_file:
                pdf_writer.write( temp_output_file )

        # Rename the temporary output file to the final output file
        os.rename( temp_output_path, output_path )


if __name__ == "__main__":
    input_pdf_path = r"C:\Users\Vrdella\Downloads\Set 2 (1)_signed_signed.pdf"
    output_pdf_path = r"C:\Users\Vrdella\Downloads\output_compressed.pdf"
    target_size_kb = 500  # Adjust this to your desired target size in kilobytes

    compress_pdf( input_pdf_path, output_pdf_path, target_size_kb )
