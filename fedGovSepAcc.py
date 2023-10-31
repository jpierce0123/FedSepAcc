import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
import filecmp

"""
Download the following files from https://www.opm.gov/data/datasets/Index.aspx?tag=FedScope
"SEPDATA_FY2005-2009"
"SEPDATA_FY2010-2014"
"SEPDATA_FY2015-2019"
"SEPDATA_FY2020-2024"

"ACCDATA_FY2005-2009"
"ACCDATA_FY2010-2014"
"ACCDATA_FY2015-2019"
"ACCDATA_FY2020-2024"

along with the data dictionaries from one of the above years groups
I chose  to get the data dictionaries from"SEPDATA_FY2020-2024"

Or if you want to run the short verion with only  the data from FY20-24 
change line 580 to  runFast = True


"""

# Define the path for the data files
PATH1 = "G:/My Drive/Data 601/New folder/"
pathSepYr05_09 = "SEPDATA_FY2005-2009"
pathSepYr10_14 = "SEPDATA_FY2010-2014"
pathSepYr15_19 = "SEPDATA_FY2015-2019"
pathSepYr20_24 = "SEPDATA_FY2020-2024"

pathAccYr05_09 = "ACCDATA_FY2005-2009"
pathAccYr10_14 = "ACCDATA_FY2010-2014"
pathAccYr15_19 = "ACCDATA_FY2015-2019"
pathAccYr20_24 = "ACCDATA_FY2020-2024"

# Read in SEPDATA table


def readSepFiles(runFast):
    if(runFast == True):
       SepYr20_24_file = PATH1 + pathSepYr20_24 + "/SEPDATA_FY2020-2024.txt"
       SepYr20_24 = pd.read_csv(SepYr20_24_file, skiprows=[
                                1], delimiter=',', quotechar='"')
       return SepYr20_24
    else:
        SepYr05_09_file = PATH1 + pathSepYr05_09 + "/SEPDATA_FY2005-2009.txt"
        SepYr05_09 = pd.read_csv(SepYr05_09_file, skiprows=[
                                 1], delimiter=',', quotechar='"')
    
        SepYr10_14_file = PATH1 + pathSepYr10_14 + "/SEPDATA_FY2010-2014.txt"
        SepYr10_14 = pd.read_csv(SepYr10_14_file, skiprows=[
                                 1], delimiter=',', quotechar='"')
    
        SepYr15_19_file = PATH1 + pathSepYr15_19 + "/SEPDATA_FY2015-2019.txt"
        SepYr15_19 = pd.read_csv(SepYr15_19_file, skiprows=[
                                 1], delimiter=',', quotechar='"')
        SepYr20_24_file = PATH1 + pathSepYr20_24 + "/SEPDATA_FY2020-2024.txt"
        SepYr20_24 = pd.read_csv(SepYr20_24_file, skiprows=[
                                 1], delimiter=',', quotechar='"')

        return SepYr05_09, SepYr10_14, SepYr15_19, SepYr20_24

def readAccFiles(runFast):
    
    if(runFast == True):
        AccYr20_24_file = PATH1 + pathAccYr20_24 + "/ACCDATA_FY2020-2024.txt"
        AccYr20_24 = pd.read_csv(AccYr20_24_file, skiprows=[
                                 1], delimiter=',', quotechar='"')
        
        return AccYr20_24

    
    else:     
        AccYr05_09_file = PATH1 + pathAccYr05_09 + "/ACCDATA_FY2005-2009.txt"
        AccYr05_09 = pd.read_csv(AccYr05_09_file, skiprows=[
                                 1], delimiter=',', quotechar='"')
    
        AccYr10_14_file = PATH1 + pathAccYr10_14 + "/ACCDATA_FY2010-2014.txt"
        AccYr10_14 = pd.read_csv(AccYr10_14_file, skiprows=[
                                 1], delimiter=',', quotechar='"')
    
        AccYr15_19_file = PATH1 + pathAccYr15_19 + "/ACCDATA_FY2015-2019.txt"
        AccYr15_19 = pd.read_csv(AccYr15_19_file, skiprows=[
                                 1], delimiter=',', quotechar='"')
    
        AccYr20_24_file = PATH1 + pathAccYr20_24 + "/ACCDATA_FY2020-2024.txt"
        AccYr20_24 = pd.read_csv(AccYr20_24_file, skiprows=[
                                 1], delimiter=',', quotechar='"')
    
        return AccYr05_09, AccYr10_14, AccYr15_19, AccYr20_24

