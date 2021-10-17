# -*- encoding:utf-8 -*-

import numpy as np


class Player(object):
    def __init__(self, policy_len):
        """
        :param policy_len: 策略个数
        :param utility:  收益矩阵
        """
        self.policy_len = policy_len
        self.policy = np.random.random(self.policy_len)
        self.history = np.zeros(self.policy_len)

    def change_policy(self, op_pro):
        """
        根据传入的对手历史策略，选择自己的最优策略，并改变自己的策略
        :param op_pro: 对手策略
        """
        rock = op_pro[1] - op_pro[2]
        scissor = -op_pro[0] + op_pro[2]
        paper = op_pro[0] - op_pro[1]

        money_sum = np.array([rock, scissor, paper]) + np.random.random(3) * 0.0001
        best_choice = np.argmax(money_sum)
        self.history[best_choice] += 1
        self.policy = self.history / np.sum(self.history)

    def get_policy(self):
        """
        :return: 返回自己本轮策略
        """
        return self.policy


class MultiNash(object):
    def __init__(self, p0, p1, p2):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2

    def get_nash_equilibrium(self, loop_time):
        """
        求解纳什均衡
        :param loop_time: 迭代次数
        """
        for i in range(loop_time):
            self.p0.change_policy(self.p1.get_policy())
            self.p0.change_policy(self.p2.get_policy())
            self.p1.change_policy(self.p0.get_policy())
            self.p1.change_policy(self.p2.get_policy())
            self.p2.change_policy(self.p0.get_policy())
            self.p2.change_policy(self.p1.get_policy())

    def show_result(self):
        """
        显示结果
        """
        print('p0', self.p0.get_policy())
        print('p1', self.p1.get_policy())
        print('p2', self.p2.get_policy())


if __name__ == '__main__':
    p0 = Player(3)
    p1 = Player(3)
    p2 = Player(3)
    nash = MultiNash(p0, p1, p2)
    nash.get_nash_equilibrium(1000)
    nash.show_result()
