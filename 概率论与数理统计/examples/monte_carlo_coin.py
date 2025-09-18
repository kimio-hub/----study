import random
import math

def simulate_coin(n, p=0.5):
    """模拟 n 次独立伯努利试验，返回正面出现次数"""
    heads = sum(1 for _ in range(n) if random.random() < p)
    return heads

def estimate_frequency(n, trials=1000, p=0.5):
    freqs = []
    for _ in range(trials):
        heads = simulate_coin(n, p)
        freqs.append(heads / n)
    mean = sum(freqs) / trials
    var = sum((x - mean) ** 2 for x in freqs) / (trials - 1)
    std = math.sqrt(var)
    return mean, std, freqs

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='蒙特卡洛模拟：抛硬币频率收敛')
    parser.add_argument('-n', type=int, default=1000, help='每次试验的掷币次数（默认 1000）')
    parser.add_argument('-t', type=int, default=500, help='蒙特卡洛重复次数（默认 500）')
    parser.add_argument('-p', type=float, default=0.5, help='硬币正面概率（默认 0.5）')
    args = parser.parse_args()

    mean, std, freqs = estimate_frequency(args.n, args.t, args.p)
    print(f"n={args.n}, trials={args.t}, p={args.p}")
    print(f"频率均值 = {mean:.6f}, 经验标准差 = {std:.6f}")
    # 计算 95% 置信区间（基于样本均值的正态近似）
    z = 1.96
    se = std / math.sqrt(args.t)
    print(f"95% 置信区间（均值）= ({mean - z*se:.6f}, {mean + z*se:.6f})")

    # 输出前 10 个重复的频率作为示例
    print("示例频率（前10个）：", freqs[:10])