def compareDataDicFiles():
    
    fileSep1 = str(PATH1 + pathSepYr05_09)
    fileSep2 = str(PATH1 + pathSepYr10_14)
    fileSep3 = str(PATH1 + pathSepYr15_19)
    fileSep4 = str(PATH1 + pathSepYr20_24)
    
    fileAcc1 = str(PATH1 + pathAccYr05_09)
    fileAcc2 = str(PATH1 + pathAccYr10_14)
    fileAcc3 = str(PATH1 + pathAccYr15_19)
    fileAcc4 = str(PATH1 + pathAccYr20_24)
      
    common = [
        "DTagy.txt", "DTagelvl.txt", "DTedlvl.txt", "DTgsegrd.txt",
        "DTloslvl.txt", "DTloc.txt", "DTocc.txt", "DTpatco.txt",
        "DTppgrd.txt", "DTsallvl.txt", "DTtoa.txt", "DTwrksch.txt"
    ]
    
    match, mismatch1, errors = filecmp.cmpfiles(fileSep1, fileSep2, common, shallow=False)
    match, mismatch2, errors = filecmp.cmpfiles(fileSep1, fileSep3, common, shallow=False)
    match, mismatch3, errors = filecmp.cmpfiles(fileSep1, fileSep4, common, shallow=False)
    match, mismatch4, errors = filecmp.cmpfiles(fileSep2, fileSep3, common, shallow=False)
    match, mismatch5, errors = filecmp.cmpfiles(fileSep2, fileSep4, common, shallow=False)
    match, mismatch6, errors = filecmp.cmpfiles(fileSep3, fileSep4, common, shallow=False)
    mismatchSep = mismatch1 + mismatch2 + mismatch3 + mismatch4 + mismatch5
    
    match, mismatch1, errors = filecmp.cmpfiles(fileAcc1, fileAcc2, common, shallow=False)
    match, mismatch2, errors = filecmp.cmpfiles(fileAcc1, fileAcc3, common, shallow=False)
    match, mismatch3, errors = filecmp.cmpfiles(fileAcc1, fileAcc4, common, shallow=False)
    match, mismatch4, errors = filecmp.cmpfiles(fileAcc2, fileAcc3, common, shallow=False)
    match, mismatch5, errors = filecmp.cmpfiles(fileAcc2, fileAcc4, common, shallow=False)
    match, mismatch6, errors = filecmp.cmpfiles(fileAcc3, fileAcc4, common, shallow=False)
    mismatchAcc = mismatch1 + mismatch2 + mismatch3 + mismatch4 + mismatch5
    

    return mismatchSep, mismatchAcc


# Define data types for SEPDATA columns
column_types = {
    'AGYSUB': str,
    'SEP': str,
    'EFDATE': str,
    'AGELVL': str,
    'EDLVL': str,
    'GSEGRD': str,
    'LOSLVL': str,
    'LOC': str,
    'OCC': str,
    'PATCO': int,
    'PPGRD': str,
    'SALLVL': str,
    'TOA': str,
    'WORKSCH': str,
    'WORKSTAT': int,
    'COUNT': int,
    'SALARY': str,
    'LOS': float
}

# Define data types for ACCDATA columns
column_types = {
    'AGYSUB': str,
    'ACC': str,
    'EFDATE': str,
    'AGELVL': str,
    'EDLVL': str,
    'GSEGRD': str,
    'LOSLVL': str,
    'LOC': str,
    'OCC': str,
    'PATCO': int,
    'PPGRD': str,
    'SALLVL': str,
    'TOA': str,
    'WORKSCH': str,
    'WORKSTAT': int,
    'COUNT': int,
    'SALARY': str,
    'LOS': float
}

dropColList =['STEMOCC', 'AGYSUB',"AGELVL","LOC", "EDLVL", 'GSEGRD','LOCTYP', 'LOSLVL', 'PATCO', "TOA","WORKSCH", "WORKSTAT", 'SALLVL', "COUNT"]
agyList = ["DEPARTMENT OF THE AIR FORCE",  "DEPARTMENT OF THE ARMY", "DEPARTMENT OF DEFENSE",
         "DEPARTMENT OF HOMELAND SECURITY", "DEPARTMENT OF THE NAVY", "OFFICE OF THE CYBER DIRECTOR ", "NATIONAL SECURITY COUNCIL"]
