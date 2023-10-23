def convert_base(number, source_base, target_base):
    if source_base < 2 or source_base > 10 or target_base < 2 or target_base > 10:
        return "A számrendszer csak 2-től 10-ig számít"

    decimal_value = int(str(number), source_base)
    result = format(decimal_value, f'{len(str(number))}d')
    return int(result, target_base)

source_base = int(input("adja meg a forrás számrendszer számot (2-10): "))
target_base = int(input("adja meg a cél számrendszer számot (2-10): "))
number = input(" adja meg a számot a forrás számrendszerben: ")

result = convert_base(number, source_base, target_base)
print(f"Az eredmény a {target_base} es számrendszerben: {result}")