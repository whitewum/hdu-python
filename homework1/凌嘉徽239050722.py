def temp_convert(temp_str):
     try:
         value = float(temp_str[:-1])  # 提取数值部分
     except ValueError:
         return "请输入类似于12.34C或12.34F的格式"

     if temp_str[-1] in ['F', 'f']:
         celsius = (value - 32) * 5 / 9
         return f"{value}华氏度 = {celsius:.2f}摄氏度"
     elif temp_str[-1] in ['C', 'c']:
         fahrenheit = value * 9 / 5 + 32
         return f"{value}摄氏度 = {fahrenheit:.2f}华氏度"
     else:
         return "请输入类似于12.34C或12.34F的格式"

def length_convert(length_str):
     try:
         value = float(length_str[:-1])
     except ValueError:
         return "请输入类似于12.34m或12.34ft的格式"

     if length_str[-1] in ['M', 'm']:  # 如果输入的是米
         # 将米转换为英尺的公式
         feet = value * 3.28084
         return f"{value}米 = {feet:.2f}英尺"
     elif length_str[-1] in ['F', 'f']:  # 如果输入的是英尺
         # 将英尺转换为米的公式
         meters = value / 3.28084
         return f"{value}英尺 = {meters:.2f}米"
     else:
         return "请输入类似于12.34m或12.34ft的格式"

def main():
     while True:
         user_input = input("请输入带符号的温度或长度值：")
         if user_input[-1].upper() in ['C', 'F']:  # 识别温度转换
             result = temp_convert(user_input)
             print(result)
         elif user_input[-1].upper() in ['M', 'F']:  # 识别长度转换
             result = length_convert(user_input)
             print(result)
         else:
             print("如果需要温度转换，请输入类似于12.34C或12.34F的格式；如果需要长度转换，请输入类似于12.34m或12.34ft的格式")

if __name__ == "__main__":
     main()