sepList = ["Transfer Out - Individual Transfer", "Transfer Out - Mass Transfer", "nan"]
accList = ["Transfer In - Individual Transfer","Transfer In - Mass Transfer", "nan"]

# General tables
def genTables():
    # Read in Agency Dimension Translation Table
    dtagy_file = PATH1 + pathSepYr20_24 + "/DTagy.txt"
    dtagy = pd.read_csv(dtagy_file, skiprows=[1], delimiter=',', quotechar='"')
    dtagy = dtagy.set_index(['AGYSUB'])
    for i, row in dtagy.iterrows():  
        agyt = str(row.at['AGYT'])
        agyt = agyt[3:]
        dtagy.at[i, 'AGYT'] = agyt  
        
        agysubt = str(row.at['AGYSUBT'])
        agysubt = agysubt[5:]
        dtagy.at[i, 'AGYSUBT'] = agysubt  
    dtagy = dtagy.drop(["AGYTYP","AGYTYPT","AGY"] , axis=1, errors='ignore')
   

    # Read in Age Level Dimension Translation Table
    dtagelvl_file = PATH1 + pathSepYr20_24 + "/DTagelvl.txt"
    dtagelvl = pd.read_csv(dtagelvl_file, skiprows=[
                           1], delimiter=',', quotechar='"')
    dtagelvl = dtagelvl.set_index(['AGELVL'])


    # Read in Age Level Dimension Translation Table
    dtedlvl_file = PATH1 + pathSepYr20_24 + "/DTedlvl.txt"
    dtedlvl = pd.read_csv(dtedlvl_file, skiprows=[1], delimiter=',', quotechar='"')
    dtedlvl = dtedlvl.set_index(['EDLVL'])
    dtedlvl = dtedlvl.drop(["EDLVLTYP","EDLVLT"] , axis=1, errors='ignore')
   

    # Read in GSEGRD Dimension Translation Table
    dtgsegrd_file = PATH1 + pathSepYr20_24 + "/DTgsegrd.txt"
    dtgsegrd = pd.read_csv(dtgsegrd_file, skiprows=[1], delimiter=',', quotechar='"')
    dtgsegrd = dtgsegrd.set_index(['GSEGRD'])
 

    # Read in Length of Service Dimension Translation Table
    dtloslvl_file = PATH1 + pathSepYr20_24 + "/DTloslvl.txt"
    dtloslvl = pd.read_csv(dtloslvl_file, skiprows=[1], delimiter=',', quotechar='"')
    dtloslvl = dtloslvl.set_index(['LOSLVL'])


    # Read in Location Dimension Translation Table
    dtloc_file = PATH1 + pathSepYr20_24 + "/DTloc.txt"
    dtloc = pd.read_csv(dtloc_file, skiprows=[1], delimiter=',', quotechar='"')
    dtloc = dtloc.set_index(['LOC'])
    for i, row in dtloc.iterrows():  
        sLoc = str(row.at['LOCT'])
        sLoc = sLoc[3:]
        dtloc.at[i, 'LOCT'] = sLoc  
    dtloc = dtloc.drop(["LOCTYPT"] , axis=1, errors='ignore')


    # Read in Occupation Dimension Translation Table
    dtocc_file = PATH1 + pathSepYr20_24 + "/DTocc.txt"
    dtocc = pd.read_csv(dtocc_file, skiprows=[1], delimiter=',', quotechar='"')
    for i, row in dtocc.iterrows():  
        sOCCT = str(row.at['OCCT'])
        sOCCT = sOCCT[5:]
        dtocc.at[i, 'OCCT'] = sOCCT      
        OCCFam = str(row.at['OCCFAMT'])
        OCCFam = OCCFam[5:]
        dtocc.at[i, 'OCCFAMT'] = OCCFam        
    dtocc = dtocc.drop(["OCCTYP", "OCCTYPT", "OCCFAM"] , axis=1, errors='ignore')
    dtocc = dtocc.set_index(['OCC'])
 

    # Read in PATCO Dimension Translation Table
    dtpatco_file = PATH1 + pathSepYr20_24 + "/DTpatco.txt"
    dtpatco = pd.read_csv(dtpatco_file, skiprows=[
                          1], delimiter=',', quotechar='"')
    dtpatco = dtpatco.set_index(['PATCO'])


    # Read in Pay Plan & Grade Dimension Translation Table
    dtppgrd_file = PATH1 + pathSepYr20_24 + "/DTppgrd.txt"
    dtppgrd = pd.read_csv(dtppgrd_file, skiprows=[
                          1], delimiter=',', quotechar='"')
    for i, row in dtppgrd.iterrows():  
        payplan = str(row.at['PAYPLANT'])
        payplan = payplan[3:]
        dtppgrd.at[i, 'PAYPLANT'] = payplan                 
    dtppgrd = dtppgrd.drop(["PPTYP", "PPTYPT", "PPGROUP",  "PPGROUPT"] , axis=1, errors='ignore')
    dtppgrd = dtppgrd.set_index("PPGRD")


    # Read in Salary Level Dimension Translation Table
    dtsallvl_file = PATH1 + pathSepYr20_24 + "/DTsallvl.txt"
    dtsallvl = pd.read_csv(dtsallvl_file, skiprows=[
                           1], delimiter=',', quotechar='"')
    dtsallvl = dtsallvl.set_index("SALLVL")


    # Read in Type of Appointment Dimension Translation Table
    dttoa_file = PATH1 + pathSepYr20_24 + "/DTtoa.txt"
    dttoa = pd.read_csv(dttoa_file, skiprows=[1], delimiter=',', quotechar='"')
    dttoa = dttoa.drop(["TOATYP", "TOAT"] , axis=1, errors='ignore')
    dttoa = dttoa.set_index("TOA")


    # Read in Work Schedule Dimension Translation Table
    dtwrksch_file = PATH1 + pathSepYr20_24 + "/DTwrksch.txt"
    dtwrksch = pd.read_csv(dtwrksch_file, skiprows=[
                           1], delimiter=',', quotechar='"')  
    dtwrksch = dtwrksch.drop(["WSTYP", "WORKSCHT"] , axis=1, errors='ignore')
    dtwrksch = dtwrksch.set_index("WORKSCH")

    
    # Read in Separation Dimension Translation Table
    dtsep20_24_file = PATH1 + pathSepYr20_24 + "/DTsep.txt"
    dtsep = pd.read_csv(dtsep20_24_file, skiprows=[
                             1], delimiter=',', quotechar='"')
    dtsep = dtsep.set_index(['SEP'])

    
    # Read in Separation Dimension Translation Table
    dtacc20_24_file = PATH1 + pathAccYr20_24 + "/DTacc.txt"
    dtacc = pd.read_csv(dtacc20_24_file, skiprows=[
                             1], delimiter=',', quotechar='"')
    dtacc = dtacc.set_index(['ACC'])
   
    
    return dtacc, dtsep, dtwrksch, dttoa, dtsallvl, dtppgrd, dtpatco, dtocc, dtloc, dtloslvl, dtgsegrd, dtedlvl, dtagelvl, dtagy

   
    
  
