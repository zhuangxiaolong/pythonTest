from mtranslate import translate


def main():
    to_translate = 'Key'
    print(translate(to_translate, 'zh'))

if __name__ == '__main__':
    main()