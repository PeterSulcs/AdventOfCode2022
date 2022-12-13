import sys
import numpy as np

FILE = sys.argv[1]

rows = list()
with open(FILE, 'r') as fid:
    for line in fid:
        row = [int(x) for x in line.strip()]
        rows.append(row)

field = np.array(rows)
print(field)

# Analysis


view_from_top = np.maximum.accumulate(field, axis=0)
view_from_left = np.maximum.accumulate(field, axis=1)
view_from_bottom = np.maximum.accumulate(field[::-1,:], axis=0)
view_from_right = np.maximum.accumulate(field[:,::-1], axis=1)

visible = np.zeros(field.shape)

visible[1:,:][np.diff(view_from_top,1,axis=0)>0]=1
visible[:,1:][np.diff(view_from_left,1,axis=1)>0]=1
visible[0:-1,:][np.diff(view_from_bottom,1,axis=0)[::-1,:]>0]=1
visible[:,0:-1][np.diff(view_from_right,1,axis=1)[:,::-1]>0]=1
# print(np.diff(view_from_right,1,axis=1))

visible[0,:]=1
visible[:,0]=1
visible[-1,:]=1
visible[:,-1]=1
print(visible)
print(visible.sum())