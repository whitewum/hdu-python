def temperature_conversion(temp_input):
    try:
        value = float(temp_input[:-1])  # 取出数值部分
        unit = temp_input[-1].upper()    # 取出单位并转换为大写
        
        if unit == 'C':  # 摄氏转华氏
            converted_temp = (value * 9/5) + 32
            return f"转换后的温度是{converted_temp:.2f}F"
        elif unit == 'F':  # 华氏转摄氏
            converted_temp = (value - 32) * 5/9
            return f"转换后的温度是{converted_temp:.2f}C"
        else:
            return "输入格式错误"
    except ValueError:
        return "输入格式错误"

def length_conversion(length_input):
    try:
        value = float(length_input[:-1])  # 取出数值部分
        unit = length_input[-1].upper()    # 取出单位并转换为大写
        
        if unit == 'M':  # 米转英尺
            converted_length = value / 0.3048
            return f"转换后的长度是{converted_length:.2f}F"
        elif unit == 'F':  # 英尺转米
            converted_length = value * 0.3048
            return f"转换后的长度是{converted_length:.2f}M"
        else:
            return "输入格式错误"
    except ValueError:
        return "输入格式错误"

def main():
    while True:
        user_input = input("请输入温度或长度值（例如：100F、10M），输入'exit'退出：")
        if user_input.lower() == 'exit':
            break
        
        if user_input[-1].upper() in ['C', 'F']:
            print(temperature_conversion(user_input))
        elif user_input[-1].upper() in ['M', 'F']:
            print(length_conversion(user_input))
        else:
            print("输入格式错误")

if __name__ == "__main__":
    main()
