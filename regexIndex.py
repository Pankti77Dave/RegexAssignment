import re
import urllib.request

f = urllib.request.urlopen("file:///D:/regex_assign/test.html")
text= f.read()
text = text.decode()

appointmentReference = re.findall(r"([A-Z]{2}\d{8}-\d{5})", text)
print(appointmentReference)

patientName = re.findall(r"([A-Za-z]{3,}\s[A-Za-z]{3,})", text)
print(patientName)

patientPhone = re.findall(r"(\(\d{3}\)\s\d{3}-\d{4})", text)
print(patientPhone)

agentNameOne = re.findall(r"(>[A-Za-z]{6}\s[A-Za-z]{5,})", text)
print(agentNameOne)
agentNameTwo = re.findall(r"(N\/A)", text)
print(agentNameTwo)

agentName = agentNameOne + agentNameTwo


appointmentStatus = re.findall(r"([A-Z]{9})", text)
print(appointmentStatus)

trackingIdOne = re.findall(r"(>\s\d{5,})", text)
print(trackingIdOne)

trackingIdTwo = re.findall(r"(\sn\/a)", text)
print(trackingIdTwo)

trackingId = trackingIdOne + trackingIdTwo

appointmentDAndT = re.findall(r"(\d{2}\s\w{3}\s\d{4}\s\d{2}:\d{2}\s[A-Z]{2})", text)
print(appointmentDAndT)


# Python code to create a file
file = open('RegexAssignment.txt','w')
data = " "
for i in range(0,34):
    data = appointmentReference[i] + " " + patientName[i] + " " + agentName[i] + " " + appointmentStatus[i] + " " +  trackingId[i] + " " + appointmentDAndT[i] + "\n"
    file.write(data)
    data = " "
file.close()
