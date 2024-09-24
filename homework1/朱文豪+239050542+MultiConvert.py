def temperature_conversion(temp_input):
    # 检查输入的最后一位是否为C或F
    if temp_input[-1] not in ['C', 'F']:
        return "输入格式错误"

    # 提取数值部分
    try:
        value = float(temp_input[:-1])
    except ValueError:
        return "输入格式错误"

    # 根据单位进行转换
    if temp_input[-1] == 'C':
        # 摄氏度转华氏度
        converted_value = value * 9/5 + 32
        return f"转换后的温度是{converted_value:.2f}F"
    elif temp_input[-1] == 'F':
        # 华氏度转摄氏度
        converted_value = (value - 32) * 5/9
        return f"转换后的温度是{converted_value:.2f}C"

def length_conversion(length_input):
    # 检查输入的最后一位是否为M或F
    if length_input[-1] not in ['M', 'F']:
        return "输入格式错误"

    # 提取数值部分
    try:
        value = float(length_input[:-1])
    except ValueError:
        return "输入格式错误"

    # 根据单位进行转换
    if length_input[-1] == 'M':
        # 米转英尺
        converted_value = value / 0.3048
        return f"转换后的长度是{converted_value:.2f}F"
    elif length_input[-1] == 'F':
        # 英尺转米
        converted_value = value * 0.3048
        return f"转换后的长度是{converted_value:.2f}M"

def weight_conversion(weight_input):
    # 检查输入的最后一位是否为K或L
    if weight_input[-1] not in ['K', 'L']:
        return "输入格式错误"

    # 提取数值部分
    try:
        value = float(weight_input[:-1])
    except ValueError:
        return "输入格式错误"

    # 根据单位进行转换
    if weight_input[-1] == 'K':
        # 千克转磅
        converted_value = value * 2.20462
        return f"转换后的重量是{converted_value:.2f}L"
    elif weight_input[-1] == 'L':
        # 磅转千克
        converted_value = value / 2.20462
        return f"转换后的重量是{converted_value:.2f}K"

def main():
    print("欢迎使用多功能转换器！")
    print("请输入带有单位的温度、长度或重量值（例如：100F、10M、50K）")

    while True:
        user_input = input("请输入要转换的值（输入'exit'退出）：")

        if user_input.lower() == 'exit':
            print("感谢使用，再见！")
            break

        # 检查输入是否为温度、长度或重量
        if user_input[-1] in ['C', 'F']:
            result = temperature_conversion(user_input)
        elif user_input[-1] in ['M', 'F']:
            result = length_conversion(user_input)
        elif user_input[-1] in ['K', 'L']:
            result = weight_conversion(user_input)
        else:
            result = "输入格式错误"

        print(result)

if __name__ == "__main__":
    main()
