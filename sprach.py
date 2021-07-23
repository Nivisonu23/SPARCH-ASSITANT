import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            talk('Say or Ask something..')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'sprach' in command:
                command = command.replace('sprach', '')
                print(command)
    except:
        pass
    return command

def run_sprach():
    command = take_command()
    if '55' in command:
        print('NIRMALA\nRoll no:18IT1248')
        print('DOB:05-06-2001')
        print('10th Percentage = 95.40 \n12th Percentage = 83.91 \nCGPA = 7.76')
        print('Number Of Standing Arrears = 0 \nHistory Of Arrears = 1')
        print('EMAIL ID:nimi5793@gmail.com')
    elif '56' in command:
        print('NIRMALKUMAR\n18IT1259')
        print('DOB:23-12-2000')
        print('10th Percentage = 88.00 \n12th Percentage = 67.00 \nCGPA = 6.96')
        print('Number Of Standing Arrears = 8 \nHistory Of Arrears = 8')
        print('EMAIL ID:nirmalkumar2312200@gmail.com')
    elif '57' in command:
        print('NIVEDITHA M\n18IT1232')
        print('DOB:23-12-2000')
        print('10th Percentage = 94.20 \n12th Percentage = 84.75 \nCGPA = 8.43')
        print('Number Of Standing Arrears = NIL \nHistory Of Arrears = NIL')
        print('nivisonu23@gmail.com')
    elif '58' in command:
        print('NIVEDITHA U\n18IT1901')
        print('DOB:12-07-2001')
        print('10th Percentage = 79.80 \n12th Percentage = 69.25 \nCGPA = 7.53')
        print('Number Of Standing Arrears = 3 \n History Of Arrears = 6')
        print('EMAIL ID:nivedithaudaykumar12@gmail.com')
    elif '59' in command:
        print('PAVITHRA\n18IT1121')
        print('DOB:07-06-2001')
        print('10th Percentage = 85.80 \n12th Percentage = 70.42 \nCGPA = 7.38')
        print('Number Of Standing Arrears = 1 \nHistory Of Arrears = 5')
        print('EMAIL ID:hacpavithra2001@gmail.com')
    elif '60' in command:
        print('POOJA\n18IT1752')
        print('DOB:12-08-2000')
        print('10th CGPA = 10.00 \n12th Percentage = 76.83 \nCGPA = 7.94')
        print('Number Of Standing Arrears = 0 \nHistory Of Arrears = 0')
        print('EMAIL ID:poojashivaji2000@gmail.com')
    elif '61' in command:
        print('PRADEEP\n18IT1235')
        print('DOB:14-03-2001')
        print('10th Percentage = 95.40 \n12th Percentage = 79.90 \nCGPA = 7.63')
        print('Number Of Standing Arrears = 1 \nHistory Of Arrears = 2')
        print('EMAIL ID:pradeepsaravanan2001@gmail.com')
    elif '62' in command:
        print('PRADHIKSHA\n18IT1225')
        print('DOB:31-05-2001')
        print('10th Percentage = 90.80 \n12th Percentage = 87.83 \nCGPA = 7.65')
        print('Number Of Standing Arrears = 0 \nHistory Of Arrears = 1')
        print('EMAIL ID:pradhikshavelu315@gmail.com')
    elif '63' in command:
        print('PRAVEEN\n18IT1120')
        print('DOB:11-05-2001')
        print('10th Percentage = 89.00 \n12th Percentage = 80.50 \nCGPA = 8.63')
        print('Number Of Standing Arrears = 0 \nHistory Of Arrears = 0')
        print('EMAIL ID:praveenpugalenthi@gmail.com')
    elif '64' in command:
        print('PREMA NADNHINI\n18IT1212')
        print('DOB:04-05-2000')
        print('10th Percentage = 97.20 \n12th Percentage = 85.41 \nCGPA = 7.99')
        print('Number Of Standing Arrears = 0 \nHistory Of Arrears = 2')
        print('EMAIL ID:premanandhini.a.m@gmail.com')
    elif '65' in command:
        print('PRIYANKA\n18IT1114')
        print('DOB:14-05-2001')
        print('10th Percentage = 95.80 \n12th Percentage = 80.83 \nCGPA = 8.63')
        print('Number Of Standing Arrears = 0 \nHistory Of Arrears = 0')
        print('EMAIL ID:priyankajawahar1405@gmail.com')
    elif '66' in command:
        print('RAGHAVENDRAN\n18IT1216')
        print('DOB:20-12-2000')
        print('10th Percentage = 80.00 \n12th Percentage = 84.00 \nCGPA = 7.06')
        print('Number Of Standing Arrears = 4 \nHistory Of Arrears = 8')
        print('EMAIL ID:ravichandran12@gmail.com')
    elif '68' in command:
        print('RAJUARAVIND\n18IT1122')
        print('DOB:29-06-2001')
        print('10th Percentage = 94.00 \n12th Percentage = 79.00 \nCGPA = 6.86')
        print('Number Of Standing Arrears = 12 \nHistory Of Arrears = 15')
        print('EMAIL ID:rajamanojsanker@gmail.com')
    elif '69' in command:
        print('RAMYA\n18IT1257')
        print('DOB:20-12-2000')
        print('10th Percentage = 94.00 \n12th Percentage = 83.00 \nCGPA = 7.65')
        print('Number Of Standing Arrears = 0 \nHistory Of Arrears = 1')
        print('EMAIL ID:ramyalnarayanan20@gmail.com')
    elif '71' in command:
        print('RICARDO JOHN PINTO\n18IT1117')
        print('DOB:27-08-2000')
        print('10th Percentage = 92.80 \n12th Percentage = 62.50 \nCGPA = 7.22')
        print('Number Of Standing Arrears = 11 \nHistory Of Arrears = 13')
        print('EMAIL ID:arjpint@gmail.com')
    elif '72' in command:
        print('ROSHINI K\n18IT1234')
        print('DOB:21-12-2000')
        print('10th Percentage = 91.40 \n12th Percentage = 82.25 \nCGPA = 7.61')
        print('Number Of Standing Arrears = 0 \nHistory Of Arrears = 0')
        print('EMAIL ID:roshiniroshu2000@gmail.com')
    elif '73' in command:
        print('ROSHINI K\n18IT1251')
        print('DOB:13-12-2000')
        print('10th Percentage = 78.00 \n12th Percentage = 76.25 \nCGPA = 7.50')
        print('Number Of Standing Arrears = 0 \nHistory Of Arrears = 1')
        print('EMAIL ID:roshinirose1312@gmail.com')
    elif '74' in command:
        print('SABITHA\n18IT1238')
        print('DOB:15-11-2000')
        print('10th Percentage = 87.60 \n12th Percentage = 83.50 \nCGPA = 7.74')
        print('Number Of Standing Arrears = 3 \nHistory Of Arrears = 4')
        print('EMAIL ID:sabima5757@gmail.com')
    elif '75' in command:
        print('SACHIN\n18IT1130')
        print('DOB:19-07-2001')
        print('10th Percentage = 79.20 \n12th Percentage = 62.25 \nCGPA = 7.30')
        print('Number Of Standing Arrears = 17 \nHistory Of Arrears = 17')
        print('EMAIL ID:iamthesoldiersachin@gmail.com')
    elif '76' in command:
        print('SAHAYA RINOSHA\n18IT1105')
        print('DOB:01-09-2000')
        print('10th Percentage = 93.00 \n12th Percentage = 71.58 \nCGPA = 8.46')
        print('Number Of Standing Arrears = 0 \nHistory Of Arrears = 1')
        print('EMAIL ID:rinoshaagabit20@gmail.com')
    elif '77' in command:
        print('SAI SIDDARTH \n18IT1273')
        print('DOB:10-10-2000')
        print('10th Percentage = 91.20 \n12th Percentage = 73.83 \nCGPA = 7.47')
        print('Number Of Standing Arrears = 2 \nHistory Of Arrears = 4')
        print('EMAIL ID:saisiddharthp8@gmail.com')
    elif '78' in command:
        print('SANJAY SAGAR\n18IT1124')
        print('DOB:10-10-2000')
        print('10th Percentage = 0.68 \n12th Percentage = 64.00 \nCGPA = 6.95')
        print('Number Of Standing Arrears = 11 \nHistory Of Arrears = 12')
        print('EMAIL ID:sanjaysat1006@gmail.com')
    elif '79' in command:
        print('SARAVANASUBBIAH\n18IT1206')
        print('DOB:05-06-2001')
        print('10th Percentage = 92.00 \n12th Percentage = 85.00 \nCGPA = 7.36')
        print('Number Of Standing Arrears = 0 \nHistory Of Arrears = 2')
        print('EMAIL ID:saravanasjit@gmail.com')
    elif '80' in command:
        print('SARU PRABHA\n18IT1203')
        print('DOB:16-06-2001')
        print('10th Percentage = 99.20 \n12th Percentage = 86.25 \nCGPA = 8.96')
        print('Number Of Standing Arrears = 0 \nHistory Of Arrears = 0')
        print('EMAIL ID:saruprabha2001@gmail.com')
    elif '81' in command:
        print('SASI KUMAR\n18IT1127')
        print('DOB:16-09-2000')
        print('10th Percentage = 80.20 \n12th Percentage = 64.58 \nCGPA = 7.12')
        print('Number Of Standing Arrears = 4 \nHistory Of Arrears = 7')
        print('EMAIL ID:sasiravi1609@gmail.com')
    elif '83' in command:
        print('SHARMILA\n18IT1231')
        print('DOB:11-03-2001')
        print('10th Percentage = 93.00 \n12th Percentage = 79.58 \nCGPA = 8.34')
        print('Number Of Standing Arrears = 0 \nHistory Of Arrears = 0')
        print('EMAIL ID:sharmilaanand2013@gmail.com')
    elif '84' in command:
        print('SHRUTHIKA\n18IT1221')
        print('DOB:28-08-2000')
        print('10th Percentage = 98.00 \n12th Percentage = 86.25 \nCGPA = 8.72')
        print('Number Of Standing Arrears = 0 \nHistory Of Arrears = 0')
        print('EMAIL ID:shruthikaa28@gmail.com')
    elif '85' in command:
        print('SIDDARTH\n18IT1107')
        print('DOB:12-01-2001')
        print('10th Percentage = 84.40 \n12th Percentage = 73.58 \nCGPA = 6.97')
        print('Number Of Standing Arrears = 6 \nHistory Of Arrears = 8')
        print('EMAIL ID:siddarthsibhu2001@gmail.com')
    elif '86' in command:
        print('SIVANESH\n18IT1264')
        print('DOB:02-09-2000')
        print('10th Percentage = 88.60 \n12th Percentage = 81.30 \nCGPA = 7.24')
        print('Number Of Standing Arrears = 2 \nHistory Of Arrears = 6')
        print('EMAIL ID:sivaneshm02@gmail.com')
    elif '87' in command:
        print('SIVA SHANKAR\n18IT1209')
        print('DOB:10-12-2000')
        print('10th Percentage = 96.60 \n12th Percentage = 86.33 \nCGPA = 8.44')
        print('Number Of Standing Arrears = 0 \nHistory Of Arrears = 0')
        print('EMAIL ID:sivashankar1326@gmail.com')
    elif '88' in command:
        print('SNEHA K\n18IT1271')
        print('DOB:11-05-2001')
        print('10th Percentage = 80.40 \n12th Percentage = 54.25 \nCGPA = 6.92')
        print('Number Of Standing Arrears = 1 \nHistory Of Arrears = 4')
        print('EMAIL ID:sneha1105201@gmail.com')
    elif '89' in command:
        print('SNEHA M\n18IT1226')
        print('DOB:14-09-2000')
        print('10th Percentage = 94.00 \n12th Percentage = 81.40 \nCGPA = 7.48')
        print('Number Of Standing Arrears = 2 \nHistory Of Arrears = 5')
        print('EMAIL ID:sneha.mohan14092000@gmail.com')
    elif '90' in command:
        print('SRIDHARAN\n18IT1258')
        print('DOB:15-09-2000')
        print('10th Percentage = 85.80 \n12th Percentage = 78.33 \nCGPA = 7.47')
        print('Number Of Standing Arrears = 0 \nHistory Of Arrears = 4')
        print('EMAIL ID:sridharanbabu100@gmail.com')
    elif '91' in command:
        print('SRI SANJITHA\n18IT1222')
        print('DOB:18-05-2001')
        print('10th Percentage = 96.20 \n12th Percentage = 82.16 \nCGPA = 7.69')
        print('Number Of Standing Arrears = 0 \nHistory Of Arrears = 0')
        print('EMAIL ID:srivadivelan2001@gmail.com')
    elif '92' in command:
        print('SUBHALAKSHMI\n18IT1239')
        print('DOB:23-07-2001')
        print('10th Percentage = 83.60 \n12th Percentage = 79.41 \nCGPA = 8.31')
        print('Number Of Standing Arrears = 0 \nHistory Of Arrears = 0')
        print('EMAIL ID:subhalakshmirajakumar@gmail.com')
    elif '93' in command:
        print('SUBHA SHREE\n18IT1244')
        print('DOB:14-08-2000')
        print('10th Percentage = 87.45 \n12th Percentage = 86.08 \nCGPA = 8.61')
        print('Number Of Standing Arrears = 0 \nHistory Of Arrears = 0')
        print('EMAIL ID:srsubhashree14@gmail.com')
    elif '94' in command:
        print('SUJAY KANNA \n 18IT1241')
        print('DOB:20-07-2000')
        print('10th Percentage = 83.65 \n12th Percentage = 74.08 \nCGPA = 6.86')
        print('Number Of Standing Arrears = 8 \nHistory Of Arrears = 9')
        print('EMAIL ID:sujaykanna123@gmail.com')
    elif '96' in command:
        print('TAMIL MOZHI\n18IT1801')
        print('DOB:22-10-1999')
        print('10th Percentage = 85.20 \n12th Percentage = 72.16 \nCGPA = 7.45')
        print('Number Of Standing Arrears = 0 \nHistory Of Arrears = 4')
        print('EMAIL ID:mozhitamil926@gmail.com')
    elif '97' in command:
        print('THARANYA\n18IT1104')
        print('DOB:01-11-2000')
        print('10th Percentage = 88.00 \n12th Percentage = 76.33 \nCGPA = 7.89')
        print('Number Of Standing Arrears = 0 \nHistory Of Arrears = 3')
        print('EMAI ID:tharanyatharu17@gmail.com')
    elif '98' in command:
        print('UMANATH\n18IT1219')
        print('DOB:09-10-2000')
        print('10th Percentage = 95.80 \n12th Percentage = 88.16 \nCGPA = 7.55')
        print('Number Of Standing Arrears = 0 \nHistory Of Arrears = 2')
        print('EMAIL ID:sathyasathya20001@gmail.com')
    elif '99' in command:
        print('UMAYAL\n18IT1204')
        print('DOB:09-10-2000')
        print('10th Percentage = 93.00 \n12th Percentage = 84.00 \nCGPA = 8.87')
        print('Number Of Standing Arrears = 0 \nHistory Of Arrears =0 ')
        print('EMAIL ID:umayal0910@gmail.com')
    elif '100' in command:
        print('VASANTH E\n18IT1260')
        print('DOB:17-10-2000')
        print('10th Percentage = 88.60 \n12th Percentage = 73.90 \nCGPA = 7.15')
        print('Number Of Standing Arrears = 3 \nHistory Of Arrears = 4')
        print('EMAIL ID:eswarvasanth17@gmail.com')
    elif '101' in command:
        print('VASANTH MS\n18IT1223')
        print('DOB:26-06-2001')
        print('10th Percentage = 85.00 \n12th Percentage = 81.42\nCGPA = 7.81')
        print('Number Of Standing Arrears = 0 \nHistory Of Arrears = 0')
        print('EMAIL ID:vasanthselvam06@gmail.com')
    elif '102' in command:
        print('VETHAVARNA\n18IT1220')
        print('DOB:03-03-2001')
        print('10th Percentage = 88.80 \n12th Percentage = 86.33 \nCGPA = 7.20')
        print('Number Of Standing Arrears = 2 \nHistory Of Arrears = 5')
        print('EMAIL ID:vethavarnabindhu@gmail.com')
    elif '103' in command:
        print('VEVEGHAA\n18IT1243')
        print('DOB:30-09-2000')
        print('10th Percentage = 91.45 \n12th Percentage = 71.25 \nCGPA = 7.84')
        print('Number Of Standing Arrears = 0 \nHistory Of Arrears = 1')
        print('EMAIL ID:nrveve3009@gmail.com')
    elif '105' in command:
        print('VIVIN KUMAR\n18IT1118')
        print('DOB:23-06-2000')
        print('10th Percentage = 68.40 \n12th Percentage = 59.25 \nCGPA = 7.09')
        print('Number Of Standing Arrears = 5 \nHistory Of Arrears = 7')
        print('EMAIL ID:vivinkumar2000@gmail.com')
    elif '106' in command:
        print('YOGA LAKSHMI\n18IT1246')
        print('DOB:13-04-2001')
        print('10th Percentage = 87.00 \n12th Percentage = 76.00 \nCGPA = 7.71')
        print('Number Of Standing Arrears = 0 \nHistory Of Arrears = 1')
        print('EMAIL ID:yogashanmugam1304@gmail.com')
    elif '107' in command:
        print('YOGESH KUMAR\n18IT1224')
        print('DOB:10-08-2000')
        print('10th Percentage = 96.00 \n12th Percentage = 86.00 \nCGPA = 7.63')
        print('Number Of Standing Arrears = 0 \n History Of Arrears = 1')
        print('EMAIL ID:gyogeshkumar1008@gmail.com')
    elif '108' in command:
        print('YOGESHWAR\n18IT1211')
        print('DOB:04-10-2000')
        print('10th Percentage = 91.20 \n12th Percentage = 83.42 \nCGPA = 7.36')
        print('Number Of Standing Arrears = 4 \nHistory Of Arrears = 8')
        print('EMAIL ID:asyogesh.04@gmail.com')
    elif '109' in command:
        print('YUVASTIYA S\n18IT1125')
        print('DOB:31-10-2000')
        print('10th Percentage = 97.20 \n12th Percentage = 81.91 \nCGPA = 8.72')
        print('Number Of Standing Arrears = 0 \nHistory Of Arrears = 1')
        print('EMAIL ID:yuvastiya2022batch@gmail.com')
    else:
        talk('Please say the command again')
        print('Please say the command again')

while True:
    run_sprach()
