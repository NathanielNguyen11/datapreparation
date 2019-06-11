import os
import sys


# with open("/media/ubuntu/Quang/datset/list/trainval.txt") as f:
#     lines = f.readlines()
#     lines = [l for l in lines if "ROW" in l]
#     with open("/media/ubuntu/Quang/datset/list/train.txt", "w") as f1:
#         f1.writelines(lines)
i = 0
with open("/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300x3001/list/trainval.txt") as f:
    with open("/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300x3001/list/val.txt", "w") as f1:
    	with open("/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300x3001/list/train.txt", "w") as f2:
	    	lines = f.readlines()
	    	print lines
	    	for line in lines:
	            # if "ROW" in line:
	            if i< 7000:
	            	f1.write(line) 
	            else:
	            	f2.write(line)
	            i=i+1