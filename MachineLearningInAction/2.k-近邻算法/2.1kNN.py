#!/usr/bin/python
# -*- coding:utf-8 -*-
from numpy import *
import operator
from operator import itemgetter, attrgetter


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet  # 输入和样本的差【矩阵】
    sqDiffMat = diffMat ** 2  # 矩阵元素平方
    sqDistances = sqDiffMat.sum(axis=1)  # 矩阵元素求和
    distances = sqDistances ** 0.5  # 和开方
    sortedDistIndicies = distances.argsort()  # 排序下标sortedDistIndicies[0]最小的下标
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]  # 统计距离小的labels
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=itemgetter(1), reverse=True)  # 排序
    return sortedClassCount[0][0]


if __name__ == '__main__':
    group, labels = createDataSet()
    res = classify0([0, 0], group, labels, 3)
    print(res)
