import sys

script , input_encoding,error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline() #Readline() when called shifts internal pointer to next line
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line,encoding,errors):
    next_lang = line.strip() #Used to strip('chars') off 'chars' from start and end of line
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding,errors=errors)

    print(raw_bytes,"<=======>",cooked_string)

languages = open("languages.txt",encoding="utf-8")

main(languages , input_encoding ,error)