import cv2
import os


directory= 'SignImage48x48/'
print(os.getcwd())

if not os.path.exists(directory):
    os.mkdir(directory)
if not os.path.exists(f'{directory}/blank'):
    os.mkdir(f'{directory}/blank')
    

for i in range(65,91):
    letter  = chr(i)
    if not os.path.exists(f'{directory}/{letter}'):
        os.mkdir(f'{directory}/{letter}')




import os
import cv2
cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    count = {
             'a': len(os.listdir(directory+"/a")),
             'b': len(os.listdir(directory+"/b")),
             'c': len(os.listdir(directory+"/c")),
             'd': len(os.listdir(directory+"/d")),
             'e': len(os.listdir(directory+"/e")),
             'f': len(os.listdir(directory+"/f")),
             'g': len(os.listdir(directory+"/g")),
             'h': len(os.listdir(directory+"/h")),
             'i': len(os.listdir(directory+"/i")),
             'j': len(os.listdir(directory+"/j")),
             'k': len(os.listdir(directory+"/k")),
             'l': len(os.listdir(directory+"/l")),
             'm': len(os.listdir(directory+"/m")),
             'n': len(os.listdir(directory+"/n")),
             'o': len(os.listdir(directory+"/o")),
             'p': len(os.listdir(directory+"/p")),
             'q': len(os.listdir(directory+"/q")),
             'r': len(os.listdir(directory+"/r")),
             's': len(os.listdir(directory+"/s")),
             't': len(os.listdir(directory+"/t")),
             'u': len(os.listdir(directory+"/u")),
             'v': len(os.listdir(directory+"/v")),
             'w': len(os.listdir(directory+"/w")),
             'x': len(os.listdir(directory+"/x")),
             'y': len(os.listdir(directory+"/y")),
             'z': len(os.listdir(directory+"/z")),
             'blank': len(os.listdir(directory+"/blank"))
             }

    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame,(0,40),(300,300),(255,255,255),2)
    cv2.imshow("data",frame)
    frame=frame[40:300,0:300]
    cv2.imshow("ROI",frame)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame,(48,48))
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(os.path.join(directory+'A/'+str(count['a']))+'.jpg',frame)
    if interrupt & 0xFF == ord('b'):
        cv2.imwrite(os.path.join(directory+'B/'+str(count['b']))+'.jpg',frame)
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(os.path.join(directory+'C/'+str(count['c']))+'.jpg',frame)
    if interrupt & 0xFF == ord('d'):
        cv2.imwrite(os.path.join(directory+'D/'+str(count['d']))+'.jpg',frame)
    if interrupt & 0xFF == ord('e'):
        cv2.imwrite(os.path.join(directory+'E/'+str(count['e']))+'.jpg',frame)
    if interrupt & 0xFF == ord('f'):
        cv2.imwrite(os.path.join(directory+'F/'+str(count['f']))+'.jpg',frame)
    if interrupt & 0xFF == ord('g'):
        cv2.imwrite(os.path.join(directory+'G/'+str(count['g']))+'.jpg',frame)
    if interrupt & 0xFF == ord('h'):
        cv2.imwrite(os.path.join(directory+'H/'+str(count['h']))+'.jpg',frame)
    if interrupt & 0xFF == ord('i'):
        cv2.imwrite(os.path.join(directory+'I/'+str(count['i']))+'.jpg',frame)
    if interrupt & 0xFF == ord('j'):
        cv2.imwrite(os.path.join(directory+'J/'+str(count['j']))+'.jpg',frame)
    if interrupt & 0xFF == ord('k'):
        cv2.imwrite(os.path.join(directory+'K/'+str(count['k']))+'.jpg',frame)
    if interrupt & 0xFF == ord('l'):
        cv2.imwrite(os.path.join(directory+'L/'+str(count['l']))+'.jpg',frame)
    if interrupt & 0xFF == ord('m'):
        cv2.imwrite(os.path.join(directory+'M/'+str(count['m']))+'.jpg',frame)
    if interrupt & 0xFF == ord('n'):
        cv2.imwrite(os.path.join(directory+'N/'+str(count['n']))+'.jpg',frame)
    if interrupt & 0xFF == ord('o'):
        cv2.imwrite(os.path.join(directory+'O/'+str(count['o']))+'.jpg',frame)
    if interrupt & 0xFF == ord('p'):
        cv2.imwrite(os.path.join(directory+'P/'+str(count['p']))+'.jpg',frame)
    if interrupt & 0xFF == ord('q'):
        cv2.imwrite(os.path.join(directory+'Q/'+str(count['q']))+'.jpg',frame)
    if interrupt & 0xFF == ord('r'):
        cv2.imwrite(os.path.join(directory+'R/'+str(count['r']))+'.jpg',frame)
    if interrupt & 0xFF == ord('s'):
        cv2.imwrite(os.path.join(directory+'S/'+str(count['s']))+'.jpg',frame)
    if interrupt & 0xFF == ord('t'):
        cv2.imwrite(os.path.join(directory+'T/'+str(count['t']))+'.jpg',frame)
    if interrupt & 0xFF == ord('u'):
        cv2.imwrite(os.path.join(directory+'U/'+str(count['u']))+'.jpg',frame)
    if interrupt & 0xFF == ord('v'):
        cv2.imwrite(os.path.join(directory+'V/'+str(count['v']))+'.jpg',frame)
    if interrupt & 0xFF == ord('w'):
        cv2.imwrite(os.path.join(directory+'W/'+str(count['w']))+'.jpg',frame)
    if interrupt & 0xFF == ord('x'):
        cv2.imwrite(os.path.join(directory+'X/'+str(count['x']))+'.jpg',frame)
    if interrupt & 0xFF == ord('y'):
        cv2.imwrite(os.path.join(directory+'Y/'+str(count['y']))+'.jpg',frame)
    if interrupt & 0xFF == ord('z'):
        cv2.imwrite(os.path.join(directory+'Z/'+str(count['z']))+'.jpg',frame)
    if interrupt & 0xFF == ord('.'):
        cv2.imwrite(os.path.join(directory+'blank/' + str(count['blank']))+ '.jpg',frame)


    
