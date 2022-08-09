import re
import urllib.request

f = urllib.request.urlopen("file:///D:/regex_assign/regexIndexHTML.html")
text= f.read()
text = text.decode()

trSelector = re.findall("<tr>(\s*<td.{1,}\s*.{1,}\s*.{1,}\s*<td.{1,}\s*<td.{1,}\s*.{1,}\s*<td.{1,}\s*<td.{1,}\s*<td.{1,}\s*<td.{1,}\s*<td.{1,}\s*)\s*<\/tr>", text)
# print(trSelector)
row = " "
file = open('RegexAssignment.txt','w')
for i in trSelector:
    appointmentReference = re.findall(r"([A-Z]{2}\d{8}-\d{5})", i)
    row += appointmentReference[0] + " "

    patientName = re.findall(r"(\">[A-Za-z]{3,}\s[\s]?[A-Za-z]{3,})", i)

    patientAddress = re.findall(r"(\w{1,}\s*\w{1,}\s\w{1,},\s)?(\w{1,}\s)?(\w{1,},\s)?(\w(1,)\s)?(\w{1,}\s)?(\w{1,}\s)?(\w{1,}\s\w{1,},\s)?\w{1,},\s*(\s*|\w{1,})\s\w{1,},\s\w{1,},.\d{5}", i)
    str = ''
    for item in patientAddress:
        for address in item:
            str = str + address
    patientPhone = re.findall(r"(\(\d{3}\)\s\d{3}-\d{4})", i)

    appointmentStatus = re.findall(r"([A-Z]{9})", i) 

    row += patientName[0] + " " + str + " " + patientPhone[0] + " " 
    if len(patientName) == 2:
        row += patientName[1] + " "
    else:
        row += "N\A" + " "
    row += appointmentStatus[0] + " "

    trackingIdOne = re.findall(r"(>\s\d{5,})", i)

    if len(trackingIdOne) == 0:
        row += "n\a" + " "
    else:
        row += trackingIdOne[0] + " "

    appointmentDAndT = re.findall(r"(\d{2}\s\w{3}\s\d{4}\s\d{2}:\d{2}\s[A-Z]{2})", i)
    row += appointmentDAndT[0] + "\n"
    file.write(row)
    print(row)
    row = " "
    
