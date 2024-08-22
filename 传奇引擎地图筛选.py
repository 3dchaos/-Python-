import re  
import shutil  
import os  
# 获取用户输入的文件路径  
file_path = input("请输入\"MapInfo.txt\"路径: ")  
  
try:  
    with open(file_path, 'r') as file:  # 假设文件是UTF-8编码，根据实际情况调整  
        content = file.read()  
    # 使用正则表达式匹配左边是'['右边是制表符或空格的文本  
    matches = re.findall(r'\[(\s|\t)', content)  
    matches = re.findall(r'\[(?=\s|\t)', content)  
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
# 提问并等待用户输入  
MapPath = input("此处输入map文件夹路径: ")  
# 检查是否以"\"结尾  
if not MapPath.endswith("\\"):  
    # 如果不是，就加上"\"  
    MapPath += "\\"  
  
# 打印结果以确认  
print(MapPath)

saiMapPath = MapPath+"sai_maps\\"  
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
for item in cleaned_matches1:  
    # 对每个元素进行处理，并将结果添加到Maplist和saiMaplist中  
    # 注意：这里我们假设item的值是安全的，不需要进行额外的验证或清理  
    map_path = MapPath + item + ".map"  
    sai_map_path = saiMapPath + item + ".map"  
      
    # 将处理后的路径添加到列表中  
    Maplist.append(map_path)  
    saiMaplist.append(sai_map_path)  
# 确保两个列表长度相同  
if len(Maplist) == len(saiMaplist):  
    for src, dst in zip(Maplist, saiMaplist):  
        shutil.copy(src, dst)  # 或者使用shutil.copy2()来保留元数据  
else:  
    print("Maplist和saiMaplist的长度不匹配，无法复制。")
print("地图筛选完毕,被使用过的地图复制到"+saiMapPath)
