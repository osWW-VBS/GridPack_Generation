import os
import sys

# Define dict aQGC_Pars that contains info of all aQGC parameter to scan
# Format of aQGC_Pars dict:
# aQGC_Pars = { "aQGC_pars": [ aQGC_par_Ref_Number, [all +ve values to scan including zero] ] }
aQGC_Pars = {
    "FS0":[1,  [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.5, 2.0, 2.5, 3.0, 4, 5, 6, 8, 10, 20, 30, 35, 40, 45, 50]],
    "FS1":[2,  [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 7.5, 10, 15, 20, 25, 30, 33, 35]],
    
    "FM0":[3,  [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.5, 2.0, 3, 4, 5, 6, 7, 8, 9, 10]],
    "FM1":[4,  [0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.5, 3.0, 5.0, 10, 13, 15, 18, 21, 23.0, 28, 30]],
    "FM2":[5,  [0, 1, 2, 3, 6, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]],    # not included in 2016
    "FM3":[6,  [0, 1, 2, 3, 5, 8, 13, 21, 31, 44, 55, 65, 75, 85, 95, 105]],    # not included in 2016
    "FM4":[7,  [0, 1, 2, 3, 5, 8, 13, 21, 31, 44, 55, 65, 75, 85, 95, 105, 115, 121, 130]],    # not included in 2016
    "FM5":[8,  [0, 1, 2, 3, 5, 8, 13, 21, 31, 44, 55, 65, 75, 85, 95, 105, 115, 121, 130, 150, 170, 190, 200]],    # not included in 2016
    "FM6":[9,  [0, 0.2, 0.5, 0.7, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 3, 5, 7, 10, 12, 15, 18, 20]],
    "FM7":[10, [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 5.0, 10, 15, 20, 25, 30, 35, 40]],

    "FT0":[11, [0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.18, 0.20, 0.30, 0.50, 0.7, 1.0, 1.2, 1.4, 1.8, 2.0]],
    "FT1":[12, [0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.18, 0.20, 0.30, 0.50, 0.7, 1.0, 1.2, 1.4, 1.8, 2.0]],
    "FT2":[13, [0, 0.02, 0.04, 0.08, 0.14, 0.20, 0.26, 0.32, 0.5, 0.7, 0.9, 1.2, 1.7, 2.5, 2.9, 3.4, 3.9, 4.5]],
    "FT5":[16, [0, 0.2, 0.5, 0.7, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 3, 5, 7, 10, 12, 15, 18, 20, 22, 25]],    # not included in 2016
    "FT6":[17, [0, 0.2, 0.5, 0.7, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 3, 5, 7, 10, 12, 15, 18, 20, 22, 25, 27, 29]],    # not included in 2016
    "FT7":[18, [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.5, 2.0, 2.5, 3.0, 4, 5, 6, 8, 10, 20, 30, 35, 40, 45, 50, 55, 60, 65, 70]],    # not included in 2016
    "FT8":[19, [0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.18, 0.20, 0.30, 0.50, 0.7, 1.0, 1.2, 1.4, 1.8, 2.2, 2.6, 3.0, 3.5, 4.0]],    # not included in 2016
    "FT9":[20, [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.5, 2.0, 3, 4, 5, 6, 7, 8, 9, 10]]    # not included in 2016
}
twod_par_to_scan = [
		    ["FS0", "FS1"],
		    ["FM0", "FM1"]
		   ]

OutPutFile = open("reweight_card.dat","w")
input_user= input("Enetr the 1 for 1D or 2 for 2D points and 3 for both:  ")
if input_user == 1 or input_user == 3:
    print("Printing file for 1D points")
    OutPutFile.write("change helicity False\n")
    OutPutFile.write("change rwgt_dir rwgt\n")

    for key, item in aQGC_Pars.items():
	OutPutFile.write("\n\n#"+"*"*11+" "*3+key+" "*3+"*"*11+"\n")
	for parameters in item[1]:
	    if item[0] != 11:
		if parameters != 0:
		    OutPutFile.write("\nlaunch --rwgt_name="+key+"_m"+str(parameters).replace(".","p"))
		    OutPutFile.write("\n\tset anoinputs 11 0.000000e+00")
		    OutPutFile.write("\n\tset anoinputs "+str(item[0])+" -"+str(parameters)+"e-12\n")
		OutPutFile.write("\nlaunch --rwgt_name="+key+"_"+str(parameters).replace(".","p"))
		OutPutFile.write("\n\tset anoinputs 11 0.000000e+00")
		OutPutFile.write("\n\tset anoinputs "+str(item[0])+" "+str(parameters)+"e-12\n")
	    else:
		if parameters != 0:
		    OutPutFile.write("\nlaunch --rwgt_name="+key+"_m"+str(parameters).replace(".","p"))
		    OutPutFile.write("\n\tset anoinputs "+str(item[0])+" -"+str(parameters)+"e-12\n")
		OutPutFile.write("\nlaunch --rwgt_name="+key+"_"+str(parameters).replace(".","p"))
		OutPutFile.write("\n\tset anoinputs "+str(item[0])+" "+str(parameters)+"e-12\n")
    print ("*"*5+"Reweight card for 1D points is generated"+"*"*5)
OutPutFile.write("#"*50)
###########################################################
OutPutFile.write("\n\n")
if input_user == 2 or input_user == 3:
    OutPutFile.write("change helicity False\n")
    OutPutFile.write("change rwgt_dir rwgt\n")
    for i in twod_par_to_scan:
	OutPutFile.write("\n\n#"+"*"*11+" "*3+str(i)+" "*3+"*"*11+"\n")
	for key, item in aQGC_Pars.items():
	    for parameters in item[1]:
		if parameters ==0: continue
		for key2, item2 in aQGC_Pars.items():
		    for parameters2 in item2[1]:
			if parameters2 ==0: continue
			if (key==i[0] and key2==i[1]):
			    if item[0] != 11 and item2[0] != 11:
				for sign in [["",""], ["", "-"], ["-", ""], ["-","-"]]:
				    OutPutFile.write("\nlaunch --rwgt_name="+key+"_"+sign[0].replace("-","m")+str(parameters).replace(".","p")+"_"+key2+"_"+sign[1].replace("-","m")+str(parameters2).replace(".","p"))
				    OutPutFile.write("\n\n\tset anoinputs 11 0.000000e+00")
				    OutPutFile.write("\n\tset anoinputs "+str(item[0])+"  "+sign[0]+str(parameters)+"e-12")
				    OutPutFile.write("\n\tset anoinputs "+str(item2[0])+"  "+sign[1]+str(parameters2)+"e-12\n")
    print ("*"*5+"Reweight card for 2D points is generated"+"*"*5)
OutPutFile.close()