def getData(runFast):
    rf = runFast
    if (rf == True):   
       SepYr = readSepFiles(rf)
       SepTotal = sepDataClean(SepYr)
       
       AccYr= readAccFiles(rf)
       AccTotal = accDataClean(AccYr)
       
    else:
       SepYr05_09, SepYr10_14, SepYr15_19, SepYr20_24 = readSepFiles(rf)
       SepYr05_09 = sepDataClean(SepYr05_09)
       SepYr10_14 = sepDataClean(SepYr10_14)
       SepYr15_19 = sepDataClean(SepYr15_19)
       SepYr20_24 = sepDataClean(SepYr20_24)

       sepFrames = [SepYr05_09, SepYr10_14, SepYr15_19, SepYr20_24]
       SepTotal = pd.concat(sepFrames)
       
               
       AccYr05_09, AccYr10_14, AccYr15_19, AccYr20_24 = readAccFiles(rf)
       AccYr05_09 = accDataClean(AccYr05_09)
       AccYr10_14 = accDataClean(AccYr10_14)
       AccYr15_19 = accDataClean(AccYr15_19)
       AccYr20_24 = accDataClean(AccYr20_24)

       accFrames = [AccYr05_09, AccYr10_14, AccYr15_19, AccYr20_24]
       AccTotal = pd.concat(accFrames)
       
    return SepTotal, AccTotal


