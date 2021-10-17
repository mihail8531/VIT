import argparse

d = {">": "0", "<": "1", "+": "2", "-": "3", ".": "4", ",": "5", "[": "6", "]": "7"}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Утилита для перевода Brainfuck программ в файл для ОЗУ logisim')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--file", default=None, type=str, help="Считать Brainfuck код из файла")
    group.add_argument("-s", "--string", default=None, type=str, help="Считать Brainfuck код одной строкой")
    parser.add_argument("-o", "--out", default=None, type=str, help="Записать программу в файл")
    args = parser.parse_args()
    inp = ""
    if args.file is not None:
        with open(args.file, "r") as f:
            for line in f:
                inp += line.strip()
    else:
        inp = args.string
    res = inp
    for key in d:
        res = res.replace(key, d[key])
    res = " ".join(res)
    if args.out is not None:
        res = "v2.0 raw\n" + res
        with open(args.out, "w") as f:
            f.write(res)
        print(f"Записано в {args.out}")
    else:
        print(res)



