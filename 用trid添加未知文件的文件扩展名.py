import os
fol = 'Z:\\.RecycleBinHW\\'
for i in os.listdir(fol):
    strr = os.popen('trid '+fol+i).read()
    sc = strr.find('% (')
    os.rename(fol+i, fol+i+strr[sc+3:sc+7].lower())
