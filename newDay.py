from shutil import copytree
import glob
import os

days = glob.glob('./2021/*')
days = sorted([int(i.split(' ')[1]) for i in days])

suffix = days[-1] + 1

copytree('./Sample Folder', './2021/Day ' + str(suffix))
os.rename(f'./2021/Day {suffix}/day10.py',
          f'./2021/Day {suffix}/day{suffix}.py')
