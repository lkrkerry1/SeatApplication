import utils.constants
import display.gui

def main():
    if utils.constants.DEBUG:
        print("Project Dir: %s" % utils.constants.PROJECT_DIR)
        print("Data Dir: %s" % utils.constants.DATA_DIR)
        print("CLI Start")
    displayer = display.gui.GUI()
    displayer.start()

if __name__ == "__main__":
    main()