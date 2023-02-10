from gtts import gTTS
import pdfplumber
from pathlib import Path


def pdf_to_mp3(file_path='test.pdf', language='en'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        #return 'File exists!'
        
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        text = ''.join(pages)    
        with open('text1.txt', 'w', encoding='utf-8') as file:
            file.write(text)
            
        text = text.replace('\n', '')  


        my_audio = gTTS(text = text, lang = language, slow = False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return f'[+] {file_name}.mp3 saved successfulli!\n---Have a good day!---'

    else: 
        return 'File not exists, check the file path!'

def main():
    print(pdf_to_mp3(file_path= r'test_bases\fileread.pdf'))


if __name__ == '__main__':
    main()
    
    def if __name__ == '__main__':
        main(abc)
        