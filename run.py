import pyautogui
import map
from time import sleep
import time

class Main():
    _parcel_stones = 0
    _total_size = 0
    _bag_size = 24    
    _empty_space = 3
    _npc_rq_x = 0
    _npc_rq_y = 0
    _npc_helper_x = 0
    _npc_helper_y = 0
    _first_bag_x = -20
    _first_bag_y = -170
    _secound_bag_x = 15
    _secound_bag_y = 60
    _space_between = 42
    _time_start = 0
    _time_finish = 0

    def init(self):        
        print('Godswar Auto Random Quest\n\n')
        
        self.readInputs()
        self.prepareVars()
        self.start()

    def stopWatch(self, value):
        valueD = (((value/365)/24)/60)
        Days = int (valueD)

        valueH = (valueD-Days)*365
        Hours = int(valueH)

        valueM = (valueH - Hours)*24
        Minutes = int(valueM)

        valueS = (valueM - Minutes)*60
        Seconds = int(valueS)

        print('Time spend: ' + str(Minutes) + 'm ' + str(Seconds) + 's')

    def readInputs(self):
        while True:
            try:
                input_value = input('Digite a quantidade de Parcel Stone que voce possui: ')
                self._parcel_stones = int(input_value)

                if self._parcel_stones < 0 or self._parcel_stones > 3:
                    raise Exception('Error')
                
                # Break the loop
                break

            except:
                print('Digite um número de 0 à 3')
        
    def definePositionsNPC(self):
        input('Coloque o mouse no NPC Random Quest e dê enter:')
        self._npc_rq_x, self._npc_rq_y = pyautogui.position()
        
        input('Coloque o mouse no NPC Helper e dê enter:')
        self._npc_helper_x, self._npc_helper_y = pyautogui.position()

    def prepareVars(self):
        self._total_size = self._bag_size + (self._bag_size * self._parcel_stones)

    def windowsFocus(self):
        
        while True:
            try:
                x, y = pyautogui.locateCenterOnScreen('images/window_point.png', grayscale=True, confidence=0.7)
                pyautogui.moveTo(x, (y - 30))
                pyautogui.click()  
                break
                
            except:
                pass
    
    def findImage(self, image, addXPos=0, addYPos=0):       
        
        while True:
            try:
                x, y = pyautogui.locateCenterOnScreen('images/' + image + '.png', grayscale=True, confidence=0.97)
                pyautogui.moveTo((x + addXPos), (y + addYPos))
                pyautogui.click()
                break
                
            except:
                pass

    def findImageRightClick(self, image, addXPos=0, addYPos=0):       
        
        while True:
            try:
                x, y = pyautogui.locateCenterOnScreen('images/' + image + '.png', grayscale=True, confidence=0.97)
                pyautogui.moveTo((x + addXPos), (y + addYPos))
                pyautogui.rightClick()
                break
                
            except:
                pass

    def start(self):

        # Define NPC Positions
        self.definePositionsNPC()

        # Start Watchtime
        self._time_start = time.time()

        # Focus on window
        self.windowsFocus()

        for bag in range((self._total_size - self._empty_space)):

            print(str(bag + 1) + '/' + str(self._total_size - self._empty_space))

            # Abrir nova bag quando preencher a primeira
            if bag == 24: self.findImage('new_bag')

            #Step 1
            pyautogui.moveTo(self._npc_rq_x, self._npc_rq_y)
            pyautogui.click()

            #Step 2
            self.findImage('random_quest')
            
            #Step 3
            self.findImage('claim_quest_sack')
            
            #Step 4
            self.findImage('ok_button')            

            #Step 5
            pyautogui.moveTo(self._npc_helper_x, self._npc_helper_y)
            pyautogui.click(duration=0.05)

            #Step 6
            self.findImage('batch')
            self.findImage('window_sack')

            #Step 7
            if bag > 23:
                self.findImageRightClick('angel',
                    (self._secound_bag_x + (self._space_between * map.secoundBag[bag - 24][0])), 
                    (self._secound_bag_y + (self._space_between * map.secoundBag[bag - 24][1])))
            else:
                self.findImageRightClick('new_bag',
                    (self._first_bag_x + (self._space_between * map.firstBag[bag][0])), 
                    (self._first_bag_y + (self._space_between * map.firstBag[bag][1])))
            
            #Step 8
            pyautogui.moveTo(self._npc_helper_x, self._npc_helper_y)
            pyautogui.click(duration=0.05)

            #Step 9
            self.findImage('batch')
            self.findImage('finish')
        
        # Finish Watchtime
        self._time_finish = time.time()
        self.stopWatch(self._time_finish - self._time_start)

        # Close client
        pyautogui.hotkey('alt', 'f4')
        self.findImage('ok_close_client')

        # Open Client
        self.findImage('client')

        # Type login
        self.findImage('login_field', 0, 15)
        pyautogui.typewrite(self.user_login)

        # Type Password
        self.findImage('login_field', 0, 15)
        pyautogui.typewrite(self.user_password)

        # Login
        pyautogui.press('enter')
        self.findImage('timeout_login')
        sleep(4)
        pyautogui.press('enter')
        sleep(2)
        pyautogui.press('enter')
        self.findImage('timeout_login')
        pyautogui.press('enter')

        # Open Bag

