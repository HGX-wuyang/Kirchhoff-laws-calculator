import numpy as np
import matplotlib.pyplot as plt

print("========欢迎使用基尔霍夫定律计算器========")
print("本程序基于基尔霍夫定律，包括KCL与KVL，在有部分必要参数前提下，以透明过程，清晰明了得得出结果。")
print("使用说明：")
print("  输入节点数与网孔数，并输入每个节点的流入电流与流出电流，各网孔回路的升压与降压等以计算结果，后以欧姆定律得出各参数。")
print("==============使用愉快==================")

print("===============启动!====================")
num_nodes = int(input("请输入节点数："))
num_loops = int(input("请输入网孔数:"))
print("请依次输入每个节点的流入电流与流出电流（单位：A），以空格分隔：")
node_currents = []
for i in range(num_nodes):
    current = 2list(map(float,input(f"节点{i+1}:").split()))
    node_currents.append(current)
    print(f"节点{i+1}流入电流：{current[0]} A，流出电流：{current[1]} A")
print("请依次输入每个网孔的升压与降压（单位：V），以空格分隔：")
loop_voltages = []
for i in range(num_loops):
    voltage = list(map(float,input(f"网孔{i+1}:").split()))
    loop_voltages.append(voltage)
    print(f"网孔{i+1}升压：{voltage[0]} V，降压：{voltage[1]} V")
# 构建KCL方程组
A_kcl = []
B_kcl = []
for i in range(num_nodes):
    equation = [0]*num_nodes
    equation[i] = 1
    equation.append(-1)
    A_kcl.append(equation)
    B_kcl.append(node_currents[i][0] - node_currents[i][1])
A_kcl = np.array(A_kcl)
B_kcl = np.array(B_kcl)
# 构建KVL方程组
A_kvl = []
B_kvl = []
for i in range(num_loops):
    equation = [0]*num_loops
    equation[i] = 1
    equation.append(-1)
    A_kvl.append(equation)
    B_kvl.append(loop_voltages[i][0] - loop_voltages[i][1])     
A_kvl = np.array(A_kvl)
B_kvl = np.array(B_kvl)
# 合并方程组
A = np.vstack((A_kcl, A_kvl))
B = np.hstack((B_kcl, B_kvl))
# 求解方程组
solution = np.linalg.lstsq(A, B, rcond=None)[0]
# 输出结果
for i in range(num_nodes):
    print(f"节点{i+1}电压：{solution[i]:.2f} V")
for i in range(num_loops):
    print(f"网孔{i+1}电流：{solution[num_nodes + i]:.2f} A")
print("===============计算完成!==================")
# 可视化结果
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.bar(range(1, num_nodes + 1), solution[:num_nodes], color='b')
plt.xlabel('节点编号')
plt.ylabel('电压 (V)')
plt.title('节点电压分布')
plt.subplot(1, 2, 2)
plt.bar(range(1, num_loops + 1), solution[num_nodes:], color='r')
plt.xlabel('网孔编号')
plt.ylabel('电流 (A)')
plt.title('网孔电流分布')
plt.tight_layout()
plt.show()