def sepDataClean(df):
    df = df
    df = df.merge(dtsep  , on='SEP', how='left')  
    df = df.merge(dtagy, on='AGYSUB', how='left')
  
    agyList = ["DEPARTMENT OF THE AIR FORCE",  "DEPARTMENT OF THE ARMY", "DEPARTMENT OF DEFENSE",
             "DEPARTMENT OF HOMELAND SECURITY", "DEPARTMENT OF THE NAVY", "OFFICE OF THE CYBER DIRECTOR ", "NATIONAL SECURITY COUNCIL"]
    sepType = ["Transfer Out - Individual Transfer", "Transfer Out - Mass Transfer", "nan"]
    df = df.apply(lambda row: row[df['AGYT'].isin(agyList)])
    df = df.apply(lambda row: row[df['SEPT'].isin(sepType)])  
  
    
    df = df.merge(dtagelvl , on='AGELVL', how='left')
    df = df.merge(dtedlvl, on='EDLVL', how='left')
    df = df.merge(dtgsegrd, on='GSEGRD', how='left')
    df = df.merge(dtloslvl , on='LOSLVL', how='left')
    df = df.merge(dtloc, on='LOC', how='left')
    df = df.merge(dtocc , on='OCC', how='left')
    df = df.merge(dtpatco  , on='PATCO', how='left')
    df = df.merge(dtppgrd , on='PPGRD', how='left')
    df = df.merge(dtsallvl , on='SALLVL', how='left')
    df = df.merge(dttoa , on='TOA', how='left')
    df = df.merge(dtwrksch , on='WORKSCH', how='left')
    
    df = df.drop(dropColList, axis=1, errors='ignore') 

 #   df = df.merge(dtacc, on='ACC', how='left')
    
    # replace NA/** as <NA> type which is a int type
    df = df.replace('**', pd.NA)
    df = df.replace('nan', pd.NA)
    df = df.replace('none', pd.NA)
    df = df.replace('None', pd.NA)
    df = df.replace('XXXX', pd.NA)
    df = df.drop([  ]) 
   
    for i, row in df.iterrows():
        sDate = str(row.at['EFDATE'])
        year = int(sDate[:4])
        month = int(sDate[4:6])
        df.at[i, 'EFDATE'] = date(year, month, 1)   
        df.at[i, 'YEAR'] = int(year)
    return df


def accDataClean(df):
    df = df
  
    df = df.merge(dtacc, on='ACC', how='left')
    df = df.merge(dtagy, on='AGYSUB', how='left')
  
    df = df.apply(lambda row: row[df['AGYT'].isin(agyList)])
    df = df.apply(lambda row: row[df['ACCT'].isin(accList)])  
    
    df = df.merge(dtagelvl , on='AGELVL', how='left')
    df = df.merge(dtedlvl, on='EDLVL', how='left')
    df = df.merge(dtgsegrd, on='GSEGRD', how='left')
    df = df.merge(dtloslvl , on='LOSLVL', how='left')
    df = df.merge(dtloc, on='LOC', how='left')
    df = df.merge(dtocc , on='OCC', how='left')
    df = df.merge(dtpatco  , on='PATCO', how='left')
    df = df.merge(dtppgrd , on='PPGRD', how='left')
    df = df.merge(dtsallvl , on='SALLVL', how='left')
    df = df.merge(dttoa , on='TOA', how='left')
    df = df.merge(dtwrksch , on='WORKSCH', how='left')
    
    df = df.drop(dropColList, axis=1, errors='ignore') 
    
    # replace NA/** as <NA> type which is a int type
    df = df.replace('**', pd.NA)
    df = df.replace('nan', pd.NA)
    df = df.replace('none', pd.NA)
    df = df.replace('None', pd.NA)
    df = df.replace('XXXX', pd.NA)
   
   
   
    for i, row in df.iterrows():
        
        sDate = str(row.at['EFDATE'])
        year = int(sDate[:4])
        month = int(sDate[4:6])
        df.at[i, 'EFDATE'] = date(year, month, 1) 
        df.at[i, 'YEAR'] = int(year)
    return df


