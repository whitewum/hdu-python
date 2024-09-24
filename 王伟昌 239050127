#王伟昌 239050127
def temperature_conversion(value):
    try:
        temp, unit = value[:-1], value[-1]
        temp = float(temp)
        if unit == 'C':
            return f"{(temp * 9/5) + 32:.2f}F"
        elif unit == 'F':
            return f"{(temp - 32) * 5/9:.2f}C"
        else:
            raise ValueError
    except ValueError:
        raise ValueError("输入格式错误")

def length_conversion(value):
    try:
        length, unit = value[:-1], value[-1]
        length = float(length)
        if unit == 'M':
            return f"{length / 0.3048:.2f}F"
        elif unit == 'F':
            return f"{length * 0.3048:.2f}M"
        else:
            raise ValueError
    except ValueError:
        raise ValueError("输入格式错误")

def main():
    input_value = input("请输入要转换的值（如 100F 或 10M）：")
    try:
        if input_value[-1] in ['C', 'F']:
            print(f"转换后的温度是{temperature_conversion(input_value)}")
        elif input_value[-1] in ['M', 'F']:
            print(f"转换后的长度是{length_conversion(input_value)}")
        else:
            raise ValueError("输入格式错误")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
