import re  
import shutil  
import os  
import sys

# 获取当前脚本路径
if hasattr(sys, 'frozen'):
    File = sys.executable
elif __file__:
    File = __file__
print("sys获取路径方法:", File)

# 获取当前运行脚本的目录  
run_path = File.replace("\\传奇引擎地图筛选.exe", "") 
file_path =  run_path +"\\Mir200\\Envir\\MapInfo.txt"
print("当前运行脚本的目录是：", file_path)

# 读取并处理 MapInfo.txt
try:  
    with open(file_path, 'r') as file:
        content = file.read()  
    # 使用正则表达式匹配文本
    matches = re.findall(r'\[(\s|\t)', content)  
    full_matches = re.findall(r'\[[^\]\n]*(?:\s|\t)', content)  
    processed_matches = [match.split(None, 1)[0] for match in full_matches]  
    print("匹配到的文本列表：")  
    cleaned_matches = [item.lstrip('[') for item in processed_matches] 
    cleaned_matches1 = [  
        item.split('|', 1)[-1] if '|' in item else item  
        for item in cleaned_matches
    ]  
except FileNotFoundError:  
    print(f"错误：文件 {file_path} 未找到。")  
except Exception as e:  
    print(f"读取文件或处理文本时发生错误：{e}")

# 获取地图路径
MapPath = run_path +"\\Mir200\\Map"

# 检查是否以"\"结尾
if not MapPath.endswith("\\"):  
    MapPath += "\\"  

# 打印结果以确认
print(MapPath)

saiMapPath = MapPath + "sai_maps\\"

# 尝试创建文件夹
try:  
    os.makedirs(saiMapPath)  
    print(f"文件夹 {saiMapPath} 创建成功")  
except FileExistsError:  
    print(f"文件夹 {saiMapPath} 已存在")  
except OSError as e:  
    print(f"创建文件夹时发生错误: {e.strerror}")

# 初始化两个空列表来存储处理后的路径  
Maplist = []  
saiMaplist = [] 

# 将所有的地图路径添加到列表
for item in os.listdir(MapPath):  # 获取MapPath中所有的文件
    if item.endswith(".map"):  # 只考虑 .map 文件
        map_path = MapPath + item
        sai_map_path = saiMapPath + item
        Maplist.append(map_path)
        saiMaplist.append(sai_map_path)

# 将匹配的地图名称放入一个集合，方便后续判断哪些文件不匹配
matched_maps = set(cleaned_matches1)

# 确保源列表和目标列表的长度一致
for src in Maplist:
    map_name = os.path.basename(src).replace(".map", "")  # 获取文件名（不带路径）
    if map_name not in matched_maps:  # 如果文件名不在匹配的列表中
        # 移动文件到 sai_maps 目录
        try:
            shutil.move(src, saiMapPath + os.path.basename(src))  # 移动文件
            print(f"文件 {src} 已移动到 {saiMapPath}")
        except Exception as e:
            print(f"移动文件 {src} 时出错: {e}")

print("不匹配的地图已移动到 " + saiMapPath)

input("按下回车键关闭程序...")