def dfBasicInfo(df):
    if isinstance(df, pd.DataFrame) == False:
        TypeError(df + " is not a dataFrame")
    dfHead = df.head()
    dfTail = df.tail()
    dfShape = df.shape
    dfRows = dfShape[0]
    dfCols = dfShape[1]
    return (dfHead, dfTail, dfShape, dfRows, dfCols)
        

    df = df
    if isinstance(df, pd.DataFrame) == False:
        TypeError(df + " is not a dataFrame")
    dfColNames = list(df.columns.values)
    iCol = len(dfColNames)
    for x in range(iCol):
        subDF = df[dfColNames[x]]
        if subDF.dtype == 'datetime64[ns]':
            print(dfColNames[x] + " is dateTime  datetime64[ns] ")
        elif subDF.dtype == 'int'or subDF.dtype == 'float' :
            colMed = subDF.median(axis=0)
            print(dfColNames[x] + " median value is " + str(colMed))
        else:
            print(dfColNames[x] + " does not have numberical values")
 

def moreInfo(accDF, sepDF):
    accDF = accDF
    sepDF = sepDF
    hires= accDF.shape[0]
    left= sepDF.shape[0]
    print("people hired between FY05-FY23: " + str(hires))
    print("people left between FY05-FY23: " + str(left))
    print("Change in personel from FY05-FY23: " + str(hires-left))
    print("Mean Salary of those hired from FY05-FY23: $" + str(int(accDesc["SALARY"]["mean"])))
    print("Mean Salary of those who left from FY05-FY23: $" + str(int(sepDesc["SALARY"]["mean"])))
    
    print("Median Salary of those hired from FY05-FY23: $" + str(int(accDesc["SALARY"]["50%"])))
    print("Median Salary of those who left from FY05-FY23: $" + str(int(sepDesc["SALARY"]["50%"])))
    return True
    
def saleryHistogramsFull():
    fig, axs = plt.subplots()
    s1 = SepTotal["SALARY"]
    a1 = AccTotal["SALARY"]
    s1.plot.hist(bins=15,label = "Leaving", ylabel="Counts",xlabel="Salary[$]", title='USG Salaries', ls='dashed', alpha = 0.55, color = '#1b9e77')
    a1.plot.hist(bins=15,label = "Joining", ylabel="Counts",xlabel="Salary[$]", title='USG Salaries', ls='dotted',alpha = 0.55, color = '#7570b3')
    plt.legend()
    plt.show() 
    return True

    
    
def yearsService():
  fig2, axs2 = plt.subplots(nrows=2, ncols=2, layout="constrained", figsize=(20, 20))
  s0 = SepTotal["LOS"]
  a0 = AccTotal["LOS"]
  axs2[0,0].hist(s0, bins=15, label = "Leaving", ls='dashed', alpha = 0.55, color = '#1b9e77')
  axs2[0,0].hist(a0,bins=15, label = "Joining*", ls='dotted',alpha = 0.55, color = '#7570b3')
  axs2[0,0].legend()
  axs2[0,0].set_title('USG Years of Service')
  axs2[0,0].text(40, 14000, '* includes prior service with other agencies/military', style='italic')
  axs2[0,0].set_ylabel('counts [100000] ')
  axs2[0,0].set_xlabel('Years')  
  
  s1 = SepTotal[~( (SepTotal['LOS'] <= 20) ) ]['LOS']
  a1 = AccTotal[~( (AccTotal['LOS'] <= 20))]['LOS']
  axs2[1,1].hist(s1,bins=15, label = "Leaving", ls='dashed', alpha = 0.55, color = '#1b9e77')
  axs2[1,1].hist(a1,bins=15, label = "Joining*", ls='dotted',alpha = 0.55, color = '#7570b3')
  axs2[1,1].legend()
  axs2[1,1].set_title('USG Years of Service')
  axs2[1,1].set_ylabel('counts ')
  axs2[1,1].set_xlabel('Years') 
   
  s3 = SepTotal[~((SepTotal['LOS'] >= 3) | (SepTotal['LOS'] == 0)) ]['LOS']
  a3 = AccTotal[~((AccTotal['LOS'] >= 3) | (AccTotal['LOS'] == 0))]['LOS']
  axs2[0,1].hist(s3,bins=15, label = "Leaving", ls='dashed', alpha = 0.55, color = '#1b9e77')
  axs2[0,1].hist(a3,bins=15, label = "Joining*", ls='dotted',alpha = 0.55, color = '#7570b3')
  axs2[0,1].legend()
  axs2[0,1].set_title('USG Years of Service  within probationary period(3yrs)')
  axs2[0,1].set_ylabel('counts ')
  axs2[0,1].set_xlabel('Years') 
  
  s2 = SepTotal[~((SepTotal['LOS'] <= 10) | (SepTotal['LOS'] >= 20) ) ]['LOS']
  a2 = AccTotal[~((AccTotal['LOS'] <= 10) | (AccTotal['LOS'] >= 20))]['LOS']
  axs2[1,0].hist(s2,bins=15, label = "Leaving", ls='dashed', alpha = 0.55, color = '#1b9e77')
  axs2[1,0].hist(a2,bins=15, label = "Joining*", ls='dotted',alpha = 0.55, color = '#7570b3')
  axs2[1,0].legend()
  axs2[1,0].set_title('USG Years of Service')
  axs2[1,0].set_ylabel('counts ')
  axs2[1,0].set_xlabel('Years')  
  
