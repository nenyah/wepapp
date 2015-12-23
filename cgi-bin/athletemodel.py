import pickle
from athletelist import AthleteList

def readData(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return(AthleteList(templ.pop(0),templ.pop(0),templ))
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)
def get_name_from_store():
    athletes = getFromStore()
    response = [athletes[each_ath].name for each_ath in athletes]
    return(response)

def putToStore(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = readData(each_file)
        #建立一个字典all_athletes，键是ath.name 即实例属性的name属性
        #值是实例本身，因为实例是一个AthleteList对象
        #AthleteList是继承的List，本身是一个列表
        all_athletes[ath.name] = ath
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print('File error(put_and_store):' + \
              str(ioerr))
    return(all_athletes)

def getFromStore():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('File error(pget_and_store):' + \
              str(ioerr))
    return(all_athletes)


    
