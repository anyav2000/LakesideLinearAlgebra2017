import numpy as np
import sys

"""
Created on Fri Sep  8 14:37:32 2017

@author: anyavinogradsky

program to reduce matrix to reduce row-echelon form
"""

#find leading number
def findLeading(matrix, row):
    for ii in range(0, matrix.shape[1]) :
        if (matrix.item(row, ii) != 0):
            return matrix.item(row, ii)
    return -1

def findLeadingColumn(matrix, row):
    for ii in range(0, matrix.shape[1]) :
        if (matrix.item(row, ii) != 0):
            return ii
    return -1

#create leading one
def createLeadingOne(matrix, row):
    scalar = 1.0
    
    if (findLeadingColumn(matrix, row) != -1) :
        scalar = 1.0/findLeading(matrix, row)
    
    for ii in range(0, matrix.shape[1]) :
        matrix.itemset((row, ii), matrix.item(row, ii) * scalar)
    
    return matrix

def eliminateInColumn(matrix, row, column):
    scalar = 1.0
    
    for ii in range(0, matrix.shape[0]) : #rows
        if (ii != row):
            scalar = - matrix.item(ii, column);
            for jj in range(0, matrix.shape[1]) : #columns in that row
                matrix.itemset((ii, jj), specialAddition(matrix.item(ii, jj), scalar * matrix.item(row, jj)))
    return matrix;

def specialAddition(a, b):
    if (abs(a + b) < .00001):
        return 0
    return a + b

def swapRowDown(matrix, row_a, row_b):
    temp = []
    for ii in range (0, matrix.shape[1]) :
        temp.append(matrix.item(row_a, ii))
    
    for ii in range (0, matrix.shape[1]) :
        matrix.itemset((row_a, ii), matrix.item(row_b, ii))
        matrix.itemset((row_b, ii), temp[ii])
        
    return matrix

def nonZeroRowBelow(matrix, row):
    for ii in range(row + 1, matrix.shape[0]) : #rows
        if (findLeadingColumn(matrix, ii) != -1):
            return ii 
    return -1


def rref(m) :
    for row in range(0, m.shape[0]):
        if (findLeadingColumn(m, row) != -1):
            m = createLeadingOne(m, row)
            m = eliminateInColumn(m, row, findLeadingColumn(m, row))
        elif (row < m.shape[0] - 1) :
            temp = nonZeroRowBelow(m, row)
            if (temp != -1) :
                m = swapRowDown(m, row, temp)
                m = createLeadingOne(m, row)
                m = eliminateInColumn(m, row, findLeadingColumn(m, row))            
    return m                   