def moreSepPlots(sepDF):
    sepDF = sepDF
    dfColNames = list(sepDF.columns.values)
    iCol = len(dfColNames)
    
    fig, ax = plt.subplots()
   # print(sepDF.value_counts()[:10])
    startDate = sepDF["EFDATE"].min().strftime('%b %Y')
    endDate = sepDF["EFDATE"].max().strftime('%b %Y')
    for x in range(iCol):
        col = dfColNames[x]
        y = sepDF[col].value_counts()
        y = y.head(15)
        y.plot.barh(xlabel="Counts", color = '#1b9e77', title='USG Sepration Metrics from '+ startDate + "-"+ endDate + 'for '+col)
        plt.show()       
    return True

    return True

def moreAccPlots(accDF):
    accDF = accDF
    dfColNames = list(accDF.columns.values)
    iCol = len(dfColNames)
    
    fig, ax = plt.subplots()
    startDate = accDF["EFDATE"].min().strftime('%b %Y')
    endDate = accDF["EFDATE"].max().strftime('%b %Y')
   # print(AccTotal.value_counts()[:10])
    for x in range(iCol):
        col = dfColNames[x]
        y = accDF[col].value_counts()
        y = y.head(15)
        y.plot.barh(xlabel="Counts", color = '#7570b3', title='USG Acceptance Metrics from '+ startDate + "-"+ endDate + 'for '+col)
        plt.show() 
    return True
       

def morePlots(accDF, sepDF):
    
def split_years(dt):
   [dt[dt['YEAR'] == y] for y in dt['YEAR'].unique()]
    accDF = accDF
    sepDF = sepDF
    dfColNames = list(accDF.columns.values)
    iCol = len(dfColNames)

    fig, ax = plt.subplots()
    startDate = accDF["EFDATE"].min().strftime('%b %Y')
    endDate = accDF["EFDATE"].max().strftime('%b %Y')
   # print(AccTotal.value_counts()[:10])
    for x in range(iCol):
        col = dfColNames[x]
        if col not in ['SEP', 'SEPT', 'ACC', 'ACCT']:    
            a = accDF[col].value_counts()
            a = a.head(15)
            s = sepDF[col].value_counts()
            s = s.head(15)
            #a.plot.barh(xlabel="Counts", color = '#666666', title='USG Acceptance Metrics from '+ startDate + "-"+ endDate + 'for '+col)
            s.plot.barh(label = "Leaving", ylabel=col, xlabel="Counts", ls='dashed', alpha = 0.55 , color = '#1b9e77', title='USG Metrics from '+ startDate + "-"+ endDate + 'for '+col)
            a.plot.barh(label = "Joining", ylabel=col, xlabel="Counts",ls='dotted',alpha = 0.55, color = '#7570b3', title='USG Metrics from '+ startDate + "-"+ endDate + 'for '+col)
            plt.legend()
            plt.show()  
    return True
       
   
dtacc, dtsep, dtwrksch, dttoa, dtsallvl, dtppgrd, dtpatco, dtocc, dtloc, dtloslvl, dtgsegrd, dtedlvl, dtagelvl, dtagy = genTables()
runFast = False


SepTotal, AccTotal = getData(runFast)


sepBasicInfo = dfBasicInfo(SepTotal)
sepDesc = SepTotal.describe()

accBasicInfo = dfBasicInfo(AccTotal)
accDesc = AccTotal.describe()



moreInfo(AccTotal, SepTotal)
saleryHistogramsFull()
yearsService()
moreSepPlots(SepTotal)
moreAccPlots(AccTotal)
morePlots(AccTotal, SepTotal)




#mismatchSep, mismatchAcc = compareDataDicFiles